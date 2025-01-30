from aiogram.types import Message
from aiogram.filters import CommandStart,Command
from aiogram import Router
from keyboards.main_menu import main_menu_kb


router = Router()

@router.message(CommandStart())
async def start(message : Message):
    await message.answer(f"Привет {message.from_user.full_name}.Я бот для управления финансами",reply_markup=main_menu_kb())

    




