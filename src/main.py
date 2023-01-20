# A simple program to download videos from social media.
# Suported social media: Facebook Youtube Twitter

from pytube import YouTube
import ffmpeg
import sys

yt = YouTube('https://www.youtube.com/shorts/mwcukSUltGY')


video_qualitys = ['2160p60fps', '2160p30fps', '1440p60fps', '1440p30fps', '1080p60fps',
                  '1080p30fps', '720p60fps', '720p30fps', '480p60fps', '480p30fps', '360p60fps', '360p30fps']
video_streams = dict().fromkeys(video_qualitys)

for quality in video_qualitys:
    n = len(quality)
    video_streams[quality] = yt.streams.filter(
        mime_type='video/mp4', res=quality[0:n-5], progressive=False, fps=int(quality[n-5:n-3])).first()
    
for key, i in zip(video_streams, range(len(video_streams))):
    print(f'Pos: {i}. {key}: {video_streams[key]}')

print('Please select resolution of video:')
count = 1
for quality in video_streams:
    if video_streams[quality]:
        print(f'{count}. {quality}')
    count += 1

option = int(input('>'))

# Download video and audio
video_streams[video_qualitys[option-1]].download(filename='video.mp4')
yt.streams.filter(abr='128kbps').first().download(filename='audio.mp3')

# Merge video and audio
video = ffmpeg.input('video.mp4')
audio = ffmpeg.input('audio.mp3')
ffmpeg.output(audio, video, 'descarga.mp4').run(overwrite_output=True)

sys.os(' ')