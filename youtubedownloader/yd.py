from pytube import YouTube

def download_video(url, path):
    try:
        # Crear un objeto de YouTube
        yt = YouTube(url)
        
        # Obtener el stream de mayor resolución
        stream = yt.streams.get_highest_resolution()

        # Descargar el video
        print(f"Descargando {yt.title}...")
        stream.download(output_path=path)
    except Exception as e:
        print(f"Error al descargar el video: {e}")