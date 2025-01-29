from nicegui import ui

def enable_dark_mode():
    ui.dark_mode().enable()

def disable_dark_mode():
    ui.dark_mode().disable()

def create_layout(MAIN_COLOR, FRAME_COLOR):
    """
    Обёртка (layout)
    """

    # Шапка (header)
    with ui.header(elevated=True).style(f'background-color: {MAIN_COLOR}').classes('items-center'):
        ui.button(on_click=lambda: ui.open('/'), icon='directions_boat').props('flat color=white')
        ui.label('Aquatic Coastal Analysis').classes('flex-grow text-xl font-semibold px-4 py-2')
        ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')

    # Левая выдвижная панель (drawer)
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('Модули').classes('text-lg font-bold mb-4')
        ui.button('Главная страница', on_click=lambda: ui.open('/')).classes('w-full')
        ui.button('Страница анализа', on_click=lambda: ui.open('/analysis')).classes('w-full')

    # Правая панель
    with ui.right_drawer(fixed=False).style(f'background-color: {FRAME_COLOR}').props('bordered') as right_drawer:
        ui.label('Настройки').classes('text-lg font-bold mb-4')
        ui.button('Dark', on_click=enable_dark_mode)
        ui.button('Light', on_click=disable_dark_mode)

    # Футер
    with ui.footer().style(f'background-color: {MAIN_COLOR}').classes('text-center'):
        ui.label('© 2025 Aquatic Coastal Analysis. All rights reserved.').classes('text-sm p-1')
