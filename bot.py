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

@Client.on_message(filters.command(["start"]))
async def start(Peaky, message):
    await Peaky.reply_sticker("CAACAgIAAxkBAAM4YVp_n045x2s8rk8EaT3veA6PD50AAtgOAAJsrLhLfHTEmxtg9YgeBA"),
    userid = message.from_user.id
    chat_type = message.chat.type
    

#now set call back 

@Client.on_callback_query(filters.regex(r"^(start|help|about|close|about_alert)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
            InlineKeyboardButton('🕵‍♂ ᴄʀᴇᴀᴛᴏʀ', url='https://t.me/no_ones_like_me'),
            InlineKeyboardButton('⚠️ ᴊᴏɪɴ', url ='https://t.me/SSM_Chat')
        ],[
            InlineKeyboardButton('🎬 ᴄʜᴀɴɴᴇʟ', url='https://t.me/SevenScreenMovie')
        ],[
            InlineKeyboardButton('Help ⚙', callback_data="help")
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.START_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    if query_data == "help":
        buttons = [[
            InlineKeyboardButton('𝗵𝗼𝗺𝗲 ⚡', callback_data='start'),
            InlineKeyboardButton('𝗮𝗯𝗼𝘂𝘁 🚩', callback_data='about_alert')
        ],[
            InlineKeyboardButton('𝗰𝗹𝗼𝘀𝗲 🔐', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.HELP_TEXT,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    if query_data == "about": 
        buttons = [[
            InlineKeyboardButton('𝗵𝗼𝗺𝗲 ⚡', callback_data='start'),
            InlineKeyboardButton('𝗰𝗹𝗼𝘀𝗲 🔐', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            Translation.ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    if query_data == "close":
        await update.message.delete()

    if query_data == "about_alert":
        await update.answer("hi broooo", show_alert=True)
Peaky.run()
