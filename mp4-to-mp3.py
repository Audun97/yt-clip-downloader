import os
from moviepy.editor import AudioFileClip

# Get all files in the current directory
files = os.listdir()

# Filter out the mp4 files
mp4_files = [file for file in files if file.endswith('.mp4')]

# Convert each mp4 file to mp3
for mp4_file in mp4_files:
    audio = AudioFileClip(mp4_file)
    mp3_file = mp4_file.replace('.mp4', '.mp3')
    audio.write_audiofile(mp3_file)

    # Close the clip
    audio.close()