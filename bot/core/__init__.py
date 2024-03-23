from aiogram import Bot, Dispatcher
from bot.core.config import settings
from bot.common.handlers import common_router

bot = Bot(token=settings.TOKEN_API, parse_mode="HTML")
dp = Dispatcher()

dp.include_routers(common_router)
