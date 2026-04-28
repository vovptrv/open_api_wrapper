from utils.io import Output
from models.dto import CurrentWeatherResponse, ForecastResponse, ForecastEntry


def print_current(
    city: str,
    payload: CurrentWeatherResponse,
    output: Output,
) -> None:
    temperature = payload.main.temperature
    clouds = payload.clouds.all
    rain_amount = payload.rain.one_h if payload.rain else 0

    output.write(f"\nCurrent weather in {city}:")
    output.write(f"Temperature: {temperature}")
    output.write(f"Cloudiness: {clouds}%")
    output.write(f"Rain (1h): {rain_amount}")


def print_forecast(
    city: str,
    payload: ForecastResponse,
    output: Output,
) -> None:
    forecast_entries: list[ForecastEntry] = payload.list[:5]

    output.write(f"\nForecast for {city}:")

    for forecast_entry in forecast_entries:
        _print_forecast_entry(forecast_entry, output)


def _print_forecast_entry(
    forecast_entry: ForecastEntry,
    output: Output,
) -> None:
    temperature = forecast_entry.main.temperature
    cloudiness = forecast_entry.clouds.all
    rain_probability = (forecast_entry.prob_of_precipitation or 0) * 100
    output.write("---")
    output.write(f"Time: {forecast_entry.dt_txt}")
    output.write(f"Temperature: {temperature}")
    output.write(f"Cloudiness: {cloudiness}%")
    output.write(f"Rain probability: {rain_probability:.0f}%")
