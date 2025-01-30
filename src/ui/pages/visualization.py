from nicegui import ui
from src.ui.layout import create_layout


from src.ui.components.create_section_header import create_section_header


@ui.page('/visualization')
def visualization_page():
    """
    Раздел "Визуализация".
    Цель: 
   Страница для интерактивных карт и динамических графиков.
    Блок «Карта региона» — например, Plotly/Leaflet (NiceGUI поддерживает встроенные решения).
    Слои (Layers) для переключения: «Береговая линия», «Нефтяные пятна», «Районы затопления», «Станции измерений».
    Возможность «играть» по временной шкале (Time slider), чтобы посмотреть, как менялась береговая линия за годы.
    """
    create_layout()

    with ui.column().classes('w-full px-4 py-2 gap-4'):
        # --------------------
        # 1. Заголовок
        # --------------------
        create_section_header(
            title='Визуализация',
            subtitle='Страница для интерактивных карт и динамических графиков.',
            heading_level=1
        )