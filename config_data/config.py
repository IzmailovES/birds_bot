
from dataclasses import dataclass
import dotenv
import os

@dataclass
class TgBot:
    token: str
    superadmin: int
    admins: list[int] | None

class Config:
    tg_bot: TgBot



def load_config(path: str | None = None) -> Config:
    dotenv.load_dotenv(path)
    return Config()

