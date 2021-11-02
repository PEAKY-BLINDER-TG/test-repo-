import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

APP_ID = "3637235"
API_HASH = "028885dcbc64a4b56c47bdad0367523b"
TG_BOT_TOKEN = "2019246874:AAEJe65zFbHqO46lsrHhb_JgskbkUK3-BzQ"

Bot = Client(
   "Test bot",
   api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=TG_BOT_TOKEN,
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )

Bot.run()
