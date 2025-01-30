from fastapi import Request
from starlette.responses import RedirectResponse
from nicegui import ui
from src.session_manager import sessions, is_session_valid

@ui.page('/logout')
def logout_page(request: Request):
    token = request.cookies.get('session_token', '')
    if is_session_valid(token):
        del sessions[token]  # удаляем токен из хранилища
    response = RedirectResponse(url='/signin')
    response.delete_cookie(key='session_token')
    return response
