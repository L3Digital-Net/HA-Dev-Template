"""Test the Example Integration config flow."""

from unittest.mock import patch

from homeassistant import config_entries, data_entry_flow
from homeassistant.const import CONF_API_KEY, CONF_HOST
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.example_integration.config_flow import (
    CannotConnect,
    InvalidAuth,
)
from custom_components.example_integration.const import DOMAIN


async def test_form_user(hass):
    """Test we get the form for user step."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )

    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["step_id"] == "user"
    assert result["errors"] == {}


async def test_form_user_success(hass):
    """Test successful user config flow."""
    with (
        patch(
            "custom_components.example_integration.config_flow.APIClient.authenticate",
            return_value=True,
        ),
        patch(
            "custom_components.example_integration.config_flow.APIClient.fetch_device_data",
            return_value={
                "device_id": "test_device_123",
                "name": "Test Device",
            },
        ),
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            user_input={
                CONF_HOST: "192.168.1.100",
                CONF_API_KEY: "test_api_key",
            },
        )

        assert result["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
        assert result["title"] == "Test Device"
        assert result["data"] == {
            CONF_HOST: "192.168.1.100",
            CONF_API_KEY: "test_api_key",
        }


async def test_form_cannot_connect(hass):
    """Test we handle cannot connect error."""
    with patch(
        "custom_components.example_integration.config_flow.APIClient.authenticate",
        side_effect=CannotConnect,
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            user_input={
                CONF_HOST: "192.168.1.100",
                CONF_API_KEY: "test_api_key",
            },
        )

        assert result["type"] == data_entry_flow.FlowResultType.FORM
        assert result["errors"] == {"base": "cannot_connect"}


async def test_form_invalid_auth(hass):
    """Test we handle invalid authentication."""
    with patch(
        "custom_components.example_integration.config_flow.APIClient.authenticate",
        side_effect=InvalidAuth,
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            user_input={
                CONF_HOST: "192.168.1.100",
                CONF_API_KEY: "invalid_key",
            },
        )

        assert result["type"] == data_entry_flow.FlowResultType.FORM
        assert result["errors"] == {"base": "invalid_auth"}


async def test_form_unknown_error(hass):
    """Test we handle unknown errors."""
    with patch(
        "custom_components.example_integration.config_flow.APIClient.authenticate",
        side_effect=Exception("Unexpected error"),
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            user_input={
                CONF_HOST: "192.168.1.100",
                CONF_API_KEY: "test_api_key",
            },
        )

        assert result["type"] == data_entry_flow.FlowResultType.FORM
        assert result["errors"] == {"base": "unknown"}


async def test_form_already_configured(hass):
    """Test we handle already configured devices."""
    # Create a mock config entry
    config_entry = MockConfigEntry(
        domain=DOMAIN,
        title="Test Device",
        data={
            CONF_HOST: "192.168.1.100",
            CONF_API_KEY: "test_api_key",
        },
        unique_id="test_device_123",
    )
    config_entry.add_to_hass(hass)

    with (
        patch(
            "custom_components.example_integration.config_flow.APIClient.authenticate",
            return_value=True,
        ),
        patch(
            "custom_components.example_integration.config_flow.APIClient.fetch_device_data",
            return_value={
                "device_id": "test_device_123",  # Same device ID
                "name": "Test Device",
            },
        ),
    ):
        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            user_input={
                CONF_HOST: "192.168.1.100",
                CONF_API_KEY: "test_api_key",
            },
        )

        assert result["type"] == data_entry_flow.FlowResultType.ABORT
        assert result["reason"] == "already_configured"
