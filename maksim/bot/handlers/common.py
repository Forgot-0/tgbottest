from aiogram import Router, F
from aiogram.filters.command import Command, CommandStart
from aiogram.filters.state import StateFilter
from aiogram.types import Message
from .deps import users
from domain.user import UserCreate


router = Router()


@router.message(F.text, Command("start"))
async def start(message: Message):
    text = """Описание бота с его коммандами


    """
    user = UserCreate(user_id=message.from_user.id, username=message.from_user.username)
    await users.save(user.model_dump())
    await message.answer(text)



