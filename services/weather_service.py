from typing import Any, Dict

from connectors.api_connector import ApiConnector
from storages.in_memory_storage import InMemoryStorage


class WeatherService:
    """Service layer using abstract connector."""

    def __init__(
        self,
        connector: ApiConnector,
        storage: InMemoryStorage,
    ) -> None:
        self._connector = connector
        self._storage = storage

    def fetch_current(self, city: str) -> Dict[str, Any]:
        payload = self._connector.get("weather", {"q": city})
        self._storage.create(f"current:{city}", payload)
        return payload

    def fetch_forecast(self, city: str) -> Dict[str, Any]:
        payload = self._connector.get("forecast", {"q": city})
        self._storage.create(f"forecast:{city}", payload)
        return payload

    def get_cached(self, key: str) -> Any:
        return self._storage.read(key)

    def delete_cached(self, key: str) -> None:
        self._storage.delete(key)
