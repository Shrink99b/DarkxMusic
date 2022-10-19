from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "811052"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ed")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","ariyanXmusic")
BOT_USERNAME = getenv("BOT_USERNAME", "ariyanXmusic")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ariyan_discus")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "ariyan_server")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/6ace04b7668a0cd83f802.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/508209f27db5a305d1dd6.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5787575060").split()))
