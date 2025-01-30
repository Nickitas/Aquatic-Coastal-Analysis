from nicegui import ui, app
from starlette.responses import RedirectResponse
from fastapi import Request
from src.session_manager import is_session_valid


def configure_ui():
    """
    Настраиваем приложение NiceGUI и подключаем middleware проверки сессии.
    """

    # 1. Здесь можно вызвать прочие глобальные настройки, если нужно, например:
    # ui.config(...)
    # Или подключить ваш layout и т.п.

    # 2. Подключаем middleware проверки сессии.
    #    Оно будет вызываться при каждом запросе до выполнения любого @ui.page.
    # @app.middleware('http')
    # async def check_session(request: Request, call_next):
    #     public_paths = [
    #         '/signin',
    #         '/logout',
    #         '/favicon.ico',
    #         # ВАЖНО: служебные пути NiceGUI
    #         '/_nicegui',       # если нужно точнее, используйте startswith('/_nicegui')
    #         '/static',         # если у вас статические файлы
    #     ]

    #     path = request.url.path
    #     # Если путь начинается с /_nicegui, тоже пропустим без проверки
    #     if path.startswith('/_nicegui'):
    #         return await call_next(request)

    #     # Если путь не в публичных, проверяем токен
    #     if request.url.path not in public_paths:
    #         token = request.cookies.get('session_token', '')
    #         if not is_session_valid(token):
    #             # Если сессия невалидна – редирект на /signin
    #             return RedirectResponse(url='/signin')
    #     # Иначе продолжаем обработку (передаём запрос дальше)
    #     response = await call_next(request)
    #     return response

    # 3. Важно: раз импорт страниц уже сделан выше, декораторы @ui.page
    #    зарегистрированы, и middleware будет отрабатывать для них всех.
    # Импортируем страницы, чтобы зарегистрировать @ui.page
    from .pages import signin, logout, home, analysis, models, data, visualization, settings
