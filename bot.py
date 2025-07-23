# Main entry point for the bot.
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import API_BOT_TOKEN, DEBUG
from handlers import user_commands, callbacks
from utils.data import BotData
from services.sd_api import SdApi
from services.scripts import Scripts

async def main():
    """Initializes and runs the bot."""
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG if DEBUG else logging.INFO,
        format="[%(asctime)s] %(levelname)s : %(name)s : %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
    )

    # Initialize Bot and Dispatcher
    bot = Bot(token=API_BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Initialize BotData
    bot_data = BotData(prompts_file='configs/prompts.json', presets_file='configs/presets.json')
    dp['bot_data'] = bot_data

    # Initialize SdApi and Scripts
    sd_api = SdApi()
    scripts = Scripts(bot, sd_api, bot_data)
    dp['scripts'] = scripts

    # Include routers
    dp.include_router(user_commands.router)
    dp.include_router(callbacks.router)

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
