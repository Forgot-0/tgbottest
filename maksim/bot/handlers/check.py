from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states.pdf_state import PdfWaiting
from .deps import users_dogs
from domain.user_dog import UserDogCreate
from PyPDF2 import PdfReader


router = Router()


@router.message(F.text, Command("send_check"))
async def set_state_waiting_pdf(message: Message, state: FSMContext):
    text = """Отправьте чек файлом в формате pdf"""
    await state.set_state(PdfWaiting.waiting_pdf)
    await message.answer(text)


@router.message(PdfWaiting.waiting_pdf)
async def get_pdf(message: Message, state: FSMContext):
    pdf_file = await message.bot.download(message.document)

    pdf = PdfReader(pdf_file)
    
    if 1==1:
        text = """Success download"""
        await message.answer(text)
        await state.set_state(PdfWaiting.waitind_dog_info)
    else:
        text = """Error"""
        await message.answer(text)
        await state.clear()


@router.message(PdfWaiting.waitind_dog_info)
async def get_info_dog(message: Message, state: FSMContext):
    user_dog = UserDogCreate(user_id=message.from_user.id, dog_info=message.text)
    await users_dogs.save(user_dog.model_dump())
    await message.answer("Спасибо! Все данные сохранены.")
    await state.clear()