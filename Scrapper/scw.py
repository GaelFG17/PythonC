import requests
from bs4 import BeautifulSoup

# URL
url = "https://cnnespanol.cnn.com/category/mexico/"

# Realizar una solicitud GET a la página web
response = requests.get(url)


# Verificar si la solicitud fue exitosa
if response.status_code == 200:
