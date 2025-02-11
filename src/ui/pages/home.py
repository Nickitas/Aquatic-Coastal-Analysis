from datetime import datetime
from nicegui import ui
from src.ui.layout import create_layout

from src.ui.components.create_section_header import create_section_header
from analysis.coastal_weather_forecast import CoastalWeatherForecast

CITY_NAME = 'Ростов-на-Дону'

locations = {
    "Ростов-на-Дону": (47.236, 39.718),
    "Черное море": (43.0, 30.0),
    "Азовское море": (47.0, 37.5),
    "Средиземное море": (35.0, 18.0),
    "Балтийское море": (58.0, 20.0),
    "Северное море": (55.0, 5.0)
}

forecast = CoastalWeatherForecast(locations)
forecast_data = forecast.get_forecasts() or {}

@ui.page('/')
def home_page():
    """
    Главная страница приложения.
    Цель: дать пользователю быструю сводку всех важных метрик и состояний:
    Карточка с последними значениями уровня моря, скорости смещения береговой линии, прогнозы на неделю/месяц.
    Chart-виджеты с историей изменений.
    Блок «Последние события» (например, предупреждение о потенциальном разливе нефти).
    Несколько кнопок-ссылок «Перейти к деталям» (Analysis, Models).
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Добро пожаловать в Aquatic Coastal Analysis!',
            subtitle='Ваш инструмент для анализа прибрежных систем и прогноза погоды.',
            heading_level=1
        )

        # Карточка с прогнозом погоды для выбранного города
        with ui.row().classes('gap-4 items-start'):
            with ui.card().classes('max-w-sm p-4 shadow-lg'):
                ui.icon('cloud', size=120).classes('text-blue-500 mx-auto mb-2')
                ui.label(f"Погода в {CITY_NAME}").classes('text-lg font-semibold mb-1 text-center')

                weather = forecast_data.get(CITY_NAME, {})
                ui.label(f"Температура: {weather.get('temp', 'N/A')} °C").classes('text-md text-center')
                ui.label(f"Условия: {weather.get('description', 'N/A')}").classes('text-md text-gray-600 text-center')


        