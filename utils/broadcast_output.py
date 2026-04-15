from typing import Dict, Any, List
from utils.io import Output


def print_current(
    city: str,
    payload: Dict[str, Any],
    output: Output,
) -> None:
    temperature = payload['main']['temp']
    clouds = payload['clouds']['all']
    rain_amount = payload.get('rain', {}).get('1h', 0)

    output.write(f'\nCurrent weather in {city}:')
    output.write(f'Temperature: {temperature}')
    output.write(f'Cloudiness: {clouds}%')
    output.write(f'Rain (1h): {rain_amount}')


def print_forecast(
    city: str,
    payload: Dict[str, Any],
    output: Output,
) -> None:
    forecast_entries: List[Dict[str, Any]] = payload.get('list', [])[:5]

    output.write(f'\nForecast for {city}:')

    for forecast_entry in forecast_entries:
        timestamp = forecast_entry['dt_txt']
        temperature = forecast_entry['main']['temp']
        clouds = forecast_entry['clouds']['all']
        rain_probability = forecast_entry.get('pop', 0) * 100

        output.write('---')
        output.write(f'Time: {timestamp}')
        output.write(f'Temperature: {temperature}')
        output.write(f'Cloudiness: {clouds}%')
        output.write(f'Rain probability: {rain_probability:.0f}%')