import asyncio
import logging
from aiogram import Dispatcher, Bot
from bot.handlers import routers
from settings import settings
from aiogram.fsm.storage.memory import MemoryStorage




async def main() -> None:
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(settings.bot.token, parse_mode="HTML")

    dp.include_routers(*routers)

    try:
        await dp.start_polling(bot)
    finally:
        bot.session.close()



if __name__ == "__main__":
    logging.basicConfig(level=settings.logging_level)
    asyncio.run(main())