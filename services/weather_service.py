from typing import Any
from connectors.api_connector import ApiConnector
from storages.storage_interface import Storage
from models.dto import CurrentWeatherResponse, ForecastResponse


class WeatherService:
    """Service layer using abstract connector."""

    def __init__(
        self,
        connector: ApiConnector,
        storage: Storage,
    ) -> None:
        self._connector = connector
        self._storage = storage

    def fetch_current(self, city: str) -> CurrentWeatherResponse:
        payload = self._connector.get("weather", {"q": city})
        weather_data = CurrentWeatherResponse(**payload)
        self._storage.create(f"current:{city}", weather_data)
        return weather_data

    def fetch_forecast(self, city: str) -> ForecastResponse:
        payload = self._connector.get("forecast", {"q": city})
        forecast_data = ForecastResponse(**payload)
        self._storage.create(f"forecast:{city}", forecast_data)
        return forecast_data

    def get_cached(self, key: str) -> Any:
        return self._storage.read(key)

    def delete_cached(self, key: str) -> None:
        self._storage.delete(key)
