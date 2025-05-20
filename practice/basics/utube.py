import pytube
from pytube import YouTube
url=input("Enter the url of video you want to download from youtube ")
yt = YouTube(url)
print(yt.title)