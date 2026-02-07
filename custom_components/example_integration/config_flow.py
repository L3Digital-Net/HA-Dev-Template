"""Config flow for Example Integration."""

from __future__ import annotations

from typing import Any

import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.config_entries import ConfigFlowResult
from homeassistant.const import CONF_API_KEY, CONF_HOST

from .api import APIClient, AuthenticationError
from .api import ConnectionError as APIConnectionError
from .const import DOMAIN

# Default host for demonstration
DEFAULT_HOST = "192.168.1.100"


class CannotConnect(Exception):
    """Error to indicate we cannot connect."""


class InvalidAuth(Exception):
    """Error to indicate invalid authentication."""


class ExampleIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Example Integration."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step.

        This is called when the user initiates setup from the UI.
        """
        errors: dict[str, str] = {}

        if user_input is not None:
            # User submitted the form
            try:
                # Validate the input by attempting to connect
                info = await self._async_validate_input(user_input)

            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except Exception:  # noqa: BLE001
                errors["base"] = "unknown"

            else:
                # Validation successful - create the config entry
                await self.async_set_unique_id(info["device_id"])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )

        # Show the form (first time or if there were errors)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
                    vol.Required(CONF_API_KEY): str,
                }
            ),
            errors=errors,
        )

    async def _async_validate_input(self, user_input: dict[str, Any]) -> dict[str, str]:
        """Validate user input by attempting to connect to the device.

        Args:
            user_input: Dictionary containing user-provided host and API key.

        Returns:
            Dictionary with "title" and "device_id" for the config entry.

        Raises:
            CannotConnect: If connection to device fails.
            InvalidAuth: If authentication fails.
        """
        host = user_input[CONF_HOST]
        api_key = user_input[CONF_API_KEY]

        # Create API client
        session = aiohttp.ClientSession()
        try:
            api_client = APIClient(host, session)

            # Attempt authentication
            try:
                await api_client.authenticate(api_key)
            except AuthenticationError as err:
                raise InvalidAuth from err
            except APIConnectionError as err:
                raise CannotConnect from err

            # Fetch device info to get device ID and name
            try:
                data = await api_client.fetch_device_data()
            except APIConnectionError as err:
                raise CannotConnect from err

            device_id = data.get("device_id", "unknown")
            device_name = data.get("name", f"Device at {host}")

            return {
                "title": device_name,
                "device_id": device_id,
            }

        finally:
            await session.close()
