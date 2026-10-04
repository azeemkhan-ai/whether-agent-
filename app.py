from fastapi import FastAPI, Request
from fastapi.responses import Response
from twilio.twiml.messaging_response import MessagingResponse

from agent import weather_agent

app = FastAPI(
    title="WeatherAgent-WhatsApp",
    description="AI-ready weather agent with OpenWeather and WhatsApp support",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "status": "online",
        "service": "WeatherAgent-WhatsApp",
        "message": "Weather agent is running."
    }


@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    form = await request.form()
    message = str(form.get("Body", "")).strip()

    if not message:
        reply = (
            "🌦️ Weather Agent\n\n"
            "Try:\n"
            "Weather Islamabad\n"
            "Weather Lahore\n"
            "Weather Melbourne"
        )
    elif message.lower().startswith("weather"):
        city = message[7:].strip()

        if not city:
            reply = "Please provide a city. Example: Weather Islamabad"
        else:
            reply = weather_agent(city)
    else:
        reply = (
            "🌦️ I'm your Weather Agent.\n\n"
            "Send: Weather <city>\n\n"
            "Example: Weather Islamabad"
        )

    response = MessagingResponse()
    response.message(reply)

    return Response(
        content=str(response),
        media_type="application/xml"
    )
