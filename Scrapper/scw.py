import requests
from bs4 import BeautifulSoup

# URL
url = "https://cnnespanol.cnn.com/category/mexico/"

# Realizar una solicitud GET a la página web
response = requests.get(url)