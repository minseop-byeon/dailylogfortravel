import requests
import os
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

# 현재 UTC 기준 시간 (임시)
now = datetime.utcnow().strftime("%Y년 %m월 %d일 %H:%M")

send_message(f"{now} 서버 시간 기록 테스트")
