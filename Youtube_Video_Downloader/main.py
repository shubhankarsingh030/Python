from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def dowload_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video Download Seccesfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")

    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_URL = input("Enter video URL For Downloading: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        dowload_video(video_URL,save_dir)
    else:
        print("Invalid Save Location")