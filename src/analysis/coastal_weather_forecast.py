from src.__utils.weather_utils import WeatherAPI, WeatherParser


class CoastalWeatherForecast:
    """Класс для интеграции прогноза погоды в анализ прибрежных систем"""
    def __init__(self, locations):
        self.locations = locations
        self.api = WeatherAPI()

    def get_forecasts(self):
        """Получает и возвращает погоду для всех локаций"""
        forecasts = {}  # Здесь будем хранить прогнозы для всех локаций
        for name, (lat, lon) in self.locations.items():
            data = self.api.get_weather(lat, lon)
            parsed_data = WeatherParser.parse(data)
            if parsed_data:
                forecasts[name] = parsed_data  # Добавляем данные в прогноз
        return forecasts  # Возвращаем все прогнозы в виде словаря

    def analyze_coastal_conditions(self):
        """Добавляет анализ условий для прибрежных операций"""
        for name, (lat, lon) in self.locations.items():
            data = self.api.get_weather(lat, lon)
            parsed_data = WeatherParser.parse(data)
            if parsed_data:
                print(f"\nАнализ обстановки в регионе: {name}")
                self._evaluate_safety(parsed_data)

    def _evaluate_safety(self, weather_data):
        """Оценка безопасности для прибрежных операций"""
        wind_speed = float(weather_data["Ветер"].split()[0])
        visibility = int(weather_data["Видимость"].split()[0])

        if wind_speed > 15:
            print("⚠️ Внимание: сильный ветер, возможны высокие волны!")
        if visibility < 1000:
            print("⚠️ Внимание: низкая видимость, сложные условия для навигации!")
        print("Анализ завершен.")
