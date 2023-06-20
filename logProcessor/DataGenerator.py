import asyncio

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./LogFile.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

async def createEntry():
    while True:
        logger.info("Entry created")
        await asyncio.sleep(4)

if __name__ == "__main__":
    asyncio.run(createEntry())