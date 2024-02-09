from aiogram.types import BotCommand
from dataclasses import dataclass
from aiogram import Bot
@dataclass
class _MC:
    command:str
    description:str
    
    def get_bot_command(self):
        return BotCommand(command=self.command, description=self.description)

_menu_common = (_MC('/start', 'Start/restart bot'),
               _MC('/help', 'help about bot'),
               _MC('/list', 'list of avaible commands'),
               )


async def set_main_menu(bot: Bot):
    await bot.set_my_commands([x.get_bot_command() for x in _menu_common])



