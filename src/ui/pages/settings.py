import os
from nicegui import ui
from dotenv import load_dotenv

from src.global_state import global_state 
from src.__utils.data_loader import load_datasets
from src.ui.layout import create_layout
from src.ui.components.create_section_header import create_section_header

load_dotenv()

MAP_API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')

@ui.page('/settings')
def settings_page():
    """
    Раздел "Настройка". 
    Цель: предоставить возможность задавать интересующие координаты или выбирать мировые бассейны.
    Параметры, связанные с API-ключами, базами данных, логирование и пр.
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


    def save_user_data():
        pass


    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Настройки',
            subtitle='Добавление интересующих местоположений в список исследуемых.',
            heading_level=1
        )

        # --------------------
        # 1. Форма
        # --------------------
        with ui.column().classes('gap-6 w-full p-4 rounded-lg'):
            # Вкладки
            with ui.tabs().classes('w-full mt-4 bg-gray-100 dark:bg-gray-800 rounded-md') as tabs:
                one = ui.tab('Объекты')
                two = ui.tab('Аккаунт')

            with ui.tab_panels(tabs, value=one).classes('w-full'):
                with ui.tab_panel(one):
                    create_section_header(
                        title='Объекты',
                        subtitle='У Вас сейчас {count} исследуемых объектов. Выберете интересующий Вас объект.',
                        heading_level=3,
                        sep=False
                    )

                    ui.button('Добавить новый', on_click=lambda: ui.navigate.to('/add_location')).classes(
                        'w-300 py-2 dark:bg-sky-950 hover:bg-blue-600 text-white font-bold rounded-lg shadow-md'
                    )

                    grid = ui.aggrid({
                        'defaultColDef': {'flex': 1},
                        'columnDefs': [
                            {'headerName': 'Название', 'field': 'name'},
                            {'headerName': 'latitude_max', 'field': 'latitude_max'},
                            {'headerName': 'longitude_min', 'field': 'longitude_min'},
                            {'headerName': 'latitude_min', 'field': 'latitude_min'},
                            {'headerName': 'longitude_max', 'field': 'longitude_max'},
                        ],
                        'rowData': [
                            {'name': 'Ростов-на-Дону', 'latitude_max': "", 'longitude_min': "", 'latitude_min': "", 'longitude_max': "",},
                            {'name': 'Черное море', 'latitude_max': "", 'longitude_min': "", 'latitude_min': "", 'longitude_max': "",},
                            {'name': 'Балтийское море', 'latitude_max': "", 'longitude_min': "", 'latitude_min': "", 'longitude_max': "",},
                           
                        ],
                        'rowSelection': 'multiple',
                    })


                with ui.tab_panel(two):
                    create_section_header(
                        title='Мой аккаунт',
                        subtitle='Измените данные Вашего аккаунтом.',
                        heading_level=3,
                        sep=False
                    )
                    
                    with ui.row():
                        with ui.column():
                            ui.label('Укажите данные аккаунта').classes('text-lg font-semibold text-gray-600')
                            login = ui.input('Логин').classes('w-full mt-2').props('outlined type=text')
                            password = ui.input('Пароль').classes('w-full mt-2').props('outlined type=text')
                        with ui.column():
                            ui.label('Укажите персональные данные').classes('text-lg font-semibold text-gray-600')
                            fio = ui.input('ФИО').classes('w-full mt-2').props('outlined type=text')
                            email = ui.input('Почта').classes('w-full mt-2').props('outlined type=mail')
                            phone_number = ui.input('Номер телефона').classes('w-full mt-2').props('outlined type=phone')

                    ui.button('Сохранить', on_click=save_user_data).classes(
                        'w-300 mt-6 py-2 bg-blue-500 hover:bg-blue-600 text-white font-bold rounded-lg shadow-md'
                    )

