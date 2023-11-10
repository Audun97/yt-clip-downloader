# Import pytube and moviepy
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

# Function to convert YouTube timestamp to seconds
def convert_to_seconds(time):
    time_parts = list(map(int, time.split(':')))
    if len(time_parts) == 3:
        return time_parts[0] * 3600 + time_parts[1] * 60 + time_parts[2]
    elif len(time_parts) == 2:
        return time_parts[0] * 60 + time_parts[1]
    else:
        return time_parts[0]

# Ask the user for the video URL and the start and end time in seconds
video_url = input("Enter the video URL: ")
start_time = input("Enter start timestamp (or f to download full): ")

# Create a YouTube object and download the video
yt = YouTube(video_url)
video = yt.streams.filter(file_extension='mp4').first()
video.download(filename='video.mp4')

# If the user wants to download the full video
if start_time.lower() == 'f':
    os.rename('video.mp4', 'full_video.mp4')
else:
    start_time = convert_to_seconds(start_time)
    end_time = convert_to_seconds(input("Enter end timestamp: "))

    # Create a VideoFileClip object and cut the video according to the time stamps
    clip = VideoFileClip('video.mp4')
    subclip = clip.subclip(start_time, end_time)
    subclip.write_videofile('subclip.mp4')

    # Close the clips
    clip.close()
    subclip.close()

    os.remove('video.mp4')