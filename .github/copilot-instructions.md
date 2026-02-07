# GitHub Copilot Instructions - Home Assistant Integration Development

## Project Context

This repository is a template for developing Home Assistant custom integrations. All code must follow the Home Assistant Integration Quality Scale standards.

## Environment

- **Python Version:** 3.14.2 (meets HA 2025.2+ requirement for Python 3.13+)
- **Home Assistant Version:** 2026.2.0
- **Testing:** pytest with pytest-homeassistant-custom-component
- **Code Quality:** Ruff (linter/formatter), mypy (type checker)
- **Architecture:** Async-first, DataUpdateCoordinator pattern

## Mandatory Requirements

### 1. Python Version Compatibility
- Code must be compatible with Python 3.13+
- Use modern type hints: `list[str]` not `List[str]`
- Use `dict[str, Any]` not `Dict[str, Any]`
- Import from `collections.abc` not `typing` for ABC types

### 2. Async-First Architecture
ALL I/O operations MUST be asynchronous:

```python
# ✅ Correct - Async library
import aiohttp

async def fetch_data(self):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# ❌ Wrong - Blocking operation
import requests

async def fetch_data(self):
    return requests.get(url).json()  # Blocks event loop!

# ✅ Acceptable - If no async library exists
async def fetch_data(self):
    return await self.hass.async_add_executor_job(
        requests.get, url
    )
```

### 3. DataUpdateCoordinator Pattern

For ANY integration that polls data, use DataUpdateCoordinator:

```python
from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.exceptions import ConfigEntryAuthFailed

class MyIntegrationCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator to manage data fetching."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: MyApiClient,
    ) -> None:
        """Initialize coordinator."""
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
            always_update=False,  # Set False if data implements __eq__
        )
        self.client = client

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from API."""
        try:
            return await self.client.async_get_data()
        except AuthenticationError as err:
            raise ConfigEntryAuthFailed("Invalid credentials") from err
        except ConnectionError as err:
            raise UpdateFailed(f"Connection error: {err}") from err
```

### 4. Config Flow (Mandatory)

ALL new integrations MUST use config flow UI setup:

```python
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PASSWORD, CONF_USERNAME
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol

class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle user step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await self._async_validate_input(user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                await self.async_set_unique_id(info["unique_id"])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_USERNAME): str,
                vol.Required(CONF_PASSWORD): str,
            }),
            errors=errors,
        )
```

### 5. Entity Base Class Pattern

Use CoordinatorEntity for automatic update handling:

```python
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

class MyIntegrationEntity(CoordinatorEntity[MyIntegrationCoordinator]):
    """Base entity for My Integration."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MyIntegrationCoordinator,
        device_id: str,
    ) -> None:
        """Initialize entity."""
        super().__init__(coordinator)
        self._device_id = device_id

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        device = self.coordinator.data[self._device_id]
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            name=device["name"],
            manufacturer="My Manufacturer",
            model=device["model"],
            sw_version=device.get("firmware"),
        )

    @property
    def unique_id(self) -> str:
        """Return unique ID."""
        return f"{DOMAIN}_{self._device_id}_{self._entity_type}"

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return (
            super().available
            and self._device_id in self.coordinator.data
        )
```

### 6. Error Handling

Proper error handling is REQUIRED:

```python
# In coordinator _async_update_data():
async def _async_update_data(self) -> dict[str, Any]:
    """Fetch data."""
    try:
        data = await self.client.async_get_data()
    except AuthenticationError as err:
        # Triggers reauth flow automatically
        raise ConfigEntryAuthFailed("Invalid credentials") from err
    except ConnectionError as err:
        # Marks entities unavailable, logs once
        raise UpdateFailed(f"Connection error: {err}") from err
    except Exception as err:
        # Catch-all for unexpected errors
        raise UpdateFailed(f"Unexpected error: {err}") from err
    else:
        return data
```

### 7. Type Hints (Required)

ALL functions, methods, and variables must have type hints:

