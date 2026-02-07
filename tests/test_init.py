"""Test the Example Integration init module."""

from homeassistant.const import Platform

from custom_components.example_integration import (
    PLATFORMS,
    async_setup_entry,
    async_unload_entry,
)


async def test_async_setup_entry_not_implemented() -> None:
    """Test that async_setup_entry is implemented."""
    # This test ensures the integration can be imported without errors
    assert async_setup_entry is not None
    assert callable(async_setup_entry)


async def test_async_unload_entry_not_implemented() -> None:
    """Test that async_unload_entry is implemented."""
    # This test ensures the unload function exists
    assert async_unload_entry is not None
    assert callable(async_unload_entry)


async def test_platforms_defined() -> None:
    """Test that platforms are properly defined."""
    assert PLATFORMS is not None
    assert isinstance(PLATFORMS, list)
    assert Platform.SENSOR in PLATFORMS
