import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> dict:
    """Get current weather from OpenWeather."""

    if not API_KEY:
        return {
            "success": False,
            "error": "OPENWEATHER_API_KEY is not configured."
        }

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.RequestException:
        return {
            "success": False,
            "error": "Weather service is temporarily unavailable."
        }

    if response.status_code == 404:
        return {
            "success": False,
            "error": f"Could not find weather for '{city}'."
        }

    if response.status_code != 200:
        return {
            "success": False,
            "error": "Weather API returned an error."
        }

    data = response.json()

    return {
        "success": True,
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
    }
