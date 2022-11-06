import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins_id = list(map(int, os.getenv("ADMINS_ID").split()))
