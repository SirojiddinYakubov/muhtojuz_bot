from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

async def get_applicant_kb():
   
    kb = [
        [
            KeyboardButton(text="Ariza topshirish")
        ],
        
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)