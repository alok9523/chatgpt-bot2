from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "10705457")
API_HASH = getenv("API_HASH", "bcc1e5c3860302e6f99f123353eea63b")
BOT_TOKEN = getenv("BOT_TOKEN", "6248436409:AAGOhMBJ_ST8C9GfPecqf0PzZsK4PiALIZ0")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
