import os, requests
token = os.environ.get("TELEGRAM_BOT_TOKEN")
if not token:
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN secret")
r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id":"@pinayasian_496","text":"✅ Pinay Tambayan bot connection test successful. Daily video uploader configuration is being verified."},timeout=30)
r.raise_for_status()
data = r.json()
if not data.get("ok"):
    raise SystemExit("Telegram rejected test message")
print("Telegram channel test message sent successfully.")
