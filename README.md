# Pinay Tambayan Telegram Uploader

Posts up to 5 authorized video URLs to @pinayasian_496 daily at 09:00 Asia/Manila.

## Setup
1. Add GitHub Actions secret `TELEGRAM_BOT_TOKEN` (never commit the token).
2. Edit `videos.json` with direct HTTPS URLs to videos you have permission to repost.
3. Run the workflow manually for a test.
4. GitHub Actions daily schedule runs at 01:00 UTC (09:00 Philippine time).

The uploader tracks posted URLs in `posted.json` committed back to this repository.
The source website is NOT scraped automatically; only authorized direct URLs are used.
