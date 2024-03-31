import uuid

from aiogram import Bot, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandObject, CommandStart
from aiogram.handlers import InlineQueryHandler
from aiogram.types import *

from application.utils import get_application_by_id, generate_progress_message
from common.keyboards import share_inline_query_keyboard

common_router = Router(name=__name__)


@common_router.message(CommandStart())
async def message_handler(
        message: Message, bot: Bot, command: CommandObject
) -> Message:
    print("salom")
    args = command.args

    await message.answer(f"Your payload: {args}")
    await bot.send_message(args, f"Siz {message.from_user.username}ni taklif etdingiz")


@common_router.inline_query()
class ShareDiseaseInlineQueryHandler(InlineQueryHandler):
    async def handle(self):
        application_id = int(self.query) or None
        if application_id:
            application = await get_application_by_id(application_id)
            if application:
                title = application["title"]
                description = application["description"]
                required_amount = float(
                    application["required_amount"]["amount"]
                )
                total_donations = application["total_donations"]
                need_collect = float(application["required_amount"]["amount"]) - float(application["total_donations"])
                progress_message = generate_progress_message(
                    float(application["required_amount"]["amount"]),
                    application["total_donations"]
                )

                disease_hashtags = ""
                for hashtag in application["disease_category"]:
                    disease_hashtags += f"<a href='{hashtag['wikipedia_url']}'>#{hashtag['title']}</a> "

                formatted_message = (
                    f"<b>🫂{title}</b>\n\n"
                    f"❗️{description}\n\n<b>"
                    f"🧾 Kerakli summa:</b> UZS {required_amount:0,.0f}\n"
                    f"🔀 <b>Sababi:</b> Operatsiya\n"
                    f"✅ <b>Yig'ildi:</b> UZS {total_donations:0,.0f}\n<b>"
                    f"‼️ Yig'ilishi kerak:</b> UZS {need_collect:0,.0f}\n\n"
                    f"{progress_message}\n\n"
                    f"‼️<b>Yordam faqat moddiy(pul) bilan emas. Do'stlaringizga ulashish ham yordamdir.</b> \n\n"
                    f"<b>{disease_hashtags}</b>"
                )

                description = (
                    (
                        "🧾 Kerak: UZS {required_amount:0,.0f}\n"
                        "✅ Yig'ildi: UZS {total_donations:0,.0f}").format(
                        required_amount=float(
                            application["required_amount"]["amount"]
                        ),
                        total_donations=application["total_donations"],
                    )
                )

                result = InlineQueryResultPhoto(
                    id=str(uuid.uuid4()),
                    title=f"ID: {application['id']} | {application['patient']['first_name'].capitalize()} {application['patient']['last_name'].capitalize()}",
                    description=description,
                    photo_url=application['image'],
                    thumbnail_url=application['image'],
                    caption=formatted_message,
                    parse_mode=ParseMode.HTML,
                    photo_width=1200,
                    photo_height=1200,
                    photo_size=200,
                    reply_markup=await share_inline_query_keyboard(application['id'])
                )
                return await self.event.answer(results=[result], cache_time=1)
