# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

import os

from bot import Bot
from config import (
    ADMINS,
    API_HASH,
    API_ID,
    CHANNEL_ID,
    DB_URI,
    FORCE_MSG,
    SUBS1,
    SUBS2,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    LOGGER,
    OWNER,
    PROTECT_CONTENT,
    START_MSG,
    BOT_TOKEN,
)
from pyrogram import filters
from pyrogram.types import Message


@Bot.on_message(filters.command("logs") & filters.user(ADMINS))
async def get_bot_logs(client: Bot, m: Message):
    bot_log_path = "logs.txt"
    if os.path.exists(bot_log_path):
        try:
            await m.reply_document(
                bot_log_path,
                quote=True,
                caption="<b>Ini Logs Bot ini</b>",
            )
        except Exception as e:
            os.remove(bot_log_path)
            LOGGER(__name__).warning(e)
    elif not os.path.exists(bot_log_path):
        await m.reply_text("❌ <b>Tidak ada log yang ditemukan!</b>")


@Bot.on_message(filters.command("vars") & filters.user(ADMINS))
async def varsFunc(client: Bot, message: Message):
    Man = await message.reply_text("Tunggu Sebentar...")
    text = f"""<u><b>CONFIG VARS</b></u> @{client.username}
APP_ID = <code>{APP_ID}</code>
API_HASH = <code>{API_HASH}</code>
BOT_TOKEN = <code>{BOT_TOKEN}</code>
DATABASE_URL = <code>{DB_URI}</code>
OWNER = <code>{OWNER}</code>
ADMINS = <code>{ADMINS}</code>
    
<u><b>CUSTOM VARS</b></u>
CHANNEL_ID = <code>{CHANNEL_ID}</code>
SUBS1 = <code>{SUBS1}</code>
SUBS2 = <code>{SUBS2}</code>
PROTECT_CONTENT = <code>{PROTECT_CONTENT}</code>
START_MSG = <code>{START_MSG}</code>
FORCE_MSG = <code>{FORCE_MSG}</code>

<u><b>HEROKU CONFIGVARS</b></u>
HEROKU_APP_NAME = <code>{HEROKU_APP_NAME}</code>
HEROKU_API_KEY = <code>{HEROKU_API_KEY}</code>
    """
    await Man.edit_text(text)
