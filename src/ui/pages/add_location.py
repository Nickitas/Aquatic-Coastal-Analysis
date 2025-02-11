import os
from nicegui import ui
from dotenv import load_dotenv

from src.global_state import global_state 
from src.__utils.data_loader import load_datasets
from src.ui.layout import create_layout
from src.ui.components.create_section_header import create_section_header

load_dotenv()

MAP_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')

@ui.page('/add_location')
def add_location_page():
    """
    Раздел "Добавление объекта исследования". 
    Цель: предоставить возможность задавать интересующие координаты или выбирать мировые бассейны.
    """
    create_layout()

    # Загружаем данные о водных объектах
    aquatic_data = load_datasets()
    aquatic_objects = aquatic_data.get('marine_polys_10m', None)

    # Проверяем наличие данных в marine_objects
    if aquatic_objects is not None and not aquatic_objects.empty:
        marine_names = aquatic_objects['name'].fillna('Без имени').tolist()
    else:
        marine_names = []
        print("Внимание: Данные о морских объектах отсутствуют или невалидны.")

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Добавить местоположение',
            subtitle='Введите координаты нужного места или выберите объект из списка.',
            heading_level=1
        )

        # --------------------
        # 1. Форма
        # --------------------
        with ui.column().classes('gap-6 w-full p-4 rounded-lg'):
            def on_select_change(selected_item):
                ui.notify(f'Вы выбрали: {selected_item}', color='blue')

            def add_location():
                # Доступ к значениям
                if  (name.value and longitude_min.value and latitude_min.value and longitude_max.value and latitude_max.value) or (name.value and aquatic_object_name.value):
                    
                    print(aquatic_objects['name'])
                    # Получить 4 точки координат по названию из aquatic_objects...

                    # Сохраняем данные в global_state
                    global_state.current_target['name'] = name.value
                    global_state.current_target['latitude_max'] = latitude_max.value
                    global_state.current_target['longitude_min'] = longitude_min.value
                    global_state.current_target['latitude_min'] = latitude_min.value
                    global_state.current_target['longitude_max'] = longitude_max.value

                    ui.notify(
                        f'Добавлено местоположение: {global_state.current_target["name"]} ({global_state.current_target["latitude_max"]}, {global_state.current_target["longitude_min"]}, {global_state.current_target["latitude_min"]}, {global_state.current_target["longitude_max"]})',
                        color='green'
                    )
                else:
                    ui.notify('Пожалуйста, заполните все поля!', color='red')

            # Вкладки
            with ui.tabs().classes('w-full mt-4 bg-gray-100 rounded-md') as tabs:
                one = ui.tab('Бассейны')
                two = ui.tab('Координаты')

            name = ui.input('Название местоположения').classes('w-full').props('outlined')

            with ui.tab_panels(tabs, value=two).classes('w-full'):
                with ui.tab_panel(one):
                    if marine_names:
                        ui.label('Доступные акватические объекты').classes('text-lg font-semibold text-gray-600')
                        aquatic_object_name = ui.select(
                            marine_names,
                            label='Выберите акватический объект',
                            on_change=lambda e: on_select_change(e.value)
                        ).classes('w-1/2 mt-2')
                    else:
                        ui.label('Нет доступных данных о акватических объектах').classes('text-red-500 mt-2')

                # Панель для координат
                with ui.tab_panel(two):
                    ui.label('Укажите границы местоположения (широта и долгота)').classes('text-lg font-semibold text-gray-600')

                    with ui.row().classes('gap-6 mt-4'):
                        with ui.column():
                            ui.label('Северо-западный угол (верхний левый угол): ').classes('text-sm text-gray-500')
                            latitude_max = ui.input('Широта [latitude_max]').classes('w-full mt-2').props('outlined type=number')
                            longitude_min = ui.input('Долгота [longitude_min]').classes('w-full mt-2').props('outlined type=number')

                        with ui.column():
                            ui.label('Юго-восточный угол (нижний правый угол): ').classes('text-sm text-gray-500')
                            latitude_min = ui.input('Широта [latitude_min]').classes('w-full mt-2').props('outlined type=number')
                            longitude_max = ui.input('Долгота [longitude_max]').classes('w-full mt-2').props('outlined type=number')

            # --------------------
            # 3. Кнопки
            # --------------------
            with ui.row().classes('gap-4 mt-4'):
                ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/settings')).classes(
                    'w-300 mt-6 py-2 bg-gray-500 hover:bg-gray-200 text-white font-bold rounded-lg shadow-md'
                )
                ui.button('Задать местоположение', on_click=add_location).classes(
                    'w-300 mt-6 py-2 bg-blue-500 hover:bg-blue-600 text-white font-bold rounded-lg shadow-md'
                )

    # =========================================================
    print(f'Акватические объекты >>>\n {aquatic_objects.head()}')
    print(f'Заданное место >>> {global_state.current_target["name"]} ({global_state.current_target["latitude_max"]}, {global_state.current_target["longitude_min"]}, {global_state.current_target["latitude_min"]}, {global_state.current_target["longitude_max"]})')
