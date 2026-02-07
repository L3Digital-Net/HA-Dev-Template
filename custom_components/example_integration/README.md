# Example Integration

This is a template integration structure that demonstrates the required files and patterns for a Home Assistant integration.

## Files

- `manifest.json` - Integration metadata
- `__init__.py` - Entry point for the integration
- `const.py` - Constants and configuration defaults
- `strings.json` - User-facing strings for config flow
- `README.md` - This file

## TODO: Implement

- [ ] Config flow (`config_flow.py`)
- [ ] Data update coordinator (`coordinator.py`)
- [ ] Sensor platform (`sensor.py`)
- [ ] Tests (`../../../tests/`)

## Development

This template follows the Home Assistant integration development best practices:
- Python 3.13+ compatibility
- Async-first architecture
- DataUpdateCoordinator pattern
- Config flow for UI setup
- Type hints throughout

Refer to `/ha-dev-environment-requirements.md` for full development environment setup.
