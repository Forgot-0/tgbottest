import motor.motor_asyncio
from settings import settings

MONGO_DETAILS = settings.database.url
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client['tgbot']

users = database['users']
dogs = database['dogs']
