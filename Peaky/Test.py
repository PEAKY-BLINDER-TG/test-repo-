from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os
import time
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

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
