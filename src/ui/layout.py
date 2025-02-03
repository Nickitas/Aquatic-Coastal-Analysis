from nicegui import ui

from src.ui.components.create_section_header import create_section_header

dark = ui.dark_mode()

def create_layout():
    ACCENT_COLOR = '#3874c8'
    MAIN_COLOR_LIGHT = '#3b82f6'
    MAIN_COLOR_DARK = '#3b82f6'

    """
    Обёртка (layout)
    """
    # HEADER
    with ui.header(elevated=True) \
            .classes('items-center'):
        ui.button(on_click=lambda: ui.navigate.to('/'), icon='tsunami') \
            .props('flat color=white')
        ui.label('Aquatic Coastal Analysis').classes('flex-grow text-xl font-semibold')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu') \
            .props('flat color=white')

    # ЛЕВАЯ ПАНЕЛЬ
    with ui.left_drawer(top_corner=True, bottom_corner=True) \
            .classes('w-38 p-4 bg-gray-100 dark:bg-slate-900'):
        create_section_header(
            title='Настройки',
            subtitle='Введите координаты нужного места или нажмите на карту',
            heading_level=3
        )


        with ui.tabs().classes('w-full') as tabs:
            one = ui.tab('Координаты')
            two = ui.tab('Карта')
        with ui.tab_panels(tabs, value=two).classes('w-full'):
            with ui.tab_panel(one):
                ui.label('Введите координаты: ').classes('text-lg font-light text-gray-600 dark:text-white')
                ui.input('Широта', placeholder='47.236')
                ui.input('Долгота', placeholder='39.718')
            with ui.tab_panel(two):
                ui.label('Окно карты')

        
        ui.label('Погода').classes('text-lg font-light text-gray-600 dark:text-white')
        grid = ui.aggrid({
            'defaultColDef': {'flex': 1},
            'columnDefs': [
                {'headerName': 'Параметр', 'field': 'name'},
                {'headerName': 'Значение', 'field': 'value'},
            ],
            'rowData': [
                {'name': 'Описание', 'value': "",},
                {'name': 'Температура', 'value': "",},
                {'name': 'Давление', 'value': "",},
                {'name': 'Влажность', 'value': "",},
                {'name': 'Ветер', 'value': "",},
                {'name': 'Видимость', 'value': "",},
                {'name': 'Восход солнца', 'value': "",},
                {'name': 'Закат солнца', 'value': "",},
            ],
            'rowSelection': 'multiple',
        })


    # ПРАВАЯ ПАНЕЛЬ
    with ui.right_drawer(fixed=False).props('bordered') as right_drawer:
        def nav_button(icon_name: str, text: str, route: str):
            ui.button(text, icon=icon_name, on_click=lambda: ui.navigate.to(route)) \
                .props('flat') \
                .classes('hover:bg-gray-200 dark:hover:bg-slate-700 rounded-md')

        nav_button('dashboard', 'Dashboard', '/')
        nav_button('folder', 'Данные', '/data')
        nav_button('analytics', 'Анализ', '/analysis')
        nav_button('model_training', 'Модели', '/models')
        nav_button('map', 'Визуализация', '/visualization')
        nav_button('settings', 'Настройки', '/settings')

        ui.separator().classes('mt-auto')
        with ui.row().classes('flex items-center gap-2'):
            ui.button(icon='dark_mode', on_click=dark.toggle)
            ui.button(icon='light_mode', on_click=dark.toggle)
            ui.label('Цветовая тема').classes('text-md text-gray-600')

        ui.separator()
        nav_button('logout', 'Выйти', '/signin')

    # ФУТЕР
    with ui.footer():
        ui.label('© 2025 Aquatic Coastal Analysis. All rights reserved.') \
            .classes('text-sm p-1 text-white')
