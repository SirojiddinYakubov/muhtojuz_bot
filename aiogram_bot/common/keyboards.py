from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, SwitchInlineQueryChosenChat


async def share_inline_query_keyboard(application_id):
    InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='💶 Ehson qilish',
                    url='http://pay.muhtoj.uz/1/'
                ),
                InlineKeyboardButton(
                    text="⤴️ Ulashish",
                    switch_inline_query_chosen_chat=SwitchInlineQueryChosenChat(
                        query=str(
                            application_id
                        ),
                        allow_user_chats=True,
                        allow_group_chats=True,
                        allow_channel_chats=True)
                )
            ],
            [
                InlineKeyboardButton(
                    text='📋 Hisobot',
                    callback_data='report'
                ),
                InlineKeyboardButton(
                    text='📞 Aloqa',
                    callback_data='call'
                )
            ],

            # [random.choice(
            #     [
            #         InlineKeyboardButton(text="♻️️ REKLAMA | Medanta - Ko'zoynakdan xalos bo'ling",
            #                              url="https://t.me/MedantaBukhara"),
            #         InlineKeyboardButton(
            #             text="♻️️ REKLAMA | Dasturlash kurslari", url="https://t.me/geeks_tashkent"),
            #         InlineKeyboardButton(text="♻️️ REKLAMA | Best Motors - yuk avtomobillari",
            #                              url="http://t.me/Bestmotors_uz")
            #     ],
            # )]

        ]
    )
