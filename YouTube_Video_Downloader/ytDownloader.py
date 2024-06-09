import sys
from pytube import YouTube
import os

def downloadYoutube(url):
    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    yt.download('Videos')

url = input('Input url:- ')
downloadYoutube(url)
print("Download Completed")
