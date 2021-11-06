import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

APP_ID = "3637235"
API_HASH = "028885dcbc64a4b56c47bdad0367523b"
TG_BOT_TOKEN = "2019246874:AAEJe65zFbHqO46lsrHhb_JgskbkUK3-BzQ"

START_TEXT = "hey bruhh"

print("wait")

wasim = Client(
   "Test bot",
   api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=TG_BOT_TOKEN,
)
print("bot started")
wasim.run()
