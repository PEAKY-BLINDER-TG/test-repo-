import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

APP_ID = "3637235"
API_HASH = "028885dcbc64a4b56c47bdad0367523b"
TG_BOT_TOKEN = "2019246874:AAEJe65zFbHqO46lsrHhb_JgskbkUK3-BzQ"

START_TEXT = "hey bruhh"


Bot = Client(
   "Test bot",
   api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=TG_BOT_TOKEN,
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/5865e51742e0f813805a8.jpg",
        caption=f"""<b>Hᴇʏ {update.from_user.mention},
എന്നെ <a href="tg://settings">നിന്റെ</a> ഗ്രൂപ്പിൽ വേണമെങ്കിൽ ആഡ് ചെയാം ¡
𝙼𝙰𝙸𝙽𝚃𝙰𝙸𝙽𝙴𝙳 𝙱𝚈 <a href="https://t.me/Joel_tg">𝚃𝙷𝙸𝚂 𝙱𝙾𝚈</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ Add Me To Your Group ➕", url="t.me/sakura_x_bot?startgroup=true"),
                ],[
                    InlineKeyboardButton("🕵‍♂ Creator", callback_data="devs"),
                    InlineKeyboardButton("⚠️ Group", url="https://t.me/cv_group1"),
                ],[
                    InlineKeyboardButton("💡 Help", callback_data="home"),
                    InlineKeyboardButton("😃 About", callback_data="about"),
                ]
            ]
        ),
    )

Bot.run()
