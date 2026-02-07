"""Sensor platform for Example Integration."""

from __future__ import annotations

from typing import cast

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import ExampleIntegrationCoordinator
from .entity import ExampleIntegrationEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Example Integration sensors from a config entry.

    Args:
        hass: Home Assistant instance.
        entry: Config entry for this integration.
        async_add_entities: Callback to add sensor entities.
    """
    coordinator: ExampleIntegrationCoordinator = hass.data[DOMAIN][entry.entry_id]

    # Get device ID from coordinator data
    device_id = coordinator.data.get("device_id", "unknown")

    # Create sensor entities
    entities = [
        ExampleTemperatureSensor(coordinator, device_id),
        ExampleHumiditySensor(coordinator, device_id),
        ExampleBatterySensor(coordinator, device_id),
    ]

    async_add_entities(entities)


class ExampleTemperatureSensor(ExampleIntegrationEntity, SensorEntity):
    """Temperature sensor for Example Integration."""

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_suggested_display_precision = 1

    def __init__(
        self,
        coordinator: ExampleIntegrationCoordinator,
        device_id: str,
    ) -> None:
        """Initialize the temperature sensor."""
        super().__init__(coordinator, device_id, "temperature")
        self._attr_name = "Temperature"

    @property
    def native_value(self) -> float | None:
        """Return the temperature value."""
        sensors = self.coordinator.data.get("sensors", {})
        value = sensors.get("temperature")
        return cast(float, value) if value is not None else None


class ExampleHumiditySensor(ExampleIntegrationEntity, SensorEntity):
    """Humidity sensor for Example Integration."""

    _attr_device_class = SensorDeviceClass.HUMIDITY
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_suggested_display_precision = 1

    def __init__(
        self,
        coordinator: ExampleIntegrationCoordinator,
        device_id: str,
    ) -> None:
        """Initialize the humidity sensor."""
        super().__init__(coordinator, device_id, "humidity")
        self._attr_name = "Humidity"

    @property
    def native_value(self) -> float | None:
        """Return the humidity value."""
        sensors = self.coordinator.data.get("sensors", {})
        value = sensors.get("humidity")
        return cast(float, value) if value is not None else None


class ExampleBatterySensor(ExampleIntegrationEntity, SensorEntity):
    """Battery sensor for Example Integration."""

    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = PERCENTAGE

    def __init__(
        self,
        coordinator: ExampleIntegrationCoordinator,
        device_id: str,
    ) -> None:
        """Initialize the battery sensor."""
        super().__init__(coordinator, device_id, "battery")
        self._attr_name = "Battery"

    @property
    def native_value(self) -> int | None:
        """Return the battery level."""
        sensors = self.coordinator.data.get("sensors", {})
        value = sensors.get("battery")
        return cast(int, value) if value is not None else None
