import os
import subprocess
import sys

# CONFIG
VIDEO_URL = os.environ.get("VIDEO_URL")  # Direct .mp4 or .mkv link
TELEGRAM_STREAM_KEY = os.environ.get("TELEGRAM_STREAM_KEY")  # Example: abcd-1234-wxyz
MODE = os.environ.get("MODE", "download")  # Options: 'download' or 'direct'

if not VIDEO_URL or not TELEGRAM_STREAM_KEY:
    print("Missing VIDEO_URL or TELEGRAM_STREAM_KEY env var")
    sys.exit(1)

RTMP_URL = f"rtmps://dc5-1.rtmp.t.me/s/{TELEGRAM_STREAM_KEY}"

def stream_file(filename):
    print(f"Starting FFmpeg stream for file: {filename}")
    cmd = [
        "ffmpeg", "-re",
        "-i", filename,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "3000k",
        "-maxrate", "3500k",
        "-bufsize", "6000k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        RTMP_URL
    ]
    subprocess.run(cmd)

def stream_from_url(url):
    print("Streaming directly from URL (no download)...")
    cmd = [
        "ffmpeg", "-re",
        "-i", url,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-b:v", "3000k",
        "-maxrate", "3500k",
        "-bufsize", "6000k",
        "-c:a", "aac",
        "-b:a", "128k",
        "-f", "flv",
        RTMP_URL
    ]
    subprocess.run(cmd)

if MODE == "download":
    filename = "video.mp4"
    print(f"Downloading: {VIDEO_URL}")
    subprocess.run(["wget", "-O", filename, VIDEO_URL])
    stream_file(filename)
elif MODE == "direct":
    stream_from_url(VIDEO_URL)
else:
    print(f"Unknown mode: {MODE}")
