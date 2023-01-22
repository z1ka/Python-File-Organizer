import os
import shutil
from pathlib import Path
import PySimpleGUI as sg


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", ".wav", ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov", ".mp4", ".m4p", ".m4v", ".mxf", ".MP4")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png", ".gif", ".webp", ".svg", ".apng", ".avif", ".JPG", ".JPEG")

zipf = (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip")

torrent = (".torrent", ".Torrent")

txt = (".txt", ".TXT", ".rtf")

documents = (".pdf", ".doc", ".docm", ".docx", ".html",
          ".odt", ".pot", ".pptx")

codes = (".c",".py",".java",".cpp",".js",".html",".css",".php", ".jar")

# Creating Folders
'''Path("Audio").mkdir(exist_ok=True)
Path("Videos").mkdir(exist_ok=True)
Path("Photos").mkdir(exist_ok=True)
Path("ZIP").mkdir(exist_ok=True)
Path("Torrents").mkdir(exist_ok=True)
Path("Documents").mkdir(exist_ok=True)
Path("Text Files").mkdir(exist_ok=True)
Path("Codes").mkdir(exist_ok=True)'''

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
def is_documents(file):
    return os.path.splitext(file)[1] in documents
def is_txt(file):
    return os.path.splitext(file)[1] in txt
def is_codes(file):
    return os.path.splitext(file)[1] in codes


# Loop
"""for file in os.listdir():
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
    elif is_documents(file):
        shutil.move(file, "Documents")
    elif is_txt(file):
        shutil.move(file, "Text Files")
    elif is_codes(file):
        shutil.move(file, "Codes")"""

sg.theme('Darkgrey15')
# Exit Message to User
layout = [
          [sg.Text('Hello, ' + os.getlogin() + '!',size=(15, 1))],
          [sg.Text("Please check the boxes you want organized, and then click organize")],
          [sg.Text("your files will be saved in new folders.")],
          [sg.Text("")],
          [sg.Checkbox('Audio', default=False, key='-Audio'),
          sg.Checkbox('Videos',default=False, key='-Videos'),
          sg.Checkbox('Photos', default=False, key='-Photos'),
          sg.Checkbox('ZIP',default=False, key='-ZIP')],
          [sg.Checkbox('Torrents', default=False, key='-Torrents'),
          sg.Checkbox('Documents',default=False, key='-Documents'),
          sg.Checkbox('Text Files', default=False, key='-Text'),
          sg.Checkbox('Codes',default=False, key='-Codes')],
          [sg.Text("")],
          [sg.Button('Organize', size=(53, 1), button_color=('white', 'gray'))],
          [sg.Button('Quit', size = (53, 1), button_color= ('white','black'))],
          [sg.Text("")]
]

# Create the window
window = sg.Window('CleanUp', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Organize':
        for file in os.listdir():
            if is_audio(file) and values['-Audio']==True:
                Path("Audio").mkdir(exist_ok=True)
                shutil.move(file, "Audio")
            elif is_video(file) and values['-Videos']==True:
                Path("Videos").mkdir(exist_ok=True)
                shutil.move(file, "Videos")
            elif is_image(file) and values['-Photos']==True:
                Path("Photos").mkdir(exist_ok=True)
                shutil.move(file, "Photos")
            elif is_zip(file) and values['-ZIP']==True:
                Path("ZIP").mkdir(exist_ok=True)
                shutil.move(file, "ZIP")
            elif is_torrent(file) and values['-Torrents']==True:
                Path("Torrents").mkdir(exist_ok=True)
                shutil.move(file, "Torrents")
            elif is_documents(file) and values['-Documents']==True:
                Path("Documents").mkdir(exist_ok=True)
                shutil.move(file, "Documents")
            elif is_txt(file) and values['-Text']==True:
                Path("Text Files").mkdir(exist_ok=True)
                shutil.move(file, "Text Files")
            elif is_codes(file) and values['-Codes']==True:
                Path("Codes").mkdir(exist_ok=True)
                shutil.move(file, "Codes")
    sg.Popup('     Done!', keep_on_top=True)


# Finish up by removing from the screen
window.close()