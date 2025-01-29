from nicegui import ui
from src.ui.layout import create_layout
# from src.analysis.coastline_analysis import analyze_coastline

@ui.page('/analysis')
def analysis_page():
    """Страница анализа береговой линии."""

    create_layout('#3874c8', '#ebf1fa')

    ui.label('Анализ береговой линии')

    # def run_coastline_analysis():
    #     # Допустим, здесь идёт реальный анализ
    #     result = analyze_coastline()
    #     ui.notify(f'Результаты анализа: {result}')

    # ui.button('Запустить анализ', on_click=run_coastline_analysis)
    # ui.button('Вернуться на главную', on_click=lambda: ui.open('/'))
