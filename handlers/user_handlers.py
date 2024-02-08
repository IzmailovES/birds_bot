from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router

from database.database import birds

router = Router()

@router.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text='Hello! this is birds bot!')

@router.message(Command(commands=['list']))
async def list_of_birds(message:Message):
    lst = '\n'.join(map(lambda x: x.short_name, birds))
    await message.answer(f'list of birds:\n{lst}')

@router.message(Command(commands=['count']))
async def birds_count(message:Message):
    await message.answer(f'count birds in base: {len(birds)}')

@router.message(Command(commands=['list_images']))
async def list_images(message:Message):
    await message.answer('there is list of birds with foto')
