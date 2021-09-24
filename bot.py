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
    await update.reply_photo(
        photo="https://telegra.ph/file/fe47bf785fc127335ac1f.jpg",
        caption=f"""**Hello {update.from_user.mention}\nഞാൻ Mᴏᴠɪᴇ Gʀᴀᴍ എന്ന ഗ്രൂപ്പിൽ മൂവി ഫിൽറ്റർ ചെയ്യുന്ന ബോട് അണ്
നോക്കണ്ടാ എന്നെ മറ്റു ഗ്രൂപ്പിൽ ഒന്നും ഉപയോഗിക്കാൻ കഴിയുകയില്ല!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚠️ 𝙂𝙍𝙊𝙐𝙋", url="https://t.me/MGMOVIEGRAM"),
                    InlineKeyboardButton("🕵‍♂ 𝘾𝙍𝙀𝘼𝙏𝙊𝙍", url="https://t.me/Xxxtentacion_TG"),
                ],
                [
                    InlineKeyboardButton("♻️ 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ♻️", url="https://t.me/joinchat/WSO_eDhGmFhmMzE1")
                ],
                [
                    InlineKeyboardButton("💡𝙃𝙀𝙇𝙋", callback_data="help_data"),
                    InlineKeyboardButton("🔐 𝘾𝙇𝙊𝙎𝙀", callback_data="close_data"),
                ]
            ]
        ),
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
