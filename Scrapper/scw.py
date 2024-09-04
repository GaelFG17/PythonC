import requests
from bs4 import BeautifulSoup

# URL del sitio web que deseas scrapear
url = "https://example.com"

# Realizar una solicitud GET a la página web
response = requests.get(url)