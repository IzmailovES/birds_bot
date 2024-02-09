#!/usr/bin/env python3

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
import logging
import dotenv
import os

from config_data import global_config

from handlers import admin_handlers, other_handlers, user_handlers

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='#%(levelname)-8s %(filename)s:%(lineno)d '
                                '[%(asctime)s] - %(name)s - %(message)s')
    #config=config_data.load_config()

    logger.debug('Start main')
    dp = Dispatcher()
    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    bot = Bot(token=global_config.tg_bot.token)

    logger.debug('Starting polling')
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
