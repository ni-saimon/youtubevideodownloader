from pytube import YouTube

yt = YouTube(input())

yt.streams.get_by_resolution('720p').download('C:\\Users\\nafiz\\Downloads\\YT')