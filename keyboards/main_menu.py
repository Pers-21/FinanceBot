from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="💸 Добавить расход")
    builder.button(text="💰 Добавить доход")
    builder.button(text="📊 Статистика")
    builder.button(text="⚙️ Настройки")
    builder.adjust(2)
    return builder.as_markup(resize_markup = True)