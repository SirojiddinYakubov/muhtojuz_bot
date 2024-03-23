from aiogram import Bot, Dispatcher
from core.config import settings
from common.handlers import common_router

bot = Bot(token=settings.TOKEN_API, parse_mode="HTML")
dp = Dispatcher()

dp.include_routers(common_router)
