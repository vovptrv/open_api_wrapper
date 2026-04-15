from connectors.weather_api_connector import WeatherApiConnector
from services.weather_service import WeatherService
from storages.in_memory_storage import InMemoryStorage
from config.config import settings
from utils.io import ConsoleInput, ConsoleOutput
from utils.menu import run_menu


def main() -> None:
    connector = WeatherApiConnector(settings.weather_api_key)
    storage = InMemoryStorage()
    service = WeatherService(connector, storage)

    input_handler = ConsoleInput()
    output_handler = ConsoleOutput()

    run_menu(service, input_handler, output_handler)


if __name__ == "__main__":
    main()
