from aiogram import Bot
from aiogram.types import InputPaidMediaPhoto, Message, ReplyParameters
from aiogram_i18n import I18nContext


def _extract_photo_file_id(message: Message) -> str | None:
    """Get photo file_id from a message or replied photo."""
    if message.photo:
        return message.photo[-1].file_id
    if message.reply_to_message and message.reply_to_message.photo:
        return message.reply_to_message.photo[-1].file_id
    return None


async def handle_paid_media(message: Message, bot: Bot, i18n: I18nContext) -> None:
    """Send paid media with a specified Stars price."""
    photo_file_id: str | None = _extract_photo_file_id(message)
    text: str = message.text or message.caption or ""
    parts: list[str] = text.split()

    if not photo_file_id or len(parts) != 2:
        await message.reply(i18n.get("media-invalid"))
        return

    try:
        star_count: int = int(parts[1])
    except ValueError:
        await message.reply(i18n.get("media-invalid"))
        return

    if not (1 <= star_count <= 25000):
        await message.reply(i18n.get("media-invalid"))
        return

    caption: str = i18n.get("media-caption")
    await bot.send_paid_media(
        chat_id=message.chat.id,
        star_count=star_count,
        media=[InputPaidMediaPhoto(media=photo_file_id, caption=caption)],
        reply_parameters=ReplyParameters(message_id=message.message_id),
    )
