from typing import Any, Dict

import requests

from connectors.api_connector import ApiConnector


class WeatherApiConnector(ApiConnector):
    """Connector for weather API."""

    _base_url = "https://api.openweathermap.org/data/2.5"

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def get(
        self,
        endpoint: str,
        query_params: Dict[str, Any],
    ) -> Dict[str, Any]:
        query = {**query_params, "appid": self._api_key}

        response = requests.get(
            f"{self._base_url}/{endpoint}",
            params=query,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def post(
        self,
        endpoint: str,
        query_params: Dict[str, Any],
    ) -> Dict[str, Any]: ...
