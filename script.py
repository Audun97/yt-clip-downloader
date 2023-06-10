# Import pytube and moviepy
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

# Ask the user for the video URL and the start and end time in seconds
video_url = input("Enter the video URL: ")
start_time = int(input("Enter the start time in seconds: "))
end_time = int(input("Enter the end time in seconds: "))

# Create a YouTube object and download the video
yt = YouTube(video_url)
video = yt.streams.filter(file_extension='mp4').first()
video.download(filename='video.mp4')

# Create a VideoFileClip object and cut the video according to the time stamps
clip = VideoFileClip('video.mp4')
subclip = clip.subclip(start_time, end_time)
subclip.write_videofile('subclip.mp4')

# Close the clips
clip.close()
subclip.close()

os.remove('video.mp4')