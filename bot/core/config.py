import logging
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

logger: logging.Logger = logging.getLogger(__name__)

class Config:
    def __init__(self) -> None:
        env_path: Path = Path(__file__).resolve().parents[2] / ".env"
        load_dotenv(env_path)

        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        if not self.BOT_TOKEN:
            logger.error("Missing BOT_TOKEN in .env")
            sys.exit(1)

        self.STARTUP_NAME = os.getenv("STARTUP_NAME", "TopPromptBot")
        
        # Delivery Types: 'links', 'file', 'text'
        self.PRODUCTS = {
            "chatgpt": {
                "title": "Ultimate ChatGPT Prompt Library",
                "price": 49,
                "old_price": 99,
                "delivery_type": "links",
                "content": [
                    "https://www.aiprm.com/",
                    "https://prompts.chat/"
                ]
            },
            "midjourney": {
                "title": "Midjourney Mega Prompt Pack",
                "price": 74,
                "old_price": 149,
                "delivery_type": "text",
                "content": "Your Midjourney Premium Key: MJ-PRO-2026-X99"
            },
            "creator": {
                "title": "AI Creator Toolkit",
                "price": 99,
                "old_price": 199,
                "delivery_type": "file",
                "content": "files/stars.svg"  # Example file path
            }
        }

config: Config = Config()
