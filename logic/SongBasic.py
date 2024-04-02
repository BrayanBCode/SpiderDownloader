class SongBasic():
    def __init__(self, title: str, artist: str, duration, thumbnail: str, id: int) -> None:
        self.title = title
        self.artist = artist
        self.duration = int(duration)
        self.thumbnail = thumbnail
        self.url = f"https://www.youtube.com/watch?v={id}"
        self.id = id
        print(self)
        
    def __str__(self):
        return (
            f"title: {self.title}\n"
            f"artist: {self.artist}\n"
            f"duration: {self.duration}\n"
            f"thumbnail: {self.thumbnail}\n"
            f"url: {self.url}\n"
            f"id: {self.id}\n"
        )
        

def extract(self, song):
    defaultImg = "https://salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png"
    
    # Intenta obtener la miniatura directamente desde 'thumbnail'
    thumbnail = song.get('thumbnail', defaultImg)

    # Si no se encuentra en 'thumbnail', intenta obtenerlo desde 'thumbnails'
    if thumbnail is defaultImg:
        thumbnails = song.get('thumbnails', defaultImg)
        if thumbnails:
            thumbnail = thumbnails[0].get('url', 'Sin foto de portada')
    
    return SongBasic(
        title=song.get('title', 'Canción sin título'),
        artist=song.get('uploader', 'Artista desconocido'),
        duration=song.get('duration', 0),
        thumbnail=thumbnail,
        id=song.get('id')
    )