import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

#Start text 

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

@Peaky.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    buttons = [[
        InlineKeyboardButton('🔰 𝙹𝙾𝙸𝙽', url="https://t.me/cinemazilla"),
        InlineKeyboardButton('👨‍💻 𝙲𝚁𝙴𝙰𝚃𝙾𝚁', url="https://t.me/peaky_blinder_tg")
    ],[
        InlineKeyboardButton('💡 𝙷𝙴𝙻𝙿', callback_data="help"),
        InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data="close")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await message.reply_photo("https://telegra.ph/file/81a2435b00d1d77d511f1.jpg",)
        caption=START_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

#now set call back 

@Client.on_callback_query(filters.regex(r"^(start|help|about|close)$"), group=2)
async def callback_data(bot, update: CallbackQuery):

    query_data = update.data

    if query_data == "start":
        buttons = [[
            InlineKeyboardButton('My Dev 👨‍🔬', url='https://t.me/AlbertEinstein_TG'),
            InlineKeyboardButton('Source Code 🧾', url ='https://github.com/CrazyBotsz/Adv-Filter-Bot-V2')
        ],[
            InlineKeyboardButton('Support 🛠', url='https://t.me/CrazyBotszGrp')
        ],[
            InlineKeyboardButton('Help ⚙', callback_data="help")
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            START_TEXT.format(update.from_user.mention),
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "help":
        buttons = [[
            InlineKeyboardButton('Home ⚡', callback_data='start'),
            InlineKeyboardButton('About 🚩', callback_data='about')
        ],[
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
    
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            HELP_TEXT,
            reply_markup=reply_markup,
            parse_mode="html",
            disable_web_page_preview=True
        )


    elif query_data == "about": 
        buttons = [[
            InlineKeyboardButton('Home ⚡', callback_data='start'),
            InlineKeyboardButton('Close 🔐', callback_data='close')
        ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        
        await update.message.edit_text(
            ABOUT_TEXT,
            reply_markup=reply_markup,
            parse_mode="html"
        )


    elif query_data == "close":
        await update.message.delete()
Peaky.run()
