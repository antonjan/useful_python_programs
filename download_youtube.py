#pip install pytube

from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=OP_ECe9DP-Q

save_path='E:/'

# Create a YouTube object

video = YouTube (video_url)

# quality(quality) and format, etc

stream=video.streams.get_highest_resolution()

# Download the video

stream.download (output_path=save_path)

print("Video Downloaded Successfully.")
