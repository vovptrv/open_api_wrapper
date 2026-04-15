from typing import Callable, Dict

from services.weather_service import WeatherService
from utils.io import Input, Output
from utils.broadcast_output import print_current, print_forecast


def run_menu(
    service: WeatherService,
    input_handler: Input,
    output_handler: Output,
) -> None:
    actions = _build_actions(service, output_handler)

    while True:
        _print_menu(output_handler)
        user_choice = input_handler.read("Enter option: ").strip()

        if user_choice == "0":
            output_handler.write("Goodbye!")
            break

        city_name = input_handler.read("Enter city: ").strip()

        if not city_name:
            output_handler.write("City cannot be empty")
            continue

        action = actions.get(user_choice)
        if action:
            action(city_name)
        else:
            output_handler.write("Invalid option")


def _build_actions(
    service: WeatherService,
    output: Output,
) -> Dict[str, Callable[[str], None]]:
    return {
        "1": lambda city: _handle_current(service, city, output),
        "2": lambda city: _handle_forecast(service, city, output),
        "3": lambda city: _handle_cached(service, city, output),
        "4": lambda city: _handle_delete(service, city, output),
    }


def _handle_current(
    service: WeatherService,
    city: str,
    output: Output,
) -> None:
    payload = service.fetch_current(city)
    print_current(city, payload, output)


def _handle_forecast(
    service: WeatherService,
    city: str,
    output: Output,
) -> None:
    payload = service.fetch_forecast(city)
    print_forecast(city, payload, output)


def _handle_cached(
    service: WeatherService,
    city: str,
    output: Output,
) -> None:
    cached = service.get_cached(f"current:{city}")
    if cached:
        print_current(city, cached, output)
    else:
        output.write("No cached data found")


def _handle_delete(
    service: WeatherService,
    city: str,
    output: Output,
) -> None:
    service.delete_cached(f"current:{city}")
    output.write("Cache deleted")


def _print_menu(output: Output) -> None:
    output.write("\nChoose an action:")
    output.write("1 - Get current weather")
    output.write("2 - Get forecast")
    output.write("3 - Get cached data")
    output.write("4 - Delete cached data")
    output.write("0 - Exit")
