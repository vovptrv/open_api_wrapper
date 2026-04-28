from pydantic import BaseModel
from typing import Optional, List


class MainWeatherData(BaseModel):
    """Main weather parameters."""

    temperature: float
    feels_like: Optional[float] = None
    temp_min: Optional[float] = None
    temp_max: Optional[float] = None
    pressure: Optional[int] = None
    humidity: Optional[int] = None


class CloudsData(BaseModel):
    """Cloud coverage information."""

    all: int  # cloudiness percentage


class RainData(BaseModel):
    """Precipitation data."""

    one_h: Optional[float] = None  # rain volume for 1 hour
    three_h: Optional[float] = None  # rain volume for 3 hours

    class Config:
        populate_by_name = True
        fields = {"one_h": {"alias": "1h"}, "three_h": {"alias": "3h"}}


class CurrentWeatherResponse(BaseModel):
    """OpenWeatherMap current weather API response."""

    main: MainWeatherData
    clouds: CloudsData
    rain: Optional[RainData] = None


class ForecastEntry(BaseModel):
    """Single forecast entry."""

    dt_txt: str  # forecast time
    main: MainWeatherData
    clouds: CloudsData
    prob_of_precipitation: Optional[float] = None  # probability of precipitation


class ForecastResponse(BaseModel):
    """OpenWeatherMap forecast API response."""

    list: List[ForecastEntry]
