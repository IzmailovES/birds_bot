#!/usr/bin/env python3

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

import asyncio
import logging
import dotenv
import os

import config_data

import database as db


logger = logging.getLogger(__name__)


dp = Dispatcher()
@dp.message(Command(commands=['start']))
async def process_start_command(message:Message):
    await message.answer('Hello! This is birds bot')


@dp.message(Command(commands=['list']))
async def list_of_birds(message:Message):
    lst = map(lambda x: x.short_name, birds)
    string = '\n'.join(lst)
    await message.answer(f'list of birds:\n{string}')


@dp.message(Command(commands=['list_images']))
async def list_of_birds(message:Message):
    await message.answer('list of birds with images')


@dp.message(Command(commands=['count']))
async def birds_count(message:Message):
    await message.answer(f'count of birds  in base: {len(birds)}')


@dp.message()
async def default_answer(message:Message):
    #print(message.__dict__)
    logger.info(str(message.from_user.id) + '-' + message.from_user.username +  ': ' +  message.text)
    await message.answer('default answer to non-handling message')

async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='#%(levelname)-8s %(filename)s:%(lineno)d '
                                '[%(asctime)s] - %(name)s - %(message)s')
    config=config_data.load_config()

    bot = Bot(token=config.tg_bot.token)

    birds = db.load_birds('dbb')
    logger.info('Starting polling')
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
