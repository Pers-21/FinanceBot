import asyncio
import logging
from aiogram import Bot,Dispatcher
from config import TOKEN
from handlers import start,expenses,income,stats 
from Settings import settings
from services.database import init_db  


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s", 
)

logger = logging.getLogger(__name__)  



async def on_startup():
    await init_db()  

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.startup.register(on_startup)


dp.include_router(start.router)
dp.include_router(expenses.router)
dp.include_router(income.router)
dp.include_router(stats.router)
dp.include_router(settings.router)



async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())


