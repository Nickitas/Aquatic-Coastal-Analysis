from nicegui import ui
from datetime import datetime
from src.ui.layout import create_layout


from src.ui.components.create_section_header import create_section_header


CITY_NAME = 'Ростов-на-Дону'

weather_data = {
    'temp': 25,
    'description': 'Переменная облачность'
}

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

        # username = get_username_by_token(token) or 'Неизвестный пользователь'
        # ui.label(f'Пользователь {username}').classes('text-xl font-medium my-2')

        with ui.row().classes('gap-4 items-start'):
            with ui.card().classes('max-w-sm p-4 shadow-lg'):
                ui.icon('cloud', size=120).classes('text-blue-500 mx-auto mb-2')
                ui.label(f"Погода в {CITY_NAME}").classes('text-lg font-semibold mb-1 text-center')
                ui.label(f"Температура: {weather_data['temp']} °C").classes('text-md text-center')
                ui.label(f"Условия: {weather_data['description']}").classes('text-md text-gray-600 text-center')

            with ui.card().classes('max-w-sm p-4 shadow-lg'):
                ui.icon('schedule', size=120).classes('text-green-500 mx-auto mb-1')
                time_label = ui.label().classes('text-md font-medium my-2 text-center')

                # def update_time():
                #     current_time = datetime.now().strftime('%H:%M:%S')
                #     time_label.set_text(f"{current_time}").classes('text-md font-extrabold my-2 text-center')

                # ui.timer(interval=1.0, callback=update_time)


        ui.label('«Выбрать годовой период»')
        ui.date(value='2023-01-01', on_change=lambda e: result.set_text(e.value))
        result = ui.label()


        ui.label('«Выбрать годовой период»')

        ui.button('Перейти к анализу береговой линии', on_click=lambda: ui.navigate.to('/analysis')) \
            .classes('mt-6 bg-blue-600 text-white hover:bg-blue-700')
