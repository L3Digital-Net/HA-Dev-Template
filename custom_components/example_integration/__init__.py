"""The Example Integration integration."""

from __future__ import annotations

import logging

import aiohttp
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, CONF_HOST, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import APIClient
from .const import DOMAIN
from .coordinator import ExampleIntegrationCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Example Integration from a config entry.

    Args:
        hass: Home Assistant instance.
        entry: Config entry for this integration.

    Returns:
        True if setup was successful.
    """
    # Get configuration from config entry
    host = entry.data[CONF_HOST]
    api_key = entry.data[CONF_API_KEY]

    # Create API client with shared aiohttp session
    session = async_get_clientsession(hass)
    api_client = APIClient(host, session)

    # Authenticate with device
    try:
        await api_client.authenticate(api_key)
    except Exception as err:
        _LOGGER.error("Failed to authenticate with device: %s", err)
        return False

    # Create data update coordinator
    coordinator = ExampleIntegrationCoordinator(hass, api_client)

    # Fetch initial data
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator in hass.data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Forward setup to platforms
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry.

    Args:
        hass: Home Assistant instance.
        entry: Config entry to unload.

    Returns:
        True if unload was successful.
    """
    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    # Clean up coordinator and API client
    if unload_ok:
        coordinator: ExampleIntegrationCoordinator = hass.data[DOMAIN].pop(
            entry.entry_id
        )
        await coordinator.api_client.close()

    return unload_ok
