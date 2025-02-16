import requests

# URL de la página de productos
URL = "https://quotes.toscrape.com/"

# Simulación de un navegador web
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Hacer la petición GET a la URL
response = requests.get(URL, headers=HEADERS)

print("Scraping...")
