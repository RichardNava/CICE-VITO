
#? python -m pip uninstall youtube_dl (Para instalar la libreria)
from youtube_dl import YoutubeDL

audio_downloader = YoutubeDL({'format':'bestaudio'})

URL = input('URL a descargar:  ')
audio_downloader.extract_info(URL)
