from typing import Optional
from aiogram.filters.callback_data import CallbackData

class ApplyApplicationCB(CallbackData, prefix="apply_application"):
    action: str
    value: Optional[str] = None

