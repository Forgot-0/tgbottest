import logging
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()



@dataclass
class BotConfig:

    token: str = getenv('BOT_TOKEN')


@dataclass
class Database:
    url: str = getenv('MONGO_URL')


@dataclass
class Settings:

    debug = bool(getenv('DEBUG'))
    logging_level = int(getenv('LOGGING_LEVEL', logging.INFO))

    bot = BotConfig()
    database = Database()


settings = Settings()