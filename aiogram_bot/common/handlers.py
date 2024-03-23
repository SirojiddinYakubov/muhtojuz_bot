from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _
from application.keyboards.applicant_kb import get_applicant_kb

common_router = Router(name=__name__)


@common_router.message(CommandStart())
async def message_handler(message: Message) -> Message:
    await message.answer(_('Assalomu aleykum!'), reply_markup=await get_applicant_kb())