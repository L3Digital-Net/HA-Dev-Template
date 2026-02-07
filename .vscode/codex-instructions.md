# VS Code Codex Instructions - Home Assistant Integration Development

## Project Type
Home Assistant Custom Integration Development Template

## Environment
- Python 3.12.3
- Home Assistant 2026.2.0
- Testing: pytest + pytest-homeassistant-custom-component
- Code Quality: Ruff (linter/formatter) + mypy (type checker)

## Core Principles

### 1. DataUpdateCoordinator is MANDATORY
For any integration that polls data, use DataUpdateCoordinator pattern:

```python
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed

class MyCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    def __init__(self, hass: HomeAssistant, client: MyApiClient) -> None:
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )
        self.client = client

    async def _async_update_data(self) -> dict[str, Any]:
        try:
            return await self.client.async_get_data()
        except AuthError as err:
            raise ConfigEntryAuthFailed from err
        except ConnectionError as err:
            raise UpdateFailed(f"Connection error: {err}") from err
```

### 2. Config Flow is MANDATORY
No YAML configuration for new integrations:

```python
from homeassistant import config_entries
import voluptuous as vol

class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            # Validate and create entry
            pass
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({...}),
            errors=errors,
        )
```

### 3. Async-First Architecture
ALL I/O must be async:

```python
# ✅ Correct
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()

# ❌ Wrong - blocks event loop
data = requests.get(url).json()
```

### 4. Full Type Hints
Use modern Python 3.13+ syntax:

```python
from __future__ import annotations
from typing import Any, Final

DOMAIN: Final = "my_integration"

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up from config entry."""
```

### 5. CoordinatorEntity Pattern
For entities that use coordinator data:

```python
from homeassistant.helpers.update_coordinator import CoordinatorEntity

class MyEntity(CoordinatorEntity[MyCoordinator]):
    _attr_has_entity_name = True

    @property
    def unique_id(self) -> str:
        return f"{DOMAIN}_{self._device_id}_{self._type}"

    @property
    def available(self) -> bool:
        return super().available and self._device_id in self.coordinator.data
```

## Integration Quality Scale

**Bronze (Minimum):**
- Config flow + tests + manifest

**Silver (Reliability):**
- Error handling + availability + docs

**Gold (Complete):**
- Full async + type coverage + comprehensive tests

**Platinum (Excellence):**
- All best practices + maintenance

## File Structure Template

```
custom_components/my_integration/
├── __init__.py           # Setup/teardown
├── manifest.json         # Metadata
├── config_flow.py        # Config flow
├── const.py              # Constants
├── coordinator.py        # DataUpdateCoordinator
├── entity.py             # Base entity class
├── sensor.py             # Sensor platform
└── strings.json          # UI strings
```

## manifest.json Template

```json
{
  "domain": "my_integration",
  "name": "My Integration",
  "version": "1.0.0",
  "config_flow": true,
  "integration_type": "device|hub|service",
  "iot_class": "local_polling|local_push|cloud_polling|cloud_push",
  "documentation": "https://github.com/...",
  "requirements": ["library==1.0.0"]
}
```

## Common Patterns

### Setup Entry
```python
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator = MyCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True
```

### Unload Entry
```python
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok
```

### Sensor Entity
```python
from homeassistant.components.sensor import SensorEntity

class MySensor(CoordinatorEntity[MyCoordinator], SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator: MyCoordinator, device_id: str) -> None:
        super().__init__(coordinator)
        self._device_id = device_id

    @property
    def native_value(self) -> float | None:
        return self.coordinator.data[self._device_id].get("temperature")
```

## Error Handling

```python
# In coordinator
async def _async_update_data(self):
    try:
        return await self.client.async_get_data()
    except AuthError as err:
        raise ConfigEntryAuthFailed from err  # Triggers reauth
    except ConnectionError as err:
        raise UpdateFailed(f"Connection error: {err}") from err  # Unavailable
```

## Testing Requirements

```python
# tests/test_config_flow.py
async def test_user_flow(hass: HomeAssistant) -> None:
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
```

## Quick Commands

```bash
# Lint & fix
ruff check . --fix

# Format
ruff format .

# Type check
mypy custom_components/

# Test
pytest tests/ -v

# All checks
pre-commit run --all-files
```

## Resources
- Agent spec: `resources/agents/ha-integration-agent/ha_integration_agent_spec.md`
- Environment guide: `ha-dev-environment-requirements.md`
- Example: `custom_components/example_integration/`
