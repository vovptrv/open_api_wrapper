from services.weather_service import WeatherService
from utils.io import Input, Output
from utils.broadcast_output import print_current, print_forecast


def run_menu(
    service: WeatherService,
    input_handler: Input,
    output_handler: Output,
) -> None:
    while True:
        _print_menu(output_handler)
        user_choice = input_handler.read('Enter option: ').strip()

        if user_choice == '0':
            output_handler.write('Goodbye!')
            break

        city_name = input_handler.read('Enter city: ').strip()

        if not city_name:
            output_handler.write('City cannot be empty')
            continue

        _handle_choice(service, user_choice, city_name, output_handler)


def _print_menu(output: Output) -> None:
    output.write('\nChoose an action:')
    output.write('1 - Get current weather')
    output.write('2 - Get forecast')
    output.write('3 - Get cached data')
    output.write('4 - Delete cached data')
    output.write('0 - Exit')


def _handle_choice(
    service: WeatherService,
    choice: str,
    city: str,
    output: Output,
) -> None:
    if choice == '1':
        payload = service.fetch_current(city)
        print_current(city, payload, output)

    elif choice == '2':
        payload = service.fetch_forecast(city)
        print_forecast(city, payload, output)

    elif choice == '3':
        cached = service.get_cached(f'current:{city}')
        if cached:
            print_current(city, cached, output)
        else:
            output.write('No cached data found')

    elif choice == '4':
        service.delete_cached(f'current:{city}')
        output.write('Cache deleted')

    else:
        output.write('Invalid option')