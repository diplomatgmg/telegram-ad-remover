import logging
import re

from telethon.events import NewMessage  # type: ignore[import-untyped]

from client import tg_client
from core.config import app_config


logger = logging.getLogger(__name__)

AD_PATTERN = re.compile("|".join(app_config.patterns), re.IGNORECASE)


async def check_and_delete_message(message: NewMessage.Event, chat_id: int) -> None:
    if not (message and message.message):
        return

    if not AD_PATTERN.search(message.message):
        return

    logger.info("Ad detected in message %s from chat %s", message.id, chat_id)
    try:
        await message.delete()
        logger.info("Message %s deleted from chat %s", message.id, chat_id)
    except Exception as e:
        logger.exception(
            "Failed to delete message %s from %s. Reason: %s",
            message.id,
            chat_id,
            exc_info=e,
        )


async def new_message_handler(event: NewMessage.Event) -> None:
    """Handles new messages."""
    logger.debug("Handling new message: %s from chat id: %s", event.message.id, event.chat_id)
    await check_and_delete_message(event.message, event.chat_id)


async def check_recent_messages_on_startup() -> None:
    """Checks the last 5 messages in each configured channel on startup."""
    logger.info("Checking last 5 messages in configured channels...")

    for channel_id in app_config.channel_ids:
        try:
            messages = await tg_client.get_messages(channel_id, limit=5)
            logger.debug("Checking channel: %s. Found %s recent messages.", channel_id, len(messages))

            for message in messages:
                await check_and_delete_message(message, channel_id)

        except Exception as e:
            logger.exception("Could not process channel %s. Reason: %s", channel_id, exc_info=e)
