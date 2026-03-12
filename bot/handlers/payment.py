from aiogram import Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message, LabeledPrice
from aiogram_i18n import I18nContext


async def handle_pay(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Validate /pay amount and send a Stars invoice or payment link."""
    text: str = message.text or ""
    parts: list[str] = text.split()

    if len(parts) != 2:
        await message.reply(i18n.get("amount-invalid"))
        return

    try:
        amount: int = int(parts[1])
    except ValueError:
        await message.reply(i18n.get("amount-invalid"))
        return

    if not (1 <= amount <= 100000):
        await message.reply(i18n.get("amount-invalid"))
        return

    try:
        await bot.send_invoice(
            chat_id=message.chat.id,
            title=i18n.get("invoice-title"),
            description=i18n.get("invoice-description"),
            provider_token="",  # Empty for Stars
            currency="XTR",  # Stars currency code
            prices=[LabeledPrice(label=i18n.get("invoice-label"), amount=amount)],
            start_parameter="stars-payment",
            payload=f"stars-payment-{amount}",
        )

        # Alternative: create a payment link instead of a direct invoice
        # try:
        #     invoice_link: str = await bot.create_invoice_link(
        #         title=i18n.get("invoice-title"),
        #         description=i18n.get("invoice-description"),
        #         payload=f"stars-payment-{amount}",
        #         provider_token="",  # Empty for Stars
        #         currency="XTR",
        #         prices=[LabeledPrice(label=i18n.get("invoice-label"), amount=amount)],
        #     )
        #     await message.answer(i18n.get("payment-link", link=invoice_link))
        # except TelegramAPIError:
        #     pass

    except TelegramAPIError as exc:
        await message.reply(i18n.get("invoice-error", error=str(exc)))
