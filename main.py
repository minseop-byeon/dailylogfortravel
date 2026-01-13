import requests
import os

BOT_TOKEN = os.getenv("dailylogfortravel_bot")
CHAT_ID = os.getenv("8559715819")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

send_message("서버 연결 테스트 메시지입니다.")
