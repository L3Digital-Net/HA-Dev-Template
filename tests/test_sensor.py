"""Test the Example Integration sensor platform."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from custom_components.example_integration.const import DOMAIN
from custom_components.example_integration.coordinator import (
    ExampleIntegrationCoordinator,
)
from custom_components.example_integration.sensor import (
    ExampleBatterySensor,
    ExampleHumiditySensor,
    ExampleTemperatureSensor,
)


@pytest.fixture
def mock_coordinator(hass):
    """Create a mock coordinator with test data."""
    mock_api = MagicMock()
    mock_api.fetch_device_data = AsyncMock(
        return_value={
            "device_id": "test_device",
            "name": "Test Device",
            "model": "Test Model",
            "firmware": "1.0.0",
            "online": True,
            "sensors": {
                "temperature": 22.5,
                "humidity": 55.0,
                "battery": 95,
            },
        }
    )

    coordinator = ExampleIntegrationCoordinator(hass, mock_api)
    coordinator.data = mock_api.fetch_device_data.return_value

    return coordinator


async def test_temperature_sensor(hass, mock_coordinator):
    """Test temperature sensor."""
    sensor = ExampleTemperatureSensor(mock_coordinator, "test_device")

    # Test properties
    assert sensor.name == "Temperature"
    assert sensor.unique_id == "example_integration_test_device_temperature"
    assert sensor.native_value == 22.5
    assert sensor.device_class == "temperature"
    assert sensor.state_class == "measurement"
    assert sensor.native_unit_of_measurement == "°C"


async def test_humidity_sensor(hass, mock_coordinator):
    """Test humidity sensor."""
    sensor = ExampleHumiditySensor(mock_coordinator, "test_device")

    # Test properties
    assert sensor.name == "Humidity"
    assert sensor.unique_id == "example_integration_test_device_humidity"
    assert sensor.native_value == 55.0
    assert sensor.device_class == "humidity"
    assert sensor.state_class == "measurement"
    assert sensor.native_unit_of_measurement == "%"


async def test_battery_sensor(hass, mock_coordinator):
    """Test battery sensor."""
    sensor = ExampleBatterySensor(mock_coordinator, "test_device")

    # Test properties
    assert sensor.name == "Battery"
    assert sensor.unique_id == "example_integration_test_device_battery"
    assert sensor.native_value == 95
    assert sensor.device_class == "battery"
    assert sensor.state_class == "measurement"
    assert sensor.native_unit_of_measurement == "%"


async def test_sensor_availability(hass, mock_coordinator):
    """Test sensor availability based on device online status."""
    sensor = ExampleTemperatureSensor(mock_coordinator, "test_device")

    # Device online - sensor available
    assert sensor.available is True

    # Device offline - sensor unavailable
    mock_coordinator.data["online"] = False
    assert sensor.available is False


async def test_sensor_device_info(hass, mock_coordinator):
    """Test sensor device info."""
    sensor = ExampleTemperatureSensor(mock_coordinator, "test_device")

    device_info = sensor.device_info

    assert device_info["identifiers"] == {(DOMAIN, "test_device")}
    assert device_info["name"] == "Test Device"
    assert device_info["manufacturer"] == "Example Manufacturer"
    assert device_info["model"] == "Test Model"
    assert device_info["sw_version"] == "1.0.0"


async def test_sensor_missing_data(hass, mock_coordinator):
    """Test sensor handles missing data gracefully."""
    # Remove sensor data
    mock_coordinator.data = {
        "device_id": "test_device",
        "name": "Test Device",
        "online": True,
        "sensors": {},  # No sensor values
    }

    sensor = ExampleTemperatureSensor(mock_coordinator, "test_device")

    # Should return None for missing data
    assert sensor.native_value is None
