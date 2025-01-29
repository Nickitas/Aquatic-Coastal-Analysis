from nicegui import ui

# Глобальные настройки интерфейса
MAIN_COLOR = '#3874c8'
FRAME_COLOR = '#ebf1fa'

def configure_ui():
    """
    Функция, которая настраивает общие аспекты NiceGUI:
    """

    # 1. Подтягиваем глобальную структуру (header, footer, drawers)
    # from .layout import create_layout
    # create_layout(MAIN_COLOR, FRAME_COLOR)

    # 2. Подключаем страницы (импортируются после create_layout, чтобы избежать циклов импорта)
    from .pages import home, analysis_page
    # from .pages import some_other_page