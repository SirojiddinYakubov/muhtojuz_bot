import random
import uuid

from aiogram import Bot, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandObject, CommandStart
from aiogram.handlers import InlineQueryHandler
from aiogram.types import *
# (
#
#     # InlineKeyboardButton,
#     # InlineKeyboardMarkup,
#     # InlineQueryResultArticle,
#     # InputTextMessageContent,
#     # Message,
# )
from aiogram.types.inline_query_results_button import InlineQueryResultsButton
from aiogram.types.switch_inline_query_chosen_chat import SwitchInlineQueryChosenChat
from aiogram.utils.deep_linking import create_start_link
from application.utils import get_application_by_id, generate_progress_message
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
                text = '2222222222'
                # item = InputTextMessageContent(
                #     message_text="""🫂{title}\n\n❗️{description} <a href="https://telegra.ph/">Batafsil o'qish</a>\n\n🧾 Kerakli summa: UZS {required_amount:0,.0f}\n🔀 Sababi: {reason}\n✅ Yig'ildi: UZS {total_donations:0,.0f}\n‼️ Yig'ilishi kerak: UZS {need_collect:0,.0f}\n\n{progress_message}\n\n#Leykoz #Oqqon
                #                                     """.format(
                #         title=application["title"],
                #         description=application["description"],
                #         required_amount=float(application["required_amount"]["amount"]),
                #         # reason=dieses,
                #         total_donations=application["total_donations"],
                #         need_collect=float(application["required_amount"]["amount"]) - float(
                #             application["total_donations"]),
                #         progress_message=generate_progress_message(
                #             float(application["required_amount"]["amount"]), application["total_donations"]
                #         )
                #     ),
                # )
                # Ma'lumotlarni kiritish
                title = application["title"]
                description = application["description"]
                required_amount = float(application["required_amount"]["amount"])
                # reason = application["disease_category"]["title"]
                total_donations = application["total_donations"]
                need_collect = float(application["required_amount"]["amount"]) - float(application["total_donations"])
                progress_message = generate_progress_message(float(application["required_amount"]["amount"]),
                                                             application["total_donations"])

                # Stringni formatlash
                dieses_hashtags = ""
                for hashtag in application["disease_category"]:
                    print(hashtag)
                    dieses_hashtags += f"<a href='{hashtag['wikipedia_url']}'>#{hashtag['title']}</a> "
                formatted_message = f"<b>🫂{title}</b>\n\n❗️{description}\n\n<b>🧾 Kerakli summa:</b> UZS {required_amount:0,.0f}\n🔀 <b>Sababi:</b> Operatsiya\n✅ <b>Yig'ildi:</b> UZS {total_donations:0,.0f}\n<b>‼️ Yig'ilishi kerak:</b> UZS {need_collect:0,.0f}\n\n{progress_message}\n\n<b>{dieses_hashtags}</b>"
#                 formatted_message = """<b>Success:</b>
# ✅ Test 1
# ✅ Test 3
# ✅ Test 4
#
# <b>Failed:</b>
# ❌ Test 2
#
# <b>Summary:</b>
#   <b>Total:</b> 4
#   <b>Success:</b> 3
#   <b>Failed:</b> 1
#
# #test"""
                print(formatted_message)

                # item = InputTextMessageContent(
                #
                #     # media='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg/1200px-2019_Toyota_Corolla_Icon_Tech_VVT-i_Hybrid_1.8.jpg',
                #     # parse_mode=ParseMode.HTML,
                #
                # )
                description = "🧾 Kerak: UZS {required_amount:0,.0f}\n✅ Yig'ildi: UZS {total_donations:0,.0f}".format(
                    required_amount=float(application["required_amount"]["amount"]),
                    total_donations=application["total_donations"],
                )

                # print()
                result = InlineQueryResultPhoto(
                    id=str(uuid.uuid4()),
                    title=f"ID: {application['id']} | {application['patient']['first_name'].capitalize()} {application['patient']['last_name'].capitalize()}",
                    description=description,
                    photo_url=application['image'],
                    thumbnail_url=application['image'],
                    caption=formatted_message,
                    parse_mode=ParseMode.HTML,
                    # input_message_content=item,
                    photo_width=1200,
                    photo_height=1200,
                    photo_size=200,
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=[
                            [InlineKeyboardButton(text="⤴️ Ulashish",
                                                  switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
                                                      query=str(application["id"]),
                                                      allow_user_chats=True,
                                                      allow_group_chats=True))],
                            [random.choice(
                                [
                                    InlineKeyboardButton(text="♻️️ Medanta - Ko'zoynakdan xalos bo'ling",
                                                         url="https://t.me/MedantaBukhara"),
                                    InlineKeyboardButton(text="♻️ Dasturlash kurslari", url="https://t.me/GeeksOnline"),
                                    InlineKeyboardButton(text="♻️ Best Motors - yuk avtomobillari",
                                                         url="http://t.me/Bestmotors_uz")
                                ],
                            )]

                        ]

                    )
                    # photo_url="",

                )

                return await self.event.answer(results=[result], cache_time=5)

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
