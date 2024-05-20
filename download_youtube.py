#pip install pytube

from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=t-7tYzTf_y8&t=1082s'

save_path='./'

# Create a YouTube object

video = YouTube (video_url)

# quality(quality) and format, etc

stream=video.streams.get_highest_resolution()

# Download the video
print ("Starting to download video")

stream.download (output_path=save_path)

print("Video Downloaded Successfully.")
