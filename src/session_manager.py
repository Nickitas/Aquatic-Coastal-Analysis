import secrets
from datetime import datetime, timedelta

# Хранилище сессий. Ключ — session_token, значение — (expiry_datetime, username)
sessions = {}

SESSION_LIFETIME_HOURS = 24

def create_session(username: str) -> str:
    """Генерирует новый session_token, сохраняет его в словарь сессий."""
    token = secrets.token_hex(16)  # случайная строка
    expiry = datetime.utcnow() + timedelta(hours=SESSION_LIFETIME_HOURS)
    sessions[token] = (expiry, username)
    return token

def is_session_valid(token: str) -> bool:
    """Проверяет, есть ли такой токен, и не истёк ли."""
    if token not in sessions:
        return False
    expiry, _ = sessions[token]
    if datetime.utcnow() > expiry:
        # Сессия истекла
        del sessions[token]  # сразу почистим
        return False
    return True

def get_username_by_token(token: str) -> str:
    """Если токен валиден, вернуть имя пользователя, иначе None."""
    if not is_session_valid(token):
        return None
    return sessions[token][1]
