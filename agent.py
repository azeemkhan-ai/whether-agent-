from weather_service import get_weather


def weather_agent(city: str) -> str:
    """Turn weather API data into a human-friendly response."""

    weather = get_weather(city)

    if not weather["success"]:
        return f"❌ {weather['error']}"

    temp = weather["temperature"]
    feels_like = weather["feels_like"]
    humidity = weather["humidity"]
    pressure = weather["pressure"]
    wind = weather["wind_speed"]
    description = weather["description"].capitalize()

    advice = []

    if temp >= 35:
        advice.append("It's very hot, so stay hydrated.")
    elif temp <= 10:
        advice.append("It's quite cold, so consider warm clothing.")

    if humidity >= 80:
        advice.append("Humidity is high.")

    if wind >= 10:
        advice.append("It is fairly windy.")

    if not advice:
        advice.append("Weather conditions look fairly comfortable.")

    return (
        f"🌤️ Weather for {weather['city']}, {weather['country']}\n\n"
        f"🌡️ Temperature: {temp}°C\n"
        f"🤔 Feels like: {feels_like}°C\n"
        f"☁️ Conditions: {description}\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind: {wind} m/s\n"
        f"🔽 Pressure: {pressure} hPa\n\n"
        f"💡 Advice:\n{chr(10).join('• ' + item for item in advice)}"
    )
