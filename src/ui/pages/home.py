from nicegui import ui
from src.ui.layout import create_layout

@ui.page('/')
def home_page():
    """Главная страница приложения."""

    create_layout('#3874c8', '#ebf1fa')

    ui.label('Добро пожаловать в Aquatic Coastal Analysis!')
    ui.button('Перейти к анализу береговой линии', on_click=lambda: ui.open('/analysis'))
