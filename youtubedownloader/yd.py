from pytube import YouTube
import ssl
import certifi

# Configurar Python para usar los certificados de certifi
ssl._create_default_https_context = ssl.create_default_context(cafile=certifi.where())

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
        
if __name__ == "__main__":
    video_url = input("Introduce la URL del video de YouTube: ")
    save_path = input("Introduce la ruta donde se guardará el video: ")
    
    download_video(video_url, save_path)