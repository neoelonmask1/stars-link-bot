import logging

from aiogram import Bot
from aiogram.enums import ChatAction
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message
from aiogram_i18n import I18nContext

from bot.utils import (
    extract_charge_id,
    extract_user_id,
    get_error_message,
    parse_refund_command,
)

logger = logging.getLogger(__name__)


async def _refund_charge(bot: Bot, user_id: int, charge_id: str) -> bool:
    """Attempt to refund a single charge, returns False and logs error on failure."""
    try:
        return await bot.refund_star_payment(
            user_id=user_id,
            telegram_payment_charge_id=charge_id,
        )
    except TelegramAPIError as exc:
        logger.debug(f"Refund failed for charge {charge_id}: {exc}")
        return False


async def handle_refund(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """
    Handle refund request.

    Modes:
    - `/refund <user_id> <transaction_id>` → Refund specific payment
    - `/refund <user_id>` → Batch refund all transactions for user
    """
    text: str = message.text or ""
    user_id, transaction_id = parse_refund_command(text)

    if user_id is None:
        await message.reply(i18n.get("refund-invalid"))
        return

    # Mode 1: Specific transaction refund
    if transaction_id:
        await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        try:
            result: bool = await bot.refund_star_payment(
                user_id=user_id,
                telegram_payment_charge_id=transaction_id,
            )
            if result:
                await message.reply(i18n.get("refund-success"))
            else:
                await message.reply(i18n.get("refund-error", error="Unknown error"))
        except TelegramAPIError as exc:
            await message.reply(
                get_error_message(i18n, str(exc), user_id, transaction_id)
            )
        return

    # Mode 2: Batch refund all transactions for user
    stats: dict[str, int] = {"scanned": 0, "refunded": 0, "skipped": 0, "failed": 0}
    seen_charge_ids: set[str] = set()
    offset: int = 0
    limit: int = 100

    await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

    try:
        while True:
            result = await bot.get_star_transactions(offset=offset, limit=limit)
            transactions = result.transactions

            if not transactions:
                break

            for tx in transactions:
                stats["scanned"] += 1

                if extract_user_id(tx) != user_id:
                    stats["skipped"] += 1
                    continue

                charge_id = extract_charge_id(tx)
                if not charge_id:
                    stats["skipped"] += 1
                    continue

                # Skip duplicates (same charge_id can appear across pages)
                if charge_id in seen_charge_ids:
                    stats["skipped"] += 1
                    continue
                seen_charge_ids.add(charge_id)

                if await _refund_charge(bot, user_id, charge_id):
                    stats["refunded"] += 1
                else:
                    stats["failed"] += 1

            if len(transactions) < limit:
                break
            offset += len(transactions)

            await bot.send_chat_action(
                chat_id=message.chat.id, action=ChatAction.TYPING
            )

    except TelegramAPIError as exc:
        await message.reply(i18n.get("refund-transactions-error", error=str(exc)))
        return

    await message.reply(
        i18n.get(
            "refund-transactions-summary",
            user_id=str(user_id),
            scanned=stats["scanned"],
            refunded=stats["refunded"],
            skipped=stats["skipped"],
            failed=stats["failed"],
        )
    )
