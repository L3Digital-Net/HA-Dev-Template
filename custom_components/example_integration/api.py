"""Mock API client for Example Integration.

This is a demonstration API client showing best practices for Home Assistant integrations.
In a real integration, this would communicate with your actual device or service.
"""

from __future__ import annotations

import asyncio
import random
from typing import Any

import aiohttp


class AuthenticationError(Exception):
    """Exception raised for authentication failures."""


class ConnectionError(Exception):
    """Exception raised for connection failures."""


class APIClient:
    """Mock API client for demonstration purposes.

    This client simulates communicating with a device or service.
    Replace this with your actual API implementation.
    """

    def __init__(
        self,
        host: str,
        session: aiohttp.ClientSession,
    ) -> None:
        """Initialize the API client.

        Args:
            host: Device hostname or IP address.
            session: aiohttp client session for making requests.
        """
        self._host = host
        self._session = session
        self._authenticated = False

    async def authenticate(self, api_key: str) -> bool:
        """Authenticate with the device.

        Args:
            api_key: API key for authentication.

        Returns:
            True if authentication successful.

        Raises:
            AuthenticationError: If authentication fails.
            ConnectionError: If device is unreachable.
        """
        # Mock authentication
        # In real implementation, this would call your device's auth endpoint
        await asyncio.sleep(0.1)  # Simulate network delay

        if api_key == "invalid":
            raise AuthenticationError("Invalid API key")

        self._authenticated = True
        return True

    async def fetch_device_data(self) -> dict[str, Any]:
        """Fetch current device data.

        Returns:
            Dictionary containing device state and sensor values.

        Raises:
            AuthenticationError: If not authenticated.
            ConnectionError: If device is unreachable.
        """
        if not self._authenticated:
            raise AuthenticationError("Not authenticated")

        # Mock data fetch
        # In real implementation, this would fetch actual device data
        await asyncio.sleep(0.1)  # Simulate network delay

        # Simulate random device data
        return {
            "device_id": "example_device_001",
            "name": f"Example Device ({self._host})",
            "model": "Example Model v1.0",
            "firmware": "1.2.3",
            "online": True,
            "sensors": {
                "temperature": round(20 + random.uniform(-5, 5), 1),
                "humidity": round(50 + random.uniform(-10, 10), 1),
                "battery": random.randint(80, 100),
            },
            "timestamp": "2026-02-07T12:00:00Z",
        }

    async def set_device_state(self, state: bool) -> bool:
        """Set device on/off state.

        Args:
            state: True for on, False for off.

        Returns:
            True if state change successful.

        Raises:
            AuthenticationError: If not authenticated.
            ConnectionError: If device is unreachable.
        """
        if not self._authenticated:
            raise AuthenticationError("Not authenticated")

        # Mock state change
        await asyncio.sleep(0.1)  # Simulate network delay
        return True

    async def close(self) -> None:
        """Close the API client and clean up resources."""
        # In real implementation, close any open connections
        self._authenticated = False
