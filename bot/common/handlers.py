from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

common_router = Router(name=__name__)


@common_router.message(CommandStart())
async def message_handler(message: Message) -> Message:
    await message.answer('Hello from my router!')