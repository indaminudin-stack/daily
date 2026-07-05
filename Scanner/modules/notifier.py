import requests


def send_telegram(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        r = requests.post(url, data=payload)
        return r.json()
    except Exception as e:
        print("Telegram error:", e)
        return None