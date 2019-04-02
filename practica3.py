from bs4 import BeautifulSoup
from kernel import match_class
import requests


result = requests.get("https://www.allkeyshop.com/blog/buy-sekiro-shadows-die-twice-cd-key-compare-prices/")
c = result.content
parseador = BeautifulSoup(c, 'html5lib')
precios = parseador.findAll(match_class(["price"]))

lListaPrecios = [] #Precios del juego indicado.

for precio in precios:
        sTexto = precio.span.text #Obtenemos el precio dentro de la etiqueta span
        fPrecioFlotante = float(sTexto.join(sTexto.split()).replace("€", ""))
        lListaPrecios.append(fPrecioFlotante)# Añadimos los precios en la lista








