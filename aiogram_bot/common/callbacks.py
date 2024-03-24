from aiogram.filters.callback_data import CallbackData

class InlineQueryFactory(CallbackData, prefix="inline_query"):
    action: str
    value: str | None = None