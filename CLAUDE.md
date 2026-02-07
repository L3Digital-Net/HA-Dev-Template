# CLAUDE.md - Home Assistant Integration Development Template

This file provides guidance to Claude Code when working with this Home Assistant integration development template.

## Project Overview

This is a **production-ready template repository** for developing Home Assistant custom integrations. It includes:

- Complete Python 3.14.2 development environment
- Home Assistant 2026.2.0 with all core dependencies
- Testing framework (pytest + HA custom component support)
- Code quality tools (Ruff, mypy, pre-commit hooks)
- Example integration following HA best practices
- Specialized AI agent for HA development guidance
- Automated environment verification

**Purpose:** Enable developers to create high-quality Home Assistant integrations that meet or exceed the Integration Quality Scale standards (Bronze → Platinum tiers).

## Environment Setup

### Virtual Environment

**IMPORTANT:** Always work within the virtual environment:

```bash
# Activate virtual environment (REQUIRED before any work)
source venv/bin/activate

# Verify environment
python scripts/verify_environment.py
```

### Installed Versions

- **Python:** 3.14.2 (meets HA 2025.2+ requirement for Python 3.13+)
- **Home Assistant:** 2026.2.0
- **Testing:** pytest 9.0.0, pytest-homeassistant-custom-component 0.13.313
- **Code Quality:** Ruff 0.15.0, mypy 1.19.1, pre-commit 4.5.1

## Mandatory Development Patterns

### 1. DataUpdateCoordinator Pattern (REQUIRED)

For **ANY** integration that polls data, use DataUpdateCoordinator. This is non-negotiable.

```python
from datetime import timedelta
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.exceptions import ConfigEntryAuthFailed

class MyIntegrationCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator to manage data fetching."""

    def __init__(self, hass: HomeAssistant, client: MyApiClient) -> None:
        """Initialize coordinator."""
        super().__init__(
            hass,
            logger=_LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
            always_update=False,  # False if data implements __eq__
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

**Why:** Centralizes data fetching, handles errors properly, prevents duplicate polls, manages entity availability automatically.

### 2. Config Flow (REQUIRED)

ALL new integrations MUST use config flow UI setup. No YAML configuration.

```python
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
import voluptuous as vol

class MyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                info = await self._async_validate_input(user_input)
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            else:
                await self.async_set_unique_id(info["unique_id"])
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({...}),
            errors=errors,
        )
```

**Why:** Provides consistent UI experience, required for core integrations, mandatory for Bronze tier.

### 3. Async-First Architecture (REQUIRED)

ALL I/O operations must be asynchronous. Never block the event loop.

```python
# ✅ CORRECT - Async library
import aiohttp

async def fetch_data(self, url: str) -> dict[str, Any]:
    """Fetch data asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# ❌ WRONG - Blocks entire Home Assistant!
import requests

async def fetch_data(self, url: str) -> dict[str, Any]:
    """This BLOCKS the event loop!"""
    return requests.get(url).json()  # NEVER DO THIS

# ✅ ACCEPTABLE - If no async library exists
async def fetch_data(self, url: str) -> dict[str, Any]:
    """Use executor for sync operations."""
    return await self.hass.async_add_executor_job(
        requests.get, url
    )
```

**Why:** Home Assistant is async. Blocking operations freeze the entire system.

### 4. Full Type Hints (REQUIRED)

Use modern Python 3.13+ type hint syntax:

```python
from __future__ import annotations

from typing import Any, Final

# ✅ CORRECT - Modern syntax
DOMAIN: Final = "my_integration"
DEFAULT_TIMEOUT: Final[int] = 30

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
) -> bool:
    """Set up from a config entry."""
    data: dict[str, Any] = entry.data
    devices: list[str] = data.get("devices", [])

# ❌ WRONG - Old syntax
from typing import List, Dict

devices: List[str] = []  # Use list[str] instead
data: Dict[str, Any] = {}  # Use dict[str, Any] instead
```

**Why:** Type safety, IDE support, Gold tier requirement, modern Python standard.

### 5. CoordinatorEntity Pattern (REQUIRED)

For entities that use coordinator data:

```python
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceInfo

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
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            name=self.coordinator.data[self._device_id]["name"],
            manufacturer="My Manufacturer",
            model=self.coordinator.data[self._device_id]["model"],
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

**Why:** Automatic updates, proper availability handling, device grouping, unique IDs.

## Integration Quality Scale

### Bronze Tier (MINIMUM for all integrations)
- ✅ Config flow UI setup
- ✅ Automated setup tests
- ✅ Basic coding standards (Ruff passes)
- ✅ Proper manifest.json

### Silver Tier (Reliability)
- ✅ Proper error handling (auth failures, offline devices)
- ✅ Entity availability management
- ✅ Troubleshooting documentation
- ✅ Log-once patterns for connection issues

### Gold Tier (Feature Complete)
- ✅ Full async codebase (no blocking operations)
- ✅ Comprehensive test coverage
- ✅ Complete type annotations (mypy passes)
- ✅ Efficient data handling

### Platinum Tier (Excellence)
- ✅ All coding standards and best practices
- ✅ Clear code comments and documentation
- ✅ Optimal performance
- ✅ Active code ownership and maintenance

**Target:** Minimum Bronze tier, aim for Silver/Gold.

## File Structure

### Standard Integration Structure

```
custom_components/your_integration/
├── __init__.py           # Integration setup/teardown
├── manifest.json         # Metadata, dependencies, version
├── config_flow.py        # Config flow implementation
├── const.py              # Constants (DOMAIN, defaults)
├── coordinator.py        # DataUpdateCoordinator subclass
├── entity.py             # Base entity class (optional but recommended)
├── sensor.py             # Sensor platform (if applicable)
├── binary_sensor.py      # Binary sensor platform (if applicable)
├── switch.py             # Switch platform (if applicable)
├── strings.json          # UI strings and translations
└── translations/
    └── en.json           # English translations
```

### Test Structure

```
tests/
├── conftest.py           # Shared fixtures and mocks
├── test_config_flow.py   # Config flow tests
├── test_init.py          # Setup/unload tests
└── test_[platform].py    # Platform-specific tests
```

## Common Development Workflows

### Creating a New Integration

1. **Copy the example integration:**
   ```bash
   cp -r custom_components/example_integration custom_components/your_integration
   ```

2. **Update manifest.json:**
   - Change `domain` to your integration name
   - Update `name`, `documentation`, `issue_tracker`
   - Set appropriate `integration_type` and `iot_class`
   - Add `requirements` if using external libraries

3. **Update const.py:**
   - Change `DOMAIN` to match manifest
   - Add integration-specific constants

4. **Implement coordinator.py:**
   - Create DataUpdateCoordinator subclass
   - Implement `_async_update_data()`
   - Handle authentication and connection errors

5. **Create config_flow.py:**
   - Implement user step for initial setup
   - Add error handling
   - Create strings.json with UI text

6. **Implement entity platforms:**
   - Create platform files (sensor.py, switch.py, etc.)
   - Extend base entity class
   - Use CoordinatorEntity pattern

7. **Write tests:**
   - Config flow tests (user flow, error handling)
   - Setup/unload tests
   - Platform tests

8. **Run quality checks:**
   ```bash
   ruff check custom_components/your_integration/ --fix
   ruff format custom_components/your_integration/
   mypy custom_components/your_integration/
   pytest tests/ -v
   ```

### Testing and Quality Checks

```bash
# Activate virtual environment first
source venv/bin/activate

# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=custom_components.your_integration --cov-report=html

# Run specific test file
pytest tests/test_config_flow.py -v

# Lint and auto-fix
ruff check custom_components/ --fix

# Format code
ruff format custom_components/

# Type check
mypy custom_components/your_integration/

# Run all pre-commit hooks
pre-commit run --all-files

# Verify environment
python scripts/verify_environment.py
```

## manifest.json Reference

Required fields for custom integrations:

```json
{
  "domain": "your_integration",
  "name": "Your Integration",
  "version": "1.0.0",
  "codeowners": ["@your_github_username"],
  "config_flow": true,
  "dependencies": [],
  "documentation": "https://github.com/user/your-integration",
  "integration_type": "device",
  "iot_class": "local_polling",
  "issue_tracker": "https://github.com/user/your-integration/issues",
  "requirements": []
}
```

### integration_type Values
- `device` - Single device
- `hub` - Hub/bridge with multiple devices
- `service` - Cloud service
- `virtual` - No physical device
- `helper` - Utility integration

### iot_class Values
- `local_polling` - Local device, periodically polled
- `local_push` - Local device, pushes updates
- `cloud_polling` - Cloud service, periodically polled
- `cloud_push` - Cloud service, pushes updates
- `calculated` - Derives from other entities
- `assumed_state` - State is assumed, not confirmed

## Common Pitfalls to Avoid

### ❌ Blocking the Event Loop
```python
# WRONG - Blocks entire HA
data = requests.get(url).json()

# CORRECT - Async
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

### ❌ Polling in __init__.py
```python
# WRONG - Manual polling
async def async_setup_entry(hass, entry):
    async def update():
        # Fetch and update...
    async_track_time_interval(hass, update, 30)

# CORRECT - Use DataUpdateCoordinator
async def async_setup_entry(hass, entry):
    coordinator = MyCoordinator(hass, client)
    await coordinator.async_config_entry_first_refresh()
```

### ❌ Missing Unique IDs
```python
# WRONG - Name can change
@property
def unique_id(self) -> str:
    return self._name

# CORRECT - Stable identifier
@property
def unique_id(self) -> str:
    return f"{DOMAIN}_{self._device_id}_{self._sensor_type}"
```

### ❌ Not Handling Unavailability
```python
# WRONG - No availability check
class MySensor(SensorEntity):
    pass

# CORRECT - Proper availability
class MySensor(CoordinatorEntity):
    @property
    def available(self) -> bool:
        return super().available and self._device_id in self.coordinator.data
```

### ❌ YAML Configuration
```python
# WRONG - Don't use YAML for new integrations
async def async_setup_platform(hass, config, async_add_entities):
    # NO! Use config flow instead
```

## Using the HA Integration Agent

This template includes a specialized AI agent for Home Assistant development.

### Invoking the Agent

```python
# In Claude Code
Task(
    subagent_type="ha-integration-agent",
    prompt="Help me create a config flow for OAuth2 authentication",
    description="Create OAuth2 config flow"
)

# Or in chat
@agent ha-integration-agent
I need to create an integration for [device/service]...
```

### Agent Capabilities

The agent can:
- ✅ Generate complete integration structure
- ✅ Create DataUpdateCoordinator implementations
- ✅ Build config flows with all steps
- ✅ Generate entity platform files
- ✅ Write test files with proper mocking
- ✅ Review code against Quality Scale
- ✅ Provide architecture guidance

### When to Use the Agent

1. **Starting a new integration** - Ask for architecture guidance
2. **Implementing patterns** - DataUpdateCoordinator, config flow, entities
3. **Code review** - Check compliance with Quality Scale
4. **Debugging** - Understand errors and issues
5. **Learning** - Understand WHY patterns exist

## Key Resources

### Documentation
- [ha-dev-environment-requirements.md](ha-dev-environment-requirements.md) - Complete environment guide
- [resources/agents/ha-integration-agent/README.md](resources/agents/ha-integration-agent/README.md) - Agent usage guide
- [resources/agents/ha-integration-agent/ha_integration_agent_spec.md](resources/agents/ha-integration-agent/ha_integration_agent_spec.md) - Comprehensive patterns

### Example Code
- [custom_components/example_integration/](custom_components/example_integration/) - Reference implementation
- [tests/](tests/) - Test examples

### Official HA Documentation
- [Home Assistant Developer Docs](https://developers.home-assistant.io/)
- [Integration Quality Scale](https://developers.home-assistant.io/docs/core/integration-quality-scale/)
- [Creating Your First Integration](https://developers.home-assistant.io/docs/creating_component_index/)

## Quick Command Reference

```bash
# Environment
source venv/bin/activate              # Activate venv (ALWAYS FIRST)
python scripts/verify_environment.py  # Verify setup

# Development
ruff check . --fix                    # Lint and auto-fix
ruff format .                         # Format code
mypy custom_components/               # Type check
pytest tests/ -v                      # Run tests
pytest tests/ --cov=custom_components --cov-report=html  # Coverage

# Quality
pre-commit run --all-files            # Run all hooks
pre-commit install                    # Install git hooks

# Git workflow (pre-commit runs automatically on commit)
git add .
git commit -m "message"
```

## Critical Rules

1. **ALWAYS activate venv** before any development work
2. **ALWAYS use DataUpdateCoordinator** for polling integrations
3. **NEVER use YAML configuration** for new integrations
4. **NEVER block the event loop** - use async libraries
5. **ALWAYS add type hints** - modern Python 3.13+ syntax
6. **ALWAYS provide unique_id** for entities
7. **ALWAYS handle errors properly** - UpdateFailed, ConfigEntryAuthFailed
8. **ALWAYS write tests** - minimum Bronze tier requirement
9. **ALWAYS run quality checks** before committing
10. **ALWAYS aim for Bronze tier minimum** - Silver/Gold preferred

## Branch Protection

This template uses:
- **Main branch:** Protected, stable code
- **Testing branch:** Development work (use this for new features)

Check current branch before making changes:
```bash
git branch --show-current
```

## Getting Help

1. **Use the agent:** `@agent ha-integration-agent`
2. **Read the spec:** [ha_integration_agent_spec.md](resources/agents/ha-integration-agent/ha_integration_agent_spec.md)
3. **Check examples:** [example_integration/](custom_components/example_integration/)
4. **Run verification:** `python scripts/verify_environment.py`
5. **Check HA docs:** https://developers.home-assistant.io/

---

**Remember:** This template is designed to help you create production-quality Home Assistant integrations. Follow the patterns, use the tools, leverage the agent, and aim for at least Bronze tier compliance. Happy coding! 🚀
