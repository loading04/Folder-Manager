import os
import shutil

download_folder = os.path.expanduser("D:\\downloads")
image_folder = os.path.expanduser("D:\\downloads\\image")
exe = os.path.expanduser("D:\\downloads\\exe")
videos = os.path.expanduser("D:\\downloads\\videos")
pdf = os.path.expanduser("D:\\downloads\\pdf")
word = os.path.expanduser("D:\\downloads\\word")
music = os.path.expanduser("D:\\downloads\\music")
zip = os.path.expanduser("D:\\downloads\\zip")


if not os.path.exists(image_folder):
    os.makedirs(image_folder)
if not os.path.exists(exe):
    os.makedirs(exe)
if not os.path.exists(videos):
    os.makedirs(videos)
if not os.path.exists(pdf):
    os.makedirs(pdf)
if not os.path.exists(word):
    os.makedirs(word)
if not os.path.exists(music):
    os.makedirs(music)
if not os.path.exists(zip):
    os.makedirs(zip)

for filename in os.listdir(download_folder):
    if filename.endswith(".PNG") or filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".gif") or filename.endswith(".webp"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, image_folder)
    if filename.endswith(".pdf") or filename.endswith(".PDF"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, pdf)
    if filename.endswith(".exe") or filename.endswith(".apk") or filename.endswith(".msi"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, exe)
    if filename.endswith(".mp4"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, videos)
    if filename.endswith(".mp3") or filename.endswith(".wav"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, music)
    if filename.endswith(".docx"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, word)
    if filename.endswith(".zip") or filename.endswith(".rar"):
        file_path = os.path.join(download_folder, filename)
        shutil.move(file_path, zip)