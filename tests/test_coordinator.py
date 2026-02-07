"""Test the Example Integration coordinator."""

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import UpdateFailed

from custom_components.example_integration.api import (
    AuthenticationError,
)
from custom_components.example_integration.api import (
    ConnectionError as APIConnectionError,
)
from custom_components.example_integration.coordinator import (
    ExampleIntegrationCoordinator,
)


async def test_coordinator_update_success(hass):
    """Test successful coordinator update."""
    # Create mock API client
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(
        return_value={
            "device_id": "test_device",
            "name": "Test Device",
            "online": True,
            "sensors": {
                "temperature": 22.5,
                "humidity": 55.0,
                "battery": 95,
            },
        }
    )

    # Create coordinator
    coordinator = ExampleIntegrationCoordinator(hass, mock_api)

    # Perform update
    await coordinator.async_refresh()

    # Verify data was fetched
    assert coordinator.data["device_id"] == "test_device"
    assert coordinator.data["sensors"]["temperature"] == 22.5
    mock_api.fetch_device_data.assert_called_once()


async def test_coordinator_authentication_error(hass):
    """Test coordinator handles authentication errors."""
    # Create mock API client that raises AuthenticationError
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(
        side_effect=AuthenticationError("Invalid credentials")
    )

    # Create coordinator
    coordinator = ExampleIntegrationCoordinator(hass, mock_api)

    # Update should raise ConfigEntryAuthFailed
    with pytest.raises(ConfigEntryAuthFailed):
        await coordinator.async_refresh()


async def test_coordinator_connection_error(hass):
    """Test coordinator handles connection errors."""
    # Create mock API client that raises ConnectionError
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(
        side_effect=APIConnectionError("Device unreachable")
    )

    # Create coordinator
    coordinator = ExampleIntegrationCoordinator(hass, mock_api)

    # Update should raise UpdateFailed
    with pytest.raises(UpdateFailed):
        await coordinator.async_refresh()


async def test_coordinator_unexpected_error(hass):
    """Test coordinator handles unexpected errors."""
    # Create mock API client that raises unexpected exception
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(side_effect=Exception("Unexpected error"))

    # Create coordinator
    coordinator = ExampleIntegrationCoordinator(hass, mock_api)

    # Update should raise UpdateFailed
    with pytest.raises(UpdateFailed):
        await coordinator.async_refresh()


async def test_coordinator_update_interval(hass):
    """Test coordinator has correct update interval."""
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(return_value={})

    coordinator = ExampleIntegrationCoordinator(hass, mock_api)

    # Verify update interval is 30 seconds
    assert coordinator.update_interval.total_seconds() == 30
