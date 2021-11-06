#made by wasim Faris 
#(Date 2021 sat, Nov 6)
import os
import logging
from pyrogram import Client, filters
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

APP_ID = "3637235"
API_HASH = "028885dcbc64a4b56c47bdad0367523b"
TG_BOT_TOKEN = "2110416751:AAF20hCuQlVsIIGEmJCSd03Z8H4rFbrm_6g"

plugins = dict(root="plugins")

print("wait iam deploy ing.....")

# client 
wasim = Client(
   "Test bot",
   api_id=APP_ID,
   api_hash=API_HASH,
   bot_token=TG_BOT_TOKEN,
   plugins=plugins
)
print("bot started")
wasim.run()
