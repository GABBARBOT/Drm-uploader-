#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26184715"))
API_HASH = environ.get("API_HASH", "7fc42fe25c89660b4e0b00dd7aa0beb1")
BOT_TOKEN = environ.get("BOT_TOKEN", "8410957916:AAHRHjMAbdBNvGbfyCtaSo0BxErqcLZkiTg")

OWNER = int(environ.get("OWNER", "1182777261"))
CREDIT = environ.get("CREDIT", "🍀GABBAR🍀")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
