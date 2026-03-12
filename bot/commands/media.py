from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.handlers import handle_paid_media

router: Router = Router(name=__name__)


@router.message(Command("media"))
async def process_media(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send paid media with a specified Stars price."""
    await handle_paid_media(message, bot, i18n)
