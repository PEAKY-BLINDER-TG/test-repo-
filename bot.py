import os
import logging
import asyncio
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
   "Chumma oru bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Bot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       message.reply_photo(
               photo="https://telegra.ph/file/05cfe0010e426cd556d7c.jpg",
               caption="""<b>Hey There, I'm test bot of <a href="https://t.me/Peaky_blinder_tg">Peaky blinder</a></b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/Infinity_BOTs")
                                    ],[
                                      InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html"
)

@Bot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Bot.send_message(
               chat_id=message.chat.id,
               text="""<b>avnte oru help phaaaa </b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Bot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Bot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>
<b>♞ Developer:</b> <a href="https://t.me/ImJanindu">Janindu 🇱🇰</a>
<b>♞ Support:</b> <a href="https://t.me/InfinityBOTs_Support">Infinity BOTs Support</a>
<b>♞ Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>
<b>~ @Infinity_BOTs</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Source Code", url="https://github.com/ImJanindu/JETelegraphBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")


@Client.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @Infinity_BOTs
"""
)

Bot.run()
