
from dataclasses import dataclass
import dotenv
import os

@dataclass
class TgBot:
    token: str
    admin: int
    admins: list[int] | None = None


@dataclass
class Config:
    tg_bot: TgBot



def load_config(path: str | None = None) -> Config:
    dotenv.load_dotenv(path)
    return Config(tg_bot=TgBot(token=os.getenv('BOT_TOKEN'),
                               admin=os.getenv('ADMIN_ID')))

