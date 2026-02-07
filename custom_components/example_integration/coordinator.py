"""DataUpdateCoordinator for Example Integration."""

from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import APIClient, AuthenticationError
from .api import ConnectionError as APIConnectionError
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class ExampleIntegrationCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator to manage data fetching for Example Integration.

    This coordinator centralizes data fetching for all entities,
    ensuring efficient polling and proper error handling.
    """

    def __init__(
        self,
        hass: HomeAssistant,
        api_client: APIClient,
    ) -> None:
        """Initialize the coordinator.

        Args:
            hass: Home Assistant instance.
            api_client: API client for communicating with the device.
        """
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
            always_update=False,  # Only update entities when data changes
        )
        self.api_client = api_client

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the device.

        This method is called automatically by the coordinator according to
        the update_interval. It should return the data for all entities.

        Returns:
            Dictionary containing device data and sensor values.

        Raises:
            ConfigEntryAuthFailed: If authentication fails (triggers reauth flow).
            UpdateFailed: If device is unreachable or returns invalid data.
        """
        try:
            # Fetch data from device
            data = await self.api_client.fetch_device_data()

            _LOGGER.debug(
                "Successfully fetched data for device %s",
                data.get("device_id", "unknown"),
            )

            return data

        except AuthenticationError as err:
            # Authentication failed - trigger reauth flow
            _LOGGER.error("Authentication failed: %s", err)
            raise ConfigEntryAuthFailed("Invalid credentials") from err

        except APIConnectionError as err:
            # Device unreachable - entities will show as unavailable
            _LOGGER.warning("Connection error: %s", err)
            raise UpdateFailed(f"Error communicating with device: {err}") from err

        except Exception as err:
            # Unexpected error
            _LOGGER.exception("Unexpected error fetching data: %s", err)
            raise UpdateFailed(f"Unexpected error: {err}") from err
