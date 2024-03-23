from aiogram import Router
from aiogram.filters import F
from aiogram.utils.i18n import lazy_gettext as __

router = Router()

@router.message(F.text == __("Qo'shiq qo'shish ➕"), IsAdmin())
async def admin_add_music(message: types.Message, state: FSMContext):
    await state.set_state(AddMusicState.audio)
    await message.answer(_("Audio faylni yuklang!"))