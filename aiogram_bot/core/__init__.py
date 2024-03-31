from aiogram import Bot, Dispatcher
from core.config import settings
from common.handlers import common_router

print(settings.TOKEN_API)
bot = Bot(
    token=settings.TOKEN_API.get_secret_value(),
    parse_mode="HTML"
)

dp = Dispatcher()

dp.include_routers(common_router)
