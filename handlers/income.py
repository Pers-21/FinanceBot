from aiogram import Router,types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
from keyboards.categories import catogories_income_button
from keyboards.continue_add import continue_add
from keyboards.main_menu import main_menu_kb
from services.database import add_income  


class Income(StatesGroup):
    waiting_income = State()
    waiting_process_income = State()
    continueadd_income = State()


router = Router()

@router.message(lambda message:message.text == "💰 Добавить доход")
async def add_income_handler(message:types.Message,state:FSMContext):
    await message.answer("Выберите категорию или укажите свою:",reply_markup=catogories_income_button())
    await state.set_state(Income.waiting_income)

@router.message(Income.waiting_income)
async def select_catigory_income(message:Message,state:FSMContext):
    category_text_income = message.text
    await state.update_data(category = category_text_income)
    await message.answer("Укажите сумму дохода")
    await state.set_state(Income.waiting_process_income)

@router.message(Income.waiting_process_income)
async def process_income(message:Message,state:FSMContext):
    user_data = await state.get_data()
    category_text_income = user_data.get("category")
    sum_income = message.text
    await add_income(message.from_user.id, category_text_income, sum_income) 
    if message.text.isdigit():  
        await message.answer(f"Доход в категорию {category_text_income}:  на сумму {sum_income} руб. успешно добавлен!")
        await message.answer("💬 Хотите добавить ещё один доход?",reply_markup=continue_add())
        await state.set_state(Income.continueadd_income)
    else:
        await message.answer("Пожалуйста, введите корректную сумму (только цифры).")
        await state.set_state(Income.waiting_process_income)

@router.message(Income.continueadd_income)
async def continueadd_income(message:Message,state:FSMContext):
    if message.text == "✅ Да, добавить ещё":
        await add_income_handler(message,state)
    elif message.text == "❌ Нет, завершить":
        await message.answer("Возвращаюсь на главное меню!",reply_markup=main_menu_kb())
        await state.clear()