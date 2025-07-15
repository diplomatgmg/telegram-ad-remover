from telethon import TelegramClient  # type: ignore[import-untyped]

from core.config import BASE_DIR, app_config
from environment.config import env_config


__all__ = ["tg_client"]


session_path = BASE_DIR / f"{env_config.project_name}-session.session"

tg_client = TelegramClient(
    session_path,
    app_config.telethon_api_id,
    app_config.telethon_api_hash,
)
