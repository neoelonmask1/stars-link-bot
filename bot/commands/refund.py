from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.handlers import handle_refund

router: Router = Router(name=__name__)


@router.message(Command("refund"))
async def process_refund(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """
    Process refund request.

    Supports:
    - `/refund <user_id> <transaction_id>` - Refund a specific payment
    - `/refund <user_id>` - Batch refund all transactions for user
    """
    await handle_refund(message, bot, i18n)
