import psutil
import time
import logging
from InflexMusic import app as Client
from pyrogram import filters
from pyrogram.types import Message
from InflexMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    get_served_chats,
    get_served_users
)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Record the start time of the bot
start_time = time.time()

# Counter for tracking consecutive zero active chats
zero_active_chat_counter = 0
MAX_ZERO_CHAT_COUNT = 5

# Function to format the uptime in a human-readable format
def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)

    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))

    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]

    return tmp

# Define a command handler for the /RocksStatusBot command
@Client.on_message(filters.command("RocksStatusBot"))
async def activevc(_, message: Message):
    global zero_active_chat_counter
    try:
        uptime = time_formatter((time.time() - start_time) * 1000)
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        ram = memory.percent
        active_chats = await get_active_chats()
        active_video_chats = await get_active_video_chats()
        total_chats = (len(active_chats) + len(active_video_chats)) * 3  # Multiply by 3
        served_chats = await get_served_chats()
        served_users = await get_served_users()

        if total_chats == 0:
            zero_active_chat_counter += 1
        else:
            zero_active_chat_counter = 0  # Reset after a successful status report

        if zero_active_chat_counter >= MAX_ZERO_CHAT_COUNT:
            await message.reply("sᴇʀᴠᴇʀ ɪᴘ ʙʟᴏᴄᴋ 🚫")
            # Send the message after IP block
            TEXT = (
                f"**ᴜᴘᴛɪᴍᴇ** : {uptime} | **ᴄᴘᴜ** : {cpu}%\n"
                f"ㅤ╰⊚ **ʀᴀᴍ** : {ram}% | sᴇʀᴠᴇʀ ɪᴘ ʙʟᴏᴄᴋ 🚫\n"
                f"ㅤㅤ╰⊚ **ᴄʜᴀᴛs** : {len(served_chats)} | **ᴜsᴇʀs** : {len(served_users)}"
            )
            await message.reply(TEXT)
        else:
            TEXT = (
                f"**ᴜᴘᴛɪᴍᴇ** : {uptime} | **ᴄᴘᴜ** : {cpu}%\n"
                f"ㅤ╰⊚ **ʀᴀᴍ** : {ram}% | **ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs** : {total_chats}\n"
                f"ㅤㅤ╰⊚ **ᴄʜᴀᴛs** : {len(served_chats)} | **ᴜsᴇʀs** : {len(served_users)}"
            )
            await message.reply(TEXT)

    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
