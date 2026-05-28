from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram_i18n import I18nContext
from bot.core.config import config

router: Router = Router(name=__name__)

@router.message(Command("start"))
async def start_intro(message: Message, i18n: I18nContext) -> None:
    buttons = []
    for key, prod in config.PRODUCTS.items():
        text = f"{prod['title']} ({prod['price']} ⭐)"
        buttons.append([InlineKeyboardButton(text=text, callback_data=f"buy_{key}")])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    
    await message.answer(
        i18n.get("start", startup_name=config.STARTUP_NAME),
        reply_markup=keyboard,
        parse_mode="HTML"
    )
