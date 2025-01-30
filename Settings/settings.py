from aiogram import Router
from aiogram.types import Message
from keyboards.main_menu import main_menu_kb
router = Router()

@router.message(lambda message:message.text == "⚙️ Настройки")
async def settings(message:Message):
    await message.answer("Ведутся работы,пока этот раздел недоступен.",reply_markup=main_menu_kb())
# TODO: Реализовать функционал настроек