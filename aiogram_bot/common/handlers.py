import uuid

from aiogram import Bot, Router
from aiogram.filters import CommandObject, CommandStart
from aiogram.handlers import InlineQueryHandler
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from aiogram.types.inline_query_results_button import InlineQueryResultsButton
from aiogram.types.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
from aiogram.utils.deep_linking import create_start_link
from application.utils import get_application_by_id
from common.callbacks import InlineQueryFactory

common_router = Router(name=__name__)


@common_router.message(CommandStart())
async def message_handler(
    message: Message, bot: Bot, command: CommandObject
) -> Message:
    print("salom")
    args = command.args

    await message.answer(f"Your payload: {args}")
    await bot.send_message(args, f"Siz {message.from_user.username}ni taklif etdingiz")

    # await message.answer(_("Assalomu aleykum!"), reply_markup=await get_applicant_kb())


@common_router.inline_query()
class MyInlineQueryHandler(InlineQueryHandler):
    async def handle(self):
        application_id = self.query or ""
        if application_id:
            application = await get_application_by_id(application_id)
            if application:
                text = f"Application: {application['patient']['first_name'].capitalize()} {application['patient']['last_name'].capitalize()}"
                item = InputTextMessageContent(
                    message_text=text,
                )
                description = """🧾 Kerakli summa: UZS 175,000,000\n
🔀 Sababi: Ilik ko'chirish operatsiyasi uchun\n
✅ Yig'ildi: UZS 75,000,000\n
‼️ Yig'ilishi kerak: UZS 100,000,000"""
                print(application["image"])
                result = InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title=text,
                    description=description,
                    thumbnail_url="https://0e75-93-170-220-216.ngrok-free.app/media/upload/applications/images/photo_2024-03-24_10-39-41_LEjf2g8.jpg",
                    input_message_content=item,
                )
                return await self.event.answer(results=[result], cache_time=60)

        item = InputTextMessageContent(
            message_text="Ariza yaratish InputTextMessageContent",
        )

        result = InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Ariza yaratish",
            input_message_content=item,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="Ariza yaratish",
                            callback_data=InlineQueryFactory(
                                action="call", value="create"
                            ).pack(),
                            switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
                                allow_user_chats=True, allow_group_chats=True
                            ),
                        )
                    ]
                ]
            ),
        )

        # link = await create_start_link(self.bot, user_id, encode=True)

        button = InlineQueryResultsButton(
            text="Ariza yaratish btn", start_parameter=str(self.event.from_user.id)
        )
        # await self.bot.send_message()
        await self.event.answer(
            results=[result],
            cache_time=60,
            button=button,
        )


# @common_router.callback_query(InlineQueryFactory.filter(F.action == "call"))
# async def inline_query_handler(
#     callback: types.CallbackQuery,
#     callback_data: InlineQueryFactory,
# ):
#     print(callback_data)
#     print(callback)
#     await callback.bot.send_invoice(
#         chat_id=callback.from_user.id,
#         title="Ariza yaratish",
#         description="Ariza yaratish",
#         payload="create",
#         provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
#         currency="UZS",
#         prices=[types.LabeledPrice(label="Ariza yaratish", amount=100000)],
#         # provider_data="test",
#         start_parameter="test",
#         photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg/1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg",
#         photo_size=100,
#         photo_width=100,
#         photo_height=100,
#         # need_name=True,
#         # need_phone_number=True,
#         # need_shipping_address=True,
#         # send_phone_number_to_provider=True,
#         # send_email_to_provider=True,
#         # is_flexible=False,
#         # disable_notification=False,
#         # protect_content=False,
#         # reply_to_message_id=callback.message.message_id,
#         # allow_sending_without_reply=False,
#     )
#     # await callback.message.answer("Ariza yaratildi!")
#     await callback.answer()
