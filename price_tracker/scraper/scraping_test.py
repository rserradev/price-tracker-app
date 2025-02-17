import requests
from bs4 import BeautifulSoup


# URL de la página de productos
URL = "https://www.paris.cl/zapatillas-urbana-cuero-knu-skool-unisex-614258.html"

# Simulación de un navegador web
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Hacer la petición GET a la URL
response = requests.get(URL, headers=HEADERS)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    print("Petición exitosa")

    # Analizar el html de la respuesta
    soup = BeautifulSoup(response.text, "html.parser")

    # Obtener el nombre y precio del producto
    name = soup.find("div", {"class": "pdp-top__product-name"}).text
    price = soup.find("div", {"class": "bottom-content-prices__container"}).text

    print(f"Nombre: {name} Precio: {price}")
else:
    print(f"Petición fallida: {response.status_code}")