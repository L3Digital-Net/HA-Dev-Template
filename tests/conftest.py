"""Fixtures for Example Integration tests."""

from __future__ import annotations

import sys
from collections.abc import Generator
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
from homeassistant.const import CONF_HOST, CONF_NAME

# Add custom_components to Python path
custom_components_path = Path(__file__).parent.parent / "custom_components"
if str(custom_components_path) not in sys.path:
    sys.path.insert(0, str(custom_components_path.parent))


# This fixture enables loading custom integrations in all tests.
# Remove it to enable selective automatic fixture registration.
@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations for all tests."""
    yield


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
