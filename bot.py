import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

#Start text 
STICKER = "CAACAgIAAxkBAAM4YVp_n045x2s8rk8EaT3veA6PD50AAtgOAAJsrLhLfHTEmxtg9YgeBA"

HELP_TEXT ="""𝙷𝙴𝙻𝙿𝙸𝙻 𝙾𝙽𝚄𝙼𝙸𝙻𝙻𝙻𝙰"""
START_TEXT = """𝙷𝙴𝚈 𝙸𝙰𝙼 𝙹𝚄𝚂𝚃 𝙰 𝚃𝙴𝚂𝚃 𝙱𝙾𝚃 """
ABOUT_TEXT = """𝙻𝙸𝚂𝚂𝙰 𝙱𝙾𝚃"""
Peaky = Client(
   "Test bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Peaky.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=HELP_TEXT,
        parse_mode="html",
    )
START_TEXT = "HEY BRUHH HOW ARE YOUUU"

@Peaky.on_message(filters.text)
async def wasim(bot, message):
    if not message.text.startswith("wasim"):
        return
    await bot.send_message(
        text=START_TEXT,
        parse_mode="html",
    )
Peaky.run()
