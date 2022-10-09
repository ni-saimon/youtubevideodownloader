from pytube import YouTube

# Youtube link input from user
yt = YouTube(input())

# Resolution of the video
Resolution = '720p'

# Download path
Path = 'C:\\Users\\nafiz\\Downloads\\YT'

yt.streams.get_by_resolution(Resolution).download(Path)
