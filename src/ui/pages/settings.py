from nicegui import ui
from src.ui.layout import create_layout


from src.ui.components.create_section_header import create_section_header


@ui.page('/settings')
def settings_page():
    """
    Раздел "Настройка".
    Цель: предоставить возможность задавать интересующие координаты или выбирать мировые бассейны.
    Параметры, связанные с API-ключами, базами данных, логированием и пр.
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Настройки',
            subtitle='Управление конфигурациями приложения.',
            heading_level=1
        )