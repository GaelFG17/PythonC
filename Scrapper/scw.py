import requests
from bs4 import BeautifulSoup

# URL
url = "https://cnnespanol.cnn.com/category/mexico/"

# Realizar una solicitud GET a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los elementos que contienen los títulos de los artículos
    titles = soup.find_all('h2')  # O ajusta el selector según sea necesario

    # Imprimir los títulos de los artículos     
    for i, title in enumerate(titles, start=1):
        print(f"{i}. {title.get_text(strip=True)}")

else:
    print(f"Error al acceder a la página: {response.status_code}")