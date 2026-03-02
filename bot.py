import requests
import time
import hashlib
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

SHEET_URL = "https://docs.google.com/spreadsheets/d/1h-i-_RS2GxWkIH4iZwNLNV3NSUEB4fz9xyIWrJIhwxg/export?format=csv&gid=168784301"

last_hash = None

while True:
    try:
        response = requests.get(SHEET_URL)
        current_data = response.text
        current_hash = hashlib.md5(current_data.encode()).hexdigest()

        if last_hash and current_hash != last_hash:
            requests.get(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                params={
                    "chat_id": CHAT_ID,
                    "text": "⚡ Є зміни в аркуші НОВИНКИ!"
                }
            )

        last_hash = current_hash
        time.sleep(60)

    except Exception:
        time.sleep(60)
