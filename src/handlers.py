import logging
import re

from telethon.events import NewMessage  # type: ignore[import-untyped]

from core.config import app_config


logger = logging.getLogger(__name__)


AD_PATTERN = re.compile("|".join(app_config.patterns), re.IGNORECASE)


async def new_message_handler(event: NewMessage.Event) -> None:
    logger.debug("Handling new message: %s from chat id: %s", event.message.id, event.chat_id)

    if AD_PATTERN.search(event.message.message):
        logger.info("Ad detected from chat id: %s, message id: %s", event.chat_id, event.message.id)

        try:
            await event.delete()
            logger.info("Message id %s deleted from chat id: %s", event.message.id, event.chat_id)
        except Exception as e:
            logger.exception(
                "Failed to delete message id %s from chat id: %s",
                event.message.id,
                event.chat_id,
                exc_info=e,
            )
