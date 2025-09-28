# import os
# ##Code Written By @ItsMeMaster
# ##Code Written By @ItsMeMaster

# class Config(object):
#     BOT_TOKEN = ""
#     DB_NAME = "takkishor9784"
#     API_ID = "21157244"
#     API_HASH = "4981c2699bd91c7db836ec8f77e5b0f0"
#     ADMIN_ID = [1783306092]
#     DB_URL = "mongodb+srv://takkishor9784:gG73juoh44MnvJEZ@cluster0.q8hxdk2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#     LOG_CHANNEL = -1002758652479 # Your Log Channel ID (Bot ko ADMIN BNAYE)
#     USERLINK = "https://t.me/bosch12345o"
#     TUTORIAL_VIDEO = "https://t.me/bosch12345o"
import os

class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")           # from Render env
    DB_NAME = os.getenv("DB_NAME", "tbogtt9784")
    API_ID = int(os.getenv("API_ID"))            # convert to int
    API_HASH = os.getenv("API_HASH")
    ADMIN_ID = []
    DB_URL = os.getenv("DB_URL", "mongodb+srv://takkishor9784:gG73juoh44MnvJEZ@cluster0.q8hxdk2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # fallback if not set
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
    USERLINK = os.getenv("USERLINK", "https://t.me/bos56456ch12345o")
    TUTORIAL_VIDEO = os.getenv("TUTORIAL_VIDEO", "https://t.me/bos45h12345o")

