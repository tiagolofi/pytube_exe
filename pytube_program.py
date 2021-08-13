
from pytube import YouTube

def download_yt(link: str, type: str):
  try:
    yt = YouTube(link)
  except:
    return print('ERROR: invalid link')
  if type == 'audio':
    print('SUCESS: downloading audio')
    audio = yt.streams.filter(
      only_audio=True, 
      adaptive=True, 
      file_extension='mp4').get_audio_only('mp4')
    return audio.download()
  elif type == 'video':
    print('SUCESS: downloading video') 
    video = yt.streams.get_highest_resolution()
    return video.download()
  else:
    print('ERROR: type would be audio or video')

link_video = str(input('YouTube video URL:'))
type_output = str(input('File type (audio or video):'))

download_yt(
  link=link_video,
  type=type_output
 )