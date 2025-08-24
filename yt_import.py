
import yt_dlp
import os


def video_import(url: str, output_dir: str):

    outtmpl = os.path.join(output_dir, "%(title)s.%(ext)s")

    with yt_dlp.YoutubeDL({"format": "best", "outtmpl": outtmpl}) as ydl:
        ydl.download([url])


