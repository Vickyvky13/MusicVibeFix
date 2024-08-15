
import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 99999))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TeamInflex/InflexMusicBot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/solotreee")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/solo_tree_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

# Set this to True if you want the bot restarts automatically at 03:30 AM at morning.
AUTO_RESTART = bool(getenv("AUTO_RESTART", True))


# Set this to True if you want the bot to restart when RAM usage exceeds 90%.
RAM_OVERLOAD_RESTART = bool(getenv("RAM_OVERLOAD_RESTART", True))


# Set this to True if you want the bot to restart when CPU usage exceeds 95%.
CPU_OVERLOAD_RESTART = bool(getenv("CPU_OVERLOAD_RESTART", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://graph.org//file/f351cf8a51c2d9fc9969a.jpg", "https://graph.org//file/63d9ff677a31e7bdde74c.jpg", "https://graph.org//file/958c83e01149905477db1.jpg", "https://graph.org//file/df0d9703b3044b28c0667.jpg", "https://graph.org//file/24971956b84188a7d6d1d.jpg", "https://graph.org//file/56bf510c9fb2da88f3ac5.jpg", "https://graph.org//file/dd30b64ea9a03ff742089.jpg", "https://graph.org//file/ce4d7df628c152905657c.jpg", "https://graph.org//file/649d518423c15d9798dfd.jpg", "https://graph.org//file/f704ede79fc4c07a383a0.jpg", "https://graph.org//file/e21b945ebdc9d47f1b898.jpg", "https://graph.org//file/7357c7c7a7982245378aa.jpg", "https://graph.org//file/2c19b5f90926636b56540.jpg", "https://graph.org//file/ef8aafd15d8f2685c47fc.jpg", "https://graph.org//file/00fca8406f256ddd869f8.jpg", "https://graph.org//file/a7102d9135fab37cb0139.jpg", "https://graph.org//file/a8917840f365ffa4baf37.jpg", "https://graph.org//file/3fce2fc4f5f3eec5cdc63.jpg", "https://graph.org//file/6c94242f9aac66822d1e6.jpg", "https://graph.org//file/4866d5be528c01dfbba44.jpg", "https://graph.org//file/92a07e127a6471e7751bc.jpg", "https://graph.org//file/f008c8fb92b93fa81437a.jpg", "https://graph.org//file/ac20a7f50db0f1f8f3db9.jpg", "https://graph.org//file/645dae609ea55d3096265.jpg", "https://graph.org//file/8043d6ce98f224318ee33.jpg"]
PING_IMG_URL = ["https://graph.org//file/f351cf8a51c2d9fc9969a.jpg", "https://graph.org//file/63d9ff677a31e7bdde74c.jpg", "https://graph.org//file/958c83e01149905477db1.jpg", "https://graph.org//file/df0d9703b3044b28c0667.jpg", "https://graph.org//file/24971956b84188a7d6d1d.jpg", "https://graph.org//file/56bf510c9fb2da88f3ac5.jpg", "https://graph.org//file/dd30b64ea9a03ff742089.jpg", "https://graph.org//file/ce4d7df628c152905657c.jpg", "https://graph.org//file/649d518423c15d9798dfd.jpg", "https://graph.org//file/f704ede79fc4c07a383a0.jpg", "https://graph.org//file/e21b945ebdc9d47f1b898.jpg", "https://graph.org//file/7357c7c7a7982245378aa.jpg", "https://graph.org//file/2c19b5f90926636b56540.jpg", "https://graph.org//file/ef8aafd15d8f2685c47fc.jpg", "https://graph.org//file/00fca8406f256ddd869f8.jpg", "https://graph.org//file/a7102d9135fab37cb0139.jpg", "https://graph.org//file/a8917840f365ffa4baf37.jpg", "https://graph.org//file/3fce2fc4f5f3eec5cdc63.jpg", "https://graph.org//file/6c94242f9aac66822d1e6.jpg", "https://graph.org//file/4866d5be528c01dfbba44.jpg", "https://graph.org//file/92a07e127a6471e7751bc.jpg", "https://graph.org//file/f008c8fb92b93fa81437a.jpg", "https://graph.org//file/ac20a7f50db0f1f8f3db9.jpg", "https://graph.org//file/645dae609ea55d3096265.jpg", "https://graph.org//file/8043d6ce98f224318ee33.jpg"]
STATS_IMG_URL = ["https://graph.org//file/f351cf8a51c2d9fc9969a.jpg", "https://graph.org//file/63d9ff677a31e7bdde74c.jpg", "https://graph.org//file/958c83e01149905477db1.jpg", "https://graph.org//file/df0d9703b3044b28c0667.jpg", "https://graph.org//file/24971956b84188a7d6d1d.jpg", "https://graph.org//file/56bf510c9fb2da88f3ac5.jpg", "https://graph.org//file/dd30b64ea9a03ff742089.jpg", "https://graph.org//file/ce4d7df628c152905657c.jpg", "https://graph.org//file/649d518423c15d9798dfd.jpg", "https://graph.org//file/f704ede79fc4c07a383a0.jpg", "https://graph.org//file/e21b945ebdc9d47f1b898.jpg", "https://graph.org//file/7357c7c7a7982245378aa.jpg", "https://graph.org//file/2c19b5f90926636b56540.jpg", "https://graph.org//file/ef8aafd15d8f2685c47fc.jpg", "https://graph.org//file/00fca8406f256ddd869f8.jpg", "https://graph.org//file/a7102d9135fab37cb0139.jpg", "https://graph.org//file/a8917840f365ffa4baf37.jpg", "https://graph.org//file/3fce2fc4f5f3eec5cdc63.jpg", "https://graph.org//file/6c94242f9aac66822d1e6.jpg", "https://graph.org//file/4866d5be528c01dfbba44.jpg", "https://graph.org//file/92a07e127a6471e7751bc.jpg", "https://graph.org//file/f008c8fb92b93fa81437a.jpg", "https://graph.org//file/ac20a7f50db0f1f8f3db9.jpg", "https://graph.org//file/645dae609ea55d3096265.jpg", "https://graph.org//file/8043d6ce98f224318ee33.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://graph.org/file/9d75bfb77e17b80b3da5b.png"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://te.legra.ph/file/693694b0d94afa372ca5a.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/f72ea4bd955c418c724e1.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://telegra.ph/file/5547c6a0bcfc016089088.png"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/c3682dc6fd740b2dac969.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
