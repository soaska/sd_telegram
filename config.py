# This file contains all the configuration variables for the bot.
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot Token
API_BOT_TOKEN = os.getenv('API_BOT_TOKEN')

# Allowed users
try:
    ALLOWED_USERS = json.loads(os.getenv('ALLOWED_USERS', '[]'))
except (json.JSONDecodeError, TypeError):
    ALLOWED_USERS = []

# Stable Diffusion
SD_HOST = os.getenv('SD_HOST', '127.0.0.1')
SD_PORT = os.getenv('SD_PORT', '7861')
SD_USERNAME = os.getenv('SD_USERNAME')
SD_PASSWORD = os.getenv('SD_PASSWORD')
LORA_PATH = os.getenv('LORA_PATH', 'models/Lora')

# Social Media Tokens
VK_TOKEN = os.getenv('VK_TOKEN')
VK_ALBUM_ID = os.getenv('VK_ALBUM_ID')
OK_ACCESS_TOKEN = os.getenv('OK_ACCESS_TOKEN')
OK_APPLICATION_KEY = os.getenv('OK_APPLICATION_KEY')
OK_APPLICATION_SECRET_KEY = os.getenv('OK_APPLICATION_SECRET_KEY')
OK_GROUP_ID = os.getenv('OK_GROUP_ID')

# Debug
DEBUG = os.getenv('DEBUG', 'no').lower() == 'yes'