from aiogram.utils.keyboard import ReplyKeyboardBuilder

def continue_bt_stats():
    continue_bt_stats = ReplyKeyboardBuilder()
    continue_bt_stats.button(text="📈 Все доходы")
    continue_bt_stats.button(text="📉 Все расходы")
    continue_bt_stats.button(text="💵 Доходы по категориям")
    continue_bt_stats.button(text="🛒 Расходы по категориям")
    continue_bt_stats.button(text="💳 Ваш текущий баланс")
    continue_bt_stats.button(text="🏠 Главное меню")
    continue_bt_stats.adjust(2)
    return continue_bt_stats.as_markup(resize_markup=True)
