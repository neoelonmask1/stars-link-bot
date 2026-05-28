import logging
import os
from pathlib import Path
from dotenv import load_dotenv

logger: logging.Logger = logging.getLogger(__name__)

class Config:
    def __init__(self) -> None:
        # Load .env if it exists, but don't fail if it doesn't (Railway uses direct env vars)
        env_path: Path = Path(__file__).resolve().parents[2] / ".env"
        if env_path.exists():
            load_dotenv(env_path)

        self.BOT_TOKEN = os.getenv("BOT_TOKEN")
        if not self.BOT_TOKEN:
            # If we're in a real environment, we should log but not necessarily exit 1 
            # if we want to see logs in Railway first.
            logger.error("CRITICAL: BOT_TOKEN not found in environment variables!")
            # Note: Railway might crash if we exit here, but it's better than running without token.

        self.STARTUP_NAME = os.getenv("STARTUP_NAME", "TopPromptBot")
        
        self.PRODUCTS = {
            "chatgpt": {
                "title": "Ultimate ChatGPT Prompt Library",
                "price": 99,
                "delivery_type": "links",
                "content": [
                    "https://www.aiprm.com/",
                    "https://www.aiprm.com/prompts/",
                    "https://www.aiprm.com/en-gb/prompts/",
                    "https://prompts.chat/",
                    "https://github.com/bigscience-workshop/promptsource"
                ]
            },
            "midjourney": {
                "title": "Midjourney Mega Prompt Pack",
                "price": 149,
                "delivery_type": "links",
                "content": [
                    "https://prompthero.com/",
                    "https://promptbase.com/",
                    "https://www.aipromptlibrary.app/vs/prompthero"
                ]
            },
            "creator": {
                "title": "AI Creator Toolkit",
                "price": 199,
                "delivery_type": "links",
                "content": [
                    "https://flowgpt.com/",
                    "https://prompts.chat/",
                    "https://www.aiprm.com/"
                ]
            },
            "seo": {
                "title": "SEO + Marketing Prompt Vault",
                "price": 249,
                "delivery_type": "links",
                "content": [
                    "https://www.aiprm.com/prompts/",
                    "https://www.aiprm.com/",
                    "https://flowgpt.com/"
                ]
            },
            "research": {
                "title": "Prompt Engineering Research Pack 2026",
                "price": 299,
                "delivery_type": "links",
                "content": [
                    "https://promptflow.digital/prompts",
                    "https://www.reddit.com/r/PromptEngineering/comments/1sjgwd1/i_organized_200_prompts_by_use_case_into_a_free/",
                    "https://www.reddit.com/r/PromptEngineering/comments/1s9n81b/i_tested_500_ai_prompts_across_10_categories_here/",
                    "https://www.reddit.com/r/PromptEngineering/comments/1sglnor/i_tested_120_claude_prompt_patterns_over_3_months/",
                    "https://www.reddit.com/r/PromptCentral/comments/1rkqu0w/i_tested_600_ai_prompts_across_12_categories_over/"
                ]
            }
        }

config: Config = Config()
