from aiogram import Bot
from dotenv import load_dotenv
from os import getenv
load_dotenv()


bot = Bot(
    getenv("TG_BOT_TOKEN")
)
