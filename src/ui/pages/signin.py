import os
from dotenv import load_dotenv
from datetime import datetime
from fastapi import Request
from starlette.responses import RedirectResponse
from nicegui import ui

from src.ui.layout import create_layout
from src.session_manager import create_session, is_session_valid, sessions

load_dotenv()

ENV_LOGIN = os.getenv('APP_LOGIN', 'admin')
ENV_PASSWORD = os.getenv('APP_PASSWORD', 'verysecret')

@ui.page('/signin')
def signin_page(request: Request):
    """Страница авторизации."""
    create_layout()

    with ui.column().classes('items-center justify-center w-full py-10'):
        ui.label('Вход в систему').classes('text-2xl font-bold mb-4')

        username_input = ui.input('Логин').classes('mb-2 w-64')
        password_input = ui.input('Пароль').props('type=password').classes('mb-4 w-64')

        def handle_signin():
            username = username_input.value
            password = password_input.value
            if username == ENV_LOGIN and password == ENV_PASSWORD:
                ui.notify('Авторизация успешна!', color='green')

                # 1. Создаём токен и сессию
                session_token = create_session(username)

                # 2. Устанавливаем cookie
                # Получаем "response" из текущего request; работаем через Starlette
                response = RedirectResponse(url='/')
                response.set_cookie(
                    key='session_token',
                    value=session_token,
                    max_age=24*3600,        # 24 часа (в секундах)
                    expires=24*3600,        # также 24 часа
                    httponly=True,          # cookie нельзя читать из JS
                    secure=False,           # в продакшене True (требуется HTTPS)
                )
                # Завершаем работу, возвращая RedirectResponse
                # NiceGUI уловит это и сделает редирект
                ui.run_javascript('')  # костыль, чтобы NiceGUI понимала, что мы отдали свой response
                return response
            else:
                ui.notify('Неверный логин или пароль.', color='red')

        ui.button('Войти', on_click=handle_signin) \
           .classes('bg-blue-600 text-white hover:bg-blue-700 w-64')