```python
from __future__ import annotations

from typing import Any, Final

DOMAIN: Final = "my_integration"
DEFAULT_TIMEOUT: Final[int] = 30

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up from a config entry."""
    coordinator = MyIntegrationCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

## Integration Quality Scale

### Bronze Tier (Minimum for Core)
- ✅ Config flow UI setup
- ✅ Automated setup tests
- ✅ Basic coding standards
- ✅ Proper manifest.json

### Silver Tier (Reliability)
- ✅ Error handling (auth failures, offline devices)
- ✅ Entity availability management
- ✅ Troubleshooting documentation
- ✅ Log-once patterns for connection issues

### Gold Tier (Feature Complete)
- ✅ Full async codebase
- ✅ Comprehensive test coverage
- ✅ Complete type annotations
- ✅ Efficient data handling

### Platinum Tier (Excellence)
- ✅ All coding standards and best practices
- ✅ Clear code comments
- ✅ Optimal performance
- ✅ Active code ownership

## manifest.json Schema

Every integration must have a properly configured manifest:

```json
{
  "domain": "my_integration",
  "name": "My Integration",
  "version": "1.0.0",
  "codeowners": ["@github_username"],
  "config_flow": true,
  "dependencies": [],
  "documentation": "https://github.com/user/my-integration",
  "integration_type": "hub",
  "iot_class": "local_polling",
  "issue_tracker": "https://github.com/user/my-integration/issues",
  "loggers": ["my_device_library"],
  "requirements": ["my-device-library==1.2.3"],
  "quality_scale": "bronze"
}
```

### integration_type Values
- `device` - Single device
- `hub` - Hub/bridge with multiple devices
- `service` - Cloud service
- `virtual` - No physical device
- `helper` - Utility integration
- `hardware` - Hardware platform (USB stick, etc.)
- `system` - System integration
- `entity` - Entity namespace provider

### iot_class Values
- `local_polling` - Local device, periodically polled
- `local_push` - Local device, pushes updates
- `cloud_polling` - Cloud service, periodically polled
- `cloud_push` - Cloud service, pushes updates
- `calculated` - Derives from other entities
- `assumed_state` - State is assumed, not confirmed

## File Structure

Standard integration structure:

```
custom_components/my_integration/
├── __init__.py           # Integration setup/teardown
├── manifest.json         # Integration metadata
├── config_flow.py        # UI configuration
├── const.py              # Constants
├── coordinator.py        # DataUpdateCoordinator
├── entity.py             # Base entity class
├── sensor.py             # Sensor platform
├── binary_sensor.py      # Binary sensor platform
├── switch.py             # Switch platform
├── strings.json          # UI strings
└── translations/
    └── en.json           # English translations
```

## Testing Requirements

ALL integrations must have tests:

```python
# tests/conftest.py
import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture
def mock_client():
    """Create a mock API client."""
    with patch("custom_components.my_integration.MyApiClient") as mock:
        client = mock.return_value
        client.async_get_data.return_value = {"devices": []}
        yield client

# tests/test_config_flow.py
async def test_form(hass: HomeAssistant, mock_client) -> None:
    """Test we get the form."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["errors"] == {}

async def test_form_invalid_auth(hass: HomeAssistant, mock_client) -> None:
    """Test invalid auth handling."""
    mock_client.async_authenticate.side_effect = InvalidAuth

    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {"host": "1.2.3.4", "username": "test", "password": "test"},
    )

    assert result2["type"] == "form"
    assert result2["errors"] == {"base": "invalid_auth"}
```

## Common Pitfalls to Avoid

### ❌ Blocking the Event Loop
```python
# Wrong
data = requests.get(url).json()  # Blocks entire HA!

# Correct
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

### ❌ Polling in __init__.py
```python
# Wrong - inefficient, creates race conditions
async def async_setup_entry(hass, entry):
    async def async_update():
        data = await fetch_data()
        # Update entities...

    hass.helpers.event.async_track_time_interval(async_update, 30)

# Correct - use DataUpdateCoordinator
async def async_setup_entry(hass, entry):
    coordinator = MyCoordinator(hass, client)
    await coordinator.async_config_entry_first_refresh()
```

### ❌ Missing Unique IDs
```python
# Wrong
@property
def unique_id(self) -> str:
    return self._name  # Name can change!

# Correct
@property
def unique_id(self) -> str:
    return f"{DOMAIN}_{self._device_id}_{self._sensor_type}"
```

### ❌ Not Handling Unavailability
```python
# Wrong - entity stays available even when device offline
class MySensor(SensorEntity):
    pass  # No availability check

# Correct
class MySensor(CoordinatorEntity):
    @property
    def available(self) -> bool:
        return super().available and self._device_id in self.coordinator.data
```

## Resources

- **Agent Spec:** `resources/agents/ha-integration-agent/ha_integration_agent_spec.md`
- **Environment Setup:** `ha-dev-environment-requirements.md`
- **Example Integration:** `custom_components/example_integration/`
- **Official Docs:** https://developers.home-assistant.io/

## Code Quality Commands

```bash
# Lint and auto-fix
ruff check custom_components/ --fix

# Format code
ruff format custom_components/

# Type check
mypy custom_components/

# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=custom_components --cov-report=html

# All quality checks
pre-commit run --all-files
```

## Summary

When generating code for this project:
1. ✅ Use DataUpdateCoordinator for polling
2. ✅ Config flows, not YAML
3. ✅ Async everything (aiohttp, not requests)
4. ✅ Full type hints (modern Python 3.13+ syntax)
5. ✅ Proper error handling (UpdateFailed, ConfigEntryAuthFailed)
6. ✅ Unique IDs for all entities
7. ✅ Device info grouping
8. ✅ Availability handling
9. ✅ Tests for config flow and setup
10. ✅ Aim for Bronze tier minimum, Silver/Gold recommended
