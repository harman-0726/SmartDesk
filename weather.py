import requests
from apis import OPENWEATHER_API_KEY

def get_weather(city, speak):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"]
            weather_report = (f"Weather in {city}: "
                              f"{description.capitalize()}, "
                              f"{temperature}°C, "
                              f"Humidity {humidity}%, "
                              f"Wind {wind_speed} km/h.")
            speak(weather_report)
        else:
            speak("Sorry, I couldn't find that city.")
    except Exception as e:
        print(f"Weather error: {e}")
        speak("Sorry, I couldn't fetch the weather information.")
