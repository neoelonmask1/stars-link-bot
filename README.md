# TopPromptBot - Telegram Stars MVP

A clean, production-ready Telegram bot for selling digital content (links, files, text) via **Telegram Stars (XTR)**.

## Features
- ✅ **Native Stars Payment**: Zero third-party providers, uses `currency="XTR"`.
- ✅ **Flexible Delivery**: Support for links, plain text (keys/codes), and files.
- ✅ **Clean Code**: No dead features, focused entirely on the payment -> delivery flow.
- ✅ **Production Ready**: Env-based config, error logging, and simple deployment.

## Quick Start

### 1. Setup Environment
Create a `.env` file:
```env
BOT_TOKEN=вашь_токен_из_botfather
STARTUP_NAME=TopPromptBot
```

### 2. Configure Products
Edit `bot/core/config.py`. Add your products to the `PRODUCTS` dictionary:
```python
"my_product": {
    "title": "Cool Guide",
    "price": 50,
    "delivery_type": "links", # or "file", "text"
    "content": ["https://example.com"] # or "file/path.pdf" or "Secret Key"
}
```

### 3. Run Locally
```bash
pip install -r requirements.txt
python main.py
```

## Deployment
This bot is ready for **Railway**, **Render**, or **VPS**.
- **Railway/Render**: Just connect the repo. It uses the included `Procfile`.
- **VPS**: Use `systemd` to run `python main.py`.

## Files
- `main.py`: Entry point.
- `bot/core/config.py`: Product catalog and settings.
- `bot/commands/payment.py`: Stars payment and delivery logic.
- `locales/en/messages.ftl`: UI text and templates.

---
Built with ❤️ using aiogram 3.x
