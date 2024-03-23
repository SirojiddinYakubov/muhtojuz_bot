from aiogram import Dispatcher, types
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from typing import Dict, Any, Optional
from babel import Locale
from aiogram.types import TelegramObject
from core.config import BASE_DIR


i18n = I18n(path=BASE_DIR / "locales", default_locale="uz", domain="messages")


class Localization(SimpleI18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        if Locale is None:  # pragma: no cover
            raise RuntimeError(
                f"{type(self).__name__} can be used only when Babel installed\n"
                "Just install Babel (`pip install Babel`) "
                "or aiogram with i18n support (`pip install aiogram[i18n]`)"
            )
        event_from_user: Optional[types.User] = data.get("event_from_user", None)
        if event_from_user is None:
            return "ru"
        return "ru"


i18n_middleware = Localization(i18n=i18n)


def register_middlewares(dp: Dispatcher):
    dp.update.outer_middleware(i18n_middleware)
