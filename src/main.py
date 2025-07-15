import logging

from telethon.events import NewMessage  # type: ignore[import-untyped]
import uvloop

from client import tg_client
from core.config import app_config
from handlers import new_message_handler
from logger.factory import setup_logger


setup_logger()

logger = logging.getLogger(__name__)


async def main() -> None:
    try:
        async with tg_client:
            logger.info("Telegram client started")
            tg_client.on(NewMessage(chats=app_config.channel_ids))(new_message_handler)
            await tg_client.run_until_disconnected()
    except EOFError:
        logger.critical("Session invalid or not found. Use 'make create-session'")
        return


if __name__ == "__main__":
    uvloop.run(main())
