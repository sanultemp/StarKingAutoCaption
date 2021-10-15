# <C> StarKing Developers


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "2043641521:AAF7DRIsY-bNc_rfPWED1w_LkWZ7CmVSXUM")
    API_ID = int(os.environ.get("APP_ID", 7469109))
    API_HASH = os.environ.get("API_HASH", "4d4023337b8cc46c306af69adb5fc21a")
    CAPTION = os.environ.get("CAPTION", "𝗙𝗟𝗜𝗫 𝗖𝗜𝗡𝗘𝗠𝗔 ™°\n@Flix_CinemaSL")
    BUTTON_TEXT = os.environ.get("BUTTON", "")
    URL_LINK = os.environ.get("LINK", "https://t.me/flixcimaslk")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@FlixCaption_Bot")
