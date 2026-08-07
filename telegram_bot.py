import requests

from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
)


def send_message(message):

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram configuration missing.")
        return False

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_BOT_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=15,
        )

        if response.status_code == 200:
            print("Telegram message sent.")
            return True

        print(
            f"Telegram Error : "
            f"{response.status_code} "
            f"{response.text}"
        )

        return False

    except Exception as e:

        print(f"Telegram Exception : {e}")

        return False
