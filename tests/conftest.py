"""Fixtures for Example Integration tests."""

from __future__ import annotations

from collections.abc import Generator
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.const import CONF_HOST, CONF_NAME

MOCK_CONFIG = {
    CONF_HOST: "192.168.1.100",
    CONF_NAME: "Test Device",
}


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock]:
    """Mock setting up a config entry."""
    with patch(
        "custom_components.example_integration.async_setup_entry",
        return_value=True,
    ) as mock_setup:
        yield mock_setup
