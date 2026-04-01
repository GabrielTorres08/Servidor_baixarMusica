import yt_dlp
import imageio_ffmpeg

def baixar_audio(url):
    ydl_opts = {

        'outtmpl': 'Music/audio.%(ext)s',

        'format': 'bestaudio/best',

        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])