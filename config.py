# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "2005797220:AAFNuJeZVL2XZdwD_eFre6bi-xk6zwNJFcs")
    API_ID = int(os.environ.get("APP_ID", 8901416))
    API_HASH = os.environ.get("API_HASH", "ff05861c1bf07edcb2644f7f308584df")
    CAPTION = os.environ.get("CAPTION", "@Mo_Tech_YT @Mo_Tech_Group")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "T.ME/MO_TECH_YT")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "TestAutoCaption_Bot")
