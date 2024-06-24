import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from pytube import YouTube
import re

link = input("Provide the link of the video you want to download: ")
video_id = re.findall(r"v=([0-9A-Za-z_-]{11})", link)[0]
youtube = YouTube(f"https://www.youtube.com/watch?v={video_id}")
video = youtube.streams.all()

vid = list(enumerate(video))

for i in vid:
    print(i)

stream = int(input('Enter: '))
video[stream].download()
print('Your video has been downloaded successfully!')