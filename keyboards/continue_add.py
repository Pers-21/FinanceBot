from aiogram.utils.keyboard import ReplyKeyboardBuilder

def continue_add():
    continue_add_expens = ReplyKeyboardBuilder()
    continue_add_expens.button(text="✅ Да, добавить ещё")
    continue_add_expens.button(text="❌ Нет, завершить")
    continue_add_expens.adjust(2)
    return continue_add_expens.as_markup(resize_markup=True)