import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al obtener, el código de estado es {response.status_code}")
        return None

def get_content_by_class_and_testid(html):
    soup = BeautifulSoup(html, "html.parser")
    # Buscar todos los elementos <span> con el data-testid="paris-text"
    tags = soup.find_all("span", {"data-testid": "paris-text"})
    if tags:
        for tag in tags:
            # Verificar si el text contiene el signo $
            if "$" in tag.text:
                price = tag.text.strip()
                print(f'El precio es {price}')
                break
    else:
        print("No se encontraron elementos con el data-testid especificado")

html = get_html("https://nuevo.paris.cl/zapatillas-urbana-cuero-knu-skool-unisex-614258.html")
if html:
    get_content_by_class_and_testid(html)
else:
    print("No se pudo obtener el HTML")