import os
import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    """Класс для работы с API OpenWeatherMap"""
    def __init__(self):
        self.api_key = os.getenv('OPEN_WEATHER_MAP_API_KEY')
        self.base_url = os.getenv('OPEN_WEATHER_MAP_API_URL')

    def get_weather(self, lat, lon):
        """Запрашивает данные о погоде по координатам"""
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric",
            "lang": "ru"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка запроса: {response.status_code}")
            return None


class WeatherParser:
    """Класс для обработки данных о погоде"""
    @staticmethod
    def parse(data):
        """Извлекает и форматирует данные из ответа API"""
        if not data:
            return None

        main = data.get("main", {})
        wind = data.get("wind", {})
        sys = data.get("sys", {})
        visibility = data.get("visibility", "Нет данных")
        description = data["weather"][0]["description"].capitalize()

        sunrise = datetime.datetime.fromtimestamp(sys.get("sunrise", 0))
        sunset = datetime.datetime.fromtimestamp(sys.get("sunset", 0))

        return {
            "Описание": description,
            "Температура": f"{main.get('temp', 'Нет данных')}°C",
            "Давление": f"{main.get('pressure', 'Нет данных')} hPa",
            "Влажность": f"{main.get('humidity', 'Нет данных')}%",
            "Ветер": f"{wind.get('speed', 'Нет данных')} м/с, направление: {wind.get('deg', 'Нет данных')}°",
            "Видимость": f"{visibility} м",
            "Восход солнца": sunrise.strftime('%H:%M:%S'),
            "Закат солнца": sunset.strftime('%H:%M:%S')
        }

