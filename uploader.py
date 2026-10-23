import json, os, pathlib, requests

BASE = pathlib.Path(__file__).resolve().parent
CHANNEL = "@pinayasian_496"
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
def load(name):
    return json.loads((BASE / name).read_text(encoding="utf-8"))
videos = load("videos.json")
posted = set(load("posted.json"))
count = 0
for item in videos:
    if count >= 5:
        break
    url = item.get("url", "")
    if not url.startswith("https://") or url in posted:
        continue
    caption = item.get("caption", "")[:1024]
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendVideo",
        data={"chat_id": CHANNEL, "video": url, "caption": caption},
        timeout=120,
    )
    response.raise_for_status()
    if not response.json().get("ok"):
        raise RuntimeError("Telegram rejected a video URL")
    posted.add(url)
    (BASE / "posted.json").write_text(json.dumps(sorted(posted), indent=2) + "\n", encoding="utf-8")
    count += 1
print(f"Successfully posted {count} video(s)")
