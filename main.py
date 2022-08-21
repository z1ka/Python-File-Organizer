import os
import shutil
from pathlib import Path

# Changes Directory to Desktop
os.chdir(os.path.expanduser("~/Desktop"))


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".MP4")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif", ".JPG", ".JPEG")

zipf = (".zip", ".ZIP")

torrent = (".torrent", ".Torrent")

txt = (".txt", ".TXT")

office = (".pdf", ".doc", ".docm", ".docx", ".html",
          ".odt", ".pot", ".pptx")

codes = (".c",".py",".java",".cpp",".js",".html",".css",".php", ".jar")

# Creating Folders
Path("Audio").mkdir(exist_ok=True)
Path("Videos").mkdir(exist_ok=True)
Path("Photos").mkdir(exist_ok=True)
Path("ZIP").mkdir(exist_ok=True)
Path("Torrents").mkdir(exist_ok=True)
Path("Office").mkdir(exist_ok=True)Audio
Path("Text Files").mkdir(exist_ok=True)
Path("Codes").mkdir(exist_ok=True)

# Functions to determine extension type
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_zip(file):
    return os.path.splitext(file)[1] in zipf

def is_torrent(file):
    return os.path.splitext(file)[1] in torrent

def is_office(file):
    return os.path.splitext(file)[1] in office

def is_txt(file):
    return os.path.splitext(file)[1] in txt

def is_codes(file):
    return os.path.splitext(file)[1] in codes


# Loop
for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "Audio")
    elif is_video(file):
        shutil.move(file, "Videos")
    elif is_image(file):
        shutil.move(file, "Photos")
    elif is_zip(file):
        shutil.move(file, "ZIP")
    elif is_torrent(file):
        shutil.move(file, "Torrents")
    elif is_office(file):
        shutil.move(file, "Office")
    elif is_txt(file):
        shutil.move(file, "Text Files")
    elif is_codes(file):
        shutil.move(file, "Codes")

# Exit Message to User
print('Hello, ' + os.getlogin() + '!')
print("Your Desktop is now Organized, You will see 8 new Folders.")
input('Press ENTER to exit')