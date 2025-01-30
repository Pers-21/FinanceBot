import aiosqlite
import os
from datetime import datetime


DB_PATH = os.path.abspath("C:/Users/user/Downloads/FinanceBot/services/utils/data/finance.db")

async def init_db():
    """
    Инициализация базы данных. Создаёт таблицы, если они не существуют.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            date TEXT 
        )
        ''')
        await db.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            date TEXT 
        )
        ''')
        await db.commit()

async def add_income(user_id: int, category: str, sum_income: int):
    """
    Добавляет запись о доходе в базу данных.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        INSERT INTO incomes (user_id, category, amount,date)
        VALUES (?, ?, ?,?)
        ''', (user_id, category, sum_income,current_time))
        await db.commit()

async def add_expense(user_id: int, category: str, sum_expenses: int):
    """
    Добавляет запись о расходе в базу данных.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
        INSERT INTO expenses (user_id, category, amount,date)
        VALUES (?, ?, ?,?)
        ''', (user_id, category, sum_expenses,current_time))
        await db.commit()

async def get_incomes(user_id: int):
    """
    Возвращает список доходов пользователя, сгруппированных по категориям.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
        SELECT category, SUM(amount) FROM incomes WHERE user_id = ? GROUP BY category
        ''', (user_id,))
        return await cursor.fetchall()

async def get_expenses(user_id: int):
    """
    Возвращает список расходов пользователя, сгруппированных по категориям.
    """
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
        SELECT category, SUM(amount) FROM expenses WHERE user_id = ? GROUP BY category
        ''', (user_id,))
        return await cursor.fetchall()
    

async def detailed_incomes(user_id:int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
            SELECT category, amount, date 
            FROM incomes 
            WHERE user_id = ?
        ''', (user_id,))
        return await cursor.fetchall()
    

async def detailed_expenses(user_id:int):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('''
            SELECT category, amount, date 
            FROM expenses 
            WHERE user_id = ?
        ''', (user_id,))
        return await cursor.fetchall()
