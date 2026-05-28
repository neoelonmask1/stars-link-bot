import logging
from aiogram import Bot, F, Router, html, types
from aiogram.types import Message, PreCheckoutQuery, LabeledPrice, CallbackQuery, FSInputFile
from aiogram_i18n import I18nContext
from bot.core.config import config

router: Router = Router(name=__name__)
logger = logging.getLogger(__name__)

@router.callback_query(F.data.startswith("buy_"))
async def process_buy_callback(callback: CallbackQuery, bot: Bot, i18n: I18nContext):
    product_key = callback.data.split("_")[1]
    product = config.PRODUCTS.get(product_key)
    
    if not product:
        await callback.answer("Product not found", show_alert=True)
        return

    try:
        await bot.send_invoice(
            chat_id=callback.message.chat.id,
            title=product['title'],
            description=i18n.get("invoice-description", title=product['title']),
            provider_token="",
            currency="XTR",
            prices=[LabeledPrice(label=i18n.get("invoice-label", price=product['price']), amount=product['price'])],
            payload=f"prod_{product_key}",
            start_parameter=f"buy_{product_key}"
        )
        await callback.answer()
    except Exception as e:
        logger.error(f"Invoice error: {e}")
        await callback.answer("Error creating invoice", show_alert=True)

@router.pre_checkout_query()
async def handle_pre_checkout(pre_checkout_query: PreCheckoutQuery, bot: Bot) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@router.message(F.successful_payment)
async def handle_successful_payment(message: Message, bot: Bot, i18n: I18nContext) -> None:
    info = message.successful_payment
    payload = info.invoice_payload
    
    product_key = payload.replace("prod_", "")
    product = config.PRODUCTS.get(product_key)
    
    if not product:
        await message.reply("Internal error: Product not found after payment.")
        return

    delivery_type = product.get("delivery_type", "links")
    content = product.get("content")
    
    delivery_message = ""
    if delivery_type == "links":
        links_text = "\n".join([f"• {link}" for link in content])
        delivery_message = i18n.get("delivery-links", content=links_text)
    elif delivery_type == "text":
        delivery_message = i18n.get("delivery-text", content=content)
    elif delivery_type == "file":
        delivery_message = i18n.get("delivery-file")

    # Log payment
    logger.info(f"PAYMENT_SUCCESS: user={message.from_user.id} product={product_key} stars={info.total_amount}")

    # Send success message
    await message.answer(
        i18n.get(
            "payment-success",
            startup_name=config.STARTUP_NAME,
            delivery_message=delivery_message,
            transaction_id=html.quote(info.telegram_payment_charge_id),
        ),
        parse_mode="HTML"
    )

    # If file delivery, send the file
    if delivery_type == "file":
        try:
            file = FSInputFile(content)
            await bot.send_document(chat_id=message.chat.id, document=file)
        except Exception as e:
            logger.error(f"File delivery error: {e}")
            await message.answer("Error delivering file. Please contact support.")
