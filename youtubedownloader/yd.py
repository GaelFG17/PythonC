from pytube import YouTube

def download_video(url, path):
    try:
        # Crear un objeto de YouTube
        yt = YouTube(url)
    except Exception as e:
        print(f"Error al descargar el video: {e}")