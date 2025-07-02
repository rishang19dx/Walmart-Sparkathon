from fastapi import APIRouter, HTTPException, Query
import requests

router = APIRouter()

@router.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    # Step 1: Get lat/lon from city name
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        raise HTTPException(status_code=404, detail="City not found")

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Step 2: Get weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_res = requests.get(weather_url).json()

    if "current_weather" not in weather_res:
        raise HTTPException(status_code=500, detail="Weather data not available")

    temp = weather_res["current_weather"]["temperature"]
    wind = weather_res["current_weather"]["windspeed"]
    weather_code = weather_res["current_weather"]["weathercode"]

    return {
        "city": city,
        "temperature_celsius": temp,
        "wind_speed_kph": wind,
        "weather_code": weather_code
    }
