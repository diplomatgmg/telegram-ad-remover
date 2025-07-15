import asyncio
import logging

import uvloop

from logger.factory import setup_logger


setup_logger()

logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Hello, World!")
    await asyncio.sleep(1)


if __name__ == "__main__":
    uvloop.run(main())
