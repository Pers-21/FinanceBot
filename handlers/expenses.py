from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State
from keyboards.categories import categories_expenses_button
from keyboards.continue_add import continue_add
from keyboards.main_menu import main_menu_kb
from services.database import add_expense 

class Expenses(StatesGroup):
    waiting_expensens = State()
    waiting_amout = State()
    continue_expens = State()


router = Router()

@router.message(lambda message:message.text == "💸 Добавить расход")
async def add_expense_handler(message:Message,state:FSMContext):
    await message.answer("Выберите категорю или напишите свою:",reply_markup=categories_expenses_button())
    await state.set_state(Expenses.waiting_expensens)

@router.message(Expenses.waiting_expensens)
async def select_category(message:Message,state:FSMContext):
    category_text = message.text   
    await state.update_data(category=category_text)  
    await message.answer("Укажите сумму расхода")
    await state.set_state(Expenses.waiting_amout)

@router.message(Expenses.waiting_amout)
async def process_expense(message:Message,state:FSMContext,):
    user_data = await state.get_data()  
    category_text = user_data.get('category')   
    sum_expenses = message.text
    await add_expense(message.from_user.id, category_text, sum_expenses) 
    if sum_expenses.isdigit():
        await message.answer(f"Расход на {category_text}: {sum_expenses} руб. успешно добавлен!")
        await message.answer("💬 Хотите добавить ещё один расход?",reply_markup=continue_add())
        await state.set_state(Expenses.continue_expens)
    else:
        await message.answer("Пожалуйста, введите корректную сумму (только цифры).")
        await state.set_state(Expenses.waiting_amout)

@router.message(Expenses.continue_expens)
async def continueadd_exp(message:Message,state:FSMContext):
    if message.text == "✅ Да, добавить ещё":
       await add_expense_handler(message,state)
    elif message.text == "❌ Нет, завершить":
        await message.answer("Возвращаюсь на главное меню!",reply_markup=main_menu_kb())
        await state.clear()
    
      
