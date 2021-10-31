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
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Peaky.on_message(filters.command(["start"]))
async def start(bot, message):
 chat_id = str(message.chat.id)
 await bot.send_sticker(chat_id,"CAACAgIAAxkBAAIpI2F3krsxKAngOW664GuE00UwYGSRAAJ6DQAC0YlwSCgyxmI0r89BHgQ")
 reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton('🕵‍♂ ᴄʀᴇᴀᴛᴏʀ', url='https://t.me/no_ones_like_me'),
            InlineKeyboardButton('⚠️ ᴊᴏɪɴ', url ='https://t.me/SSM_Chat')
        ],[
            InlineKeyboardButton('🎬 ᴄʜᴀɴɴᴇʟ', url='https://t.me/SevenScreenMovie')
        ],[
            InlineKeyboardButton('Help ⚙', callback_data="help")
        ]])

Peaky.run()
