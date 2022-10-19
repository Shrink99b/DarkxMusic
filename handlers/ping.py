import os
import asyncio
import time
from datetime import datetime

import psutil

from handlers import StartTime
from helpers.filters import command
from telegram.utils.helpers import escape_markdown, mention_html
from config import BOT_USERNAME, SUPPORT_GROUP, CHANNEL_UPDATES, PING_IMG, BOT_NAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


@Client.on_message(command(["ping", "repo", "ariyan", "alive"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.delete()
    boottime = time.time()
    bot_uptime = escape_markdown(get_readable_time((time.time() - StartTime)))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply_sticker("CAACAgQAAxkBAAICpGNPxPHPdw3hyH_5Rc1yGAGPH9htAAKOCQACpZdxUYvHGycIZ7mtKgQ")
    jay = await message.reply_photo(
        photo=f"{PING_IMG}",
        caption=" Pinging...⚡ ",
    )
    await jay.edit_text(
        f"""<b> ᴘᴏɴɢ ᴘɪɴɢ ! ⚡</b>\n  🏓 `{resp} ms`\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛsᴛs :</u></b>\n\n✨ ᴜᴘᴛɪᴍᴇ : {bot_uptime}\n🔮 ᴄᴘᴜ : {cpu}%\n💫 ᴅɪsᴋ : {disk}%\n❤️ ʀᴀᴍ : {mem}\n\n||ᴍᴀᴅᴇ 🖤 ʙʏ [ᴘʀɪɴᴄᴇ ᴀʀɪʏᴀɴ](https://t.me/Prince_ariyan_143)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📨 sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📨 ᴜᴘᴅᴀᴛᴇ ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🔎 ʙᴏᴛ ʀᴇᴘᴏ ", url="https://github.com/Prince-ariyan-143/DarkxMusic"
                    )
                ]
            ]
        ),
    )
