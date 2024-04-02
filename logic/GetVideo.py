import yt_dlp, os
from logic.getDownloads import get_download_path
from logic.SongBasic import SongBasic, extract
api_key = os.getenv('YT_KEY')

def search(self, video_url, ctx):
        with yt_dlp.YoutubeDL(self.ydl_opts_Video) as ydl:
            try:
                result = ydl.extract_info(video_url, download=False)
                
                return [extract(result, ctx)]
            
            except yt_dlp.DownloadError as e:
                return []
            
def download(Song: SongBasic): 
    ydl_opts = {
        'api_key': api_key,
        'quiet': False,
        'format': 'bestaudio/best',  # Descargar el mejor formato de audio disponible
        'outtmpl': f'temp/%(id)s.%(ext)s',  # Nombre del archivo de salida
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Especificar MP3 como el códec preferido
        }],
    }   
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            
            ydl.download([Song.url])  # Descargar la canción
            video_file_path =  os.path.join(get_download_path(), f"{Song.title}.mp3")
            
            print(f"Se descargo: {video_file_path}")
            
        except yt_dlp.DownloadError as e:
            print(f"Error al descargar la canción: {str(e)}")