from nicegui import ui
from src.ui.layout import create_layout


from src.ui.components.create_section_header import create_section_header


@ui.page('/analysis')
def analysis_page():
    """
    Раздел "Анализ".
    Цель: предоставить возможность управления анализами и просмотра результатов.
    Подразделы (в виде вкладок ui.tabs() или отдельных кнопок):
    Coastline Analysis: визуализация береговой линии, вычисление скорости изменений, «before/after» картинки.
    Oil Spill Detection: загрузка снимков, результат сегментации, карта с пометками разливов.
    Flooding Risk: подсветка зон риска затопления, интеграция с данными о высоте местности.
    Sea Level Model (если хотите хранить анализ и модель вместе) или вынести в «Models».
    Каждая вкладка или страница может иметь кнопку «Запустить анализ», которая ссылается на соответствующую функцию Python. По завершении — вывод результатов (уведомление, таблица, график, карта).
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Анализ',
            subtitle='Доступ к проведении анализов.',
            heading_level=1
        )