from aiogram.fsm.state import State, StatesGroup



class PdfWaiting(StatesGroup):
    waiting_pdf = State()
    waitind_dog_info = State()