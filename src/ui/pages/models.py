from nicegui import ui
from src.ui.layout import create_layout


from src.ui.components.create_section_header import create_section_header


@ui.page('/models')
def models_page():
    """
    Раздел "Модели".
    Цель: 
    Список доступных моделей:
    Sea Level Forecast
    Coastline Dynamics
    Atmospheric Effects
    Для каждой модели — кнопки (перезапустить обучение, посмотреть метрики, загрузить/сохранить).
    Графики точности, ошибок, прогнозов.
    Если нужно — функционал «подбор гиперпараметров» (выбор, say, learning rate, epochs и т. п.).
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Модели',
            subtitle='Управление моделями машинного обучения.',
            heading_level=1
        )