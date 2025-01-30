from aiogram.types import Message
from aiogram import Router,types
from services.database import get_expenses,get_incomes,detailed_incomes,detailed_expenses
from keyboards.stats_button import continue_bt_stats
from keyboards.main_menu import main_menu_kb


router = Router()

@router.message(lambda message:message.text == "📊 Статистика" )
async def get_stats(message:Message):
    await message.answer("📊 Выберите тип статистики:",reply_markup=continue_bt_stats())

@router.message(lambda message:message.text == "📈 Все доходы")
async def get_detailed_stats_incomes(message:Message):
    user_id = message.from_user.id
    rows_incomes = await detailed_incomes(user_id)
    result_message = "Все ваши Доходы:\n\n"
    for category,sum_income,date in rows_incomes:
        result_message += f"Категория {category}:{sum_income} руб. Дата дохода: {date}\n"
    await message.answer(result_message)

@router.message(lambda message:message.text == "📉 Все расходы")
async def get_detailed_stats_expenses(message:Message):
    user_id = message.from_user.id
    rows_expenses = await detailed_expenses(user_id)
    result_message = "Все ваши Расходы:\n\n"
    for category,sum_expens,date in rows_expenses:
        result_message += f"Категория {category}:{sum_expens} руб. Дата расхода: {date}\n"
    await message.answer(result_message)

@router.message(lambda message:message.text == "💵 Доходы по категориям")
async def get_sum_incomes(message:Message):
    user_id = message.from_user.id
    incomes = await get_incomes(user_id)
    result_message = "Сумма вашего дохода по котегориям:\n"
    for category,sum_incomes in incomes:
        result_message += f"\n-Категория:{category}:{sum_incomes} руб."
    await message.answer(result_message)

@router.message(lambda message:message.text == "🛒 Расходы по категориям")
async def get_sum_expenses(message:Message):
    user_id = message.from_user.id
    expenses = await get_expenses(user_id)
    result_message = "Сумма вашего расхода по котегориям:\n"
    for category,sum_expenses in expenses:
        result_message += f"\n-Категория:{category}:{sum_expenses} руб."
    await message.answer(result_message)


@router.message(lambda message:message.text == "💳 Ваш текущий баланс")
async def use_balance(message:types.Message):
    user_id = message.from_user.id
    incomes = await get_incomes(user_id)
    expenses = await get_expenses(user_id)
    user_balance = 0
    for categories_incomes,sum_incomes in incomes:
        user_balance += sum_incomes
    for categories_expenses,sum_expenses in expenses:
        user_balance -= sum_expenses
    await message.answer(f"Ваш баланс:{user_balance} руб.")

@router.message(lambda message:message.text == "🏠 Главное меню")
async def return_main_menu(message:Message):
    await message.answer("Возвращаюсь на главное меню!",reply_markup=main_menu_kb())




