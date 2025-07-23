from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_bot_commands(bot: Bot):
    """
    Sets the bot's commands.
    """
    commands = [
        BotCommand(command="start", description="Welcome message and main menu"),
        BotCommand(command="help", description="Detailed help message"),
        BotCommand(command="gen", description="Generate an image with current settings"),
        BotCommand(command="gen_custom", description="Generate an image with custom settings"),
        BotCommand(command="skip", description="Skip the current image generation"),
        BotCommand(command="stop", description="Stop a running script"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())