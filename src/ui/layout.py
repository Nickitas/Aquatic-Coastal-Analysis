from nicegui import ui

from src.ui.components.create_section_header import create_section_header


def create_layout():
    """
    Обёртка (layout)
    """
    dark = ui.dark_mode()
    dark.enable()

    # --------------------
    # HEADER
    # --------------------
    with ui.header(elevated=True) \
            .classes('items-center bg-blue-500 dark:bg-blue-950'):
        ui.button(on_click=lambda: ui.navigate.to('/'), icon='tsunami') \
            .props('flat color=white')
        ui.label('Aquatic Coastal Analysis').classes('flex-grow text-xl font-semibold')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu') \
            .props('flat color=white')

    # --------------------
    # LEFT DRAWER
    # --------------------
    with ui.left_drawer(top_corner=True, bottom_corner=True) \
            .classes('w-38 p-4 bg-slate-200 dark:bg-slate-900'):

        ui.label('Погода').classes('text-lg font-light text-zinc-800 dark:text-zinc-200')
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

    # --------------------
    # RIGHT DRAWER
    # --------------------
    with ui.right_drawer(fixed=True).classes('bg-blue-500 dark:bg-blue-950') as right_drawer:
        def nav_button(icon_name: str, text: str, route: str):
            ui.button(text, icon=icon_name, on_click=lambda: ui.navigate.to(route)) \
                .props('flat') \
                .classes('text-white hover:bg-slate-700/50 dark:hover:bg-slate-700/50 rounded-md')

        nav_button('dashboard', 'Dashboard', '/')
        nav_button('folder', 'Данные', '/data')
        nav_button('analytics', 'Анализ', '/analysis')
        nav_button('model_training', 'Модели', '/models')
        nav_button('map', 'Визуализация', '/visualization')
        nav_button('settings', 'Настройки', '/settings')

        ui.separator().classes('mt-auto bg-slate-200 dark:bg-slate-700')
        with ui.row().classes('flex items-center gap-2'):
            ui.label('Цветовая тема').classes('text-md text-white dark:text-white')
            ui.button(icon='dark_mode', on_click=dark.enable)
            ui.button(icon='light_mode', on_click=dark.disable)

        ui.separator().classes('bg-slate-200 dark:bg-slate-700')
        nav_button('logout', 'Выйти', '/signin')

    
    # --------------------
    # FOOTER
    # --------------------
    with ui.footer().classes('bg-blue-500 dark:bg-blue-950'):
        ui.label('© 2025 Aquatic Coastal Analysis. All rights reserved.') \
            .classes('text-sm p-1 text-white')

