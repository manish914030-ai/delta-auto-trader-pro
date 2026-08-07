import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_message(message):

    print("========== TELEGRAM DEBUG ==========")
    print(f"BOT TOKEN : {TELEGRAM_BOT_TOKEN[:10]}...")
    print(f"CHAT ID   : {TELEGRAM_CHAT_ID}")

    if not TELEGRAM_BOT_TOKEN:
        print("ERROR : TELEGRAM_BOT_TOKEN Missing")
        return False

    if not TELEGRAM_CHAT_ID:
        print("ERROR : TELEGRAM_CHAT_ID Missing")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": str(TELEGRAM_CHAT_ID),
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=15
        )

        print(f"Status Code : {response.status_code}")
        print(f"Response    : {response.text}")

        if response.status_code == 200:
            print("✅ Telegram Message Sent Successfully")
            return True

        print("❌ Telegram Message Failed")
        return False

    except Exception as e:
        print(f"Telegram Exception : {e}")
        return False
