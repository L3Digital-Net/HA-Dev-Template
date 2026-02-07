"""Base entity for Example Integration."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import ExampleIntegrationCoordinator


class ExampleIntegrationEntity(CoordinatorEntity[ExampleIntegrationCoordinator]):
    """Base entity for Example Integration.

    All entity platforms (sensor, binary_sensor, etc.) should inherit from this class.
    It provides common functionality like device registry integration and availability.
    """

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: ExampleIntegrationCoordinator,
        device_id: str,
        entity_type: str,
    ) -> None:
        """Initialize the entity.

        Args:
            coordinator: The data update coordinator.
            device_id: Unique identifier for the device.
            entity_type: Type of entity (e.g., "temperature", "humidity").
        """
        super().__init__(coordinator)
        self._device_id = device_id
        self._entity_type = entity_type

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information for device registry.

        This groups all entities from the same device together in the UI.
        """
        data = self.coordinator.data
        return DeviceInfo(
            identifiers={(DOMAIN, self._device_id)},
            name=data.get("name", "Example Device"),
            manufacturer="Example Manufacturer",
            model=data.get("model", "Unknown Model"),
            sw_version=data.get("firmware", "Unknown"),
        )

    @property
    def unique_id(self) -> str:
        """Return unique ID for this entity.

        The unique ID should be stable across restarts and never change.
        Format: domain_deviceid_entitytype
        """
        return f"{DOMAIN}_{self._device_id}_{self._entity_type}"

    @property
    def available(self) -> bool:
        """Return True if entity is available.

        Entity is available if:
        1. Coordinator has valid data (super().available)
        2. Device is marked as online in the data

        This prevents showing stale data when device is offline.
        """
        return super().available and self.coordinator.data.get("online", False)
