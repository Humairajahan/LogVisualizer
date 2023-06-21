import asyncio
import random
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler("./LogFile.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def asleep_for_time():
    return random.randrange(9)


async def createEntry():
    while True:
        logger.info("Entry created")
        await asyncio.sleep(asleep_for_time())


if __name__ == "__main__":
    asyncio.run(createEntry())
