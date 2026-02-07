# Tests

This directory contains tests for the Example Integration.

## Structure

- `conftest.py` - Shared fixtures and mocks
- `test_*.py` - Test modules (to be implemented)

## Required Tests (Bronze Tier)

- [ ] `test_config_flow.py` - Config flow tests
  - [ ] User flow success
  - [ ] Connection error handling
  - [ ] Authentication error handling
  - [ ] Duplicate prevention

- [ ] `test_init.py` - Setup/unload tests
  - [ ] Successful setup
  - [ ] Setup failure handling
  - [ ] Unload entry

## Running Tests

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=custom_components.example_integration --cov-report=html

# Run specific test file
pytest tests/test_config_flow.py -v
```

## Test Requirements

- All I/O operations must be mocked
- Tests must not require a running Home Assistant instance
- Use `AsyncMock` for async operations
- Use the `hass` fixture provided by pytest-homeassistant-custom-component
