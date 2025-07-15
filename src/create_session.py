import logging

import uvloop

from client import tg_client


logger = logging.getLogger(__name__)


# Because need docker execution (make create-session)
__all__ = ()


async def create_session() -> None:
    """
    Creates a new telethon session.

    Usage:
        make create-session
    """
    print("Starting session creation...")  # noqa: T201
    async with tg_client:
        pass


if __name__ == "__main__":
    uvloop.run(create_session())
