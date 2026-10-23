import json, os, pathlib, requests
BASE = pathlib.Path(__file__).resolve().parent
CHANNEL = "@pinayasian_496"
def load(name):
    return json.loads((BASE / name).read_text(encoding="utf-8"))
videos = load("videos.json")
posted = set(load("posted.json"))
queue = [v for v in videos if isinstance(v, dict) and v.get("approved") is True and v.get("non_explicit") is True and v.get("permission_confirmed") is True and isinstance(v.get("url"), str) and v["url"].startswith("https://") and v["url"] not in posted][:5]
if not queue:
    print("No approved, non-explicit, authorized videos to post.")
else:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN in GitHub Actions secrets.")
    for item in queue:
        url = item["url"]
        response = requests.post(f"https://api.telegram.org/bot{token}/sendVideo", data={"chat_id": CHANNEL, "video": url, "caption": str(item.get("caption", ""))[:1024]}, timeout=120)
        response.raise_for_status()
        if not response.json().get("ok"):
            raise RuntimeError("Telegram rejected video")
        posted.add(url)
        (BASE / "posted.json").write_text(json.dumps(sorted(posted), indent=2) + "\n", encoding="utf-8")
    print(f"Posted {len(queue)} approved video(s).")
