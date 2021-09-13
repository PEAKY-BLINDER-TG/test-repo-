from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = pyrogram.Client(
      "siri",
       bot_token=Config.BOT_TOKEN,
       api_id=Config.APP_ID,
       api_hash=Config.API_HASH,
       plugins=dict(root="siri")
    )

@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_photo(photo=Config.START_IMG, caption=Config.START_MSG.format(message.from_user.mention),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('⚠️  𝒋𝒐𝒊𝒏', url='https://t.me/cinemazilla')
                 ],[
                    InlineKeyboardButton('⚠️  𝒋𝒐𝒊𝒏', url='https://t.me/cinemazilla'),
                    InlineKeyboardButton('yoyo', url='https://t.me/wasim')
            ]
          ]
        ),
        reply_to_message_id=message.message_id
    )
app.run()
