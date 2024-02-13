from urllib import request
from json import loads

eleccion_usuario = input("Introduce DOLARES, EUROS O LIBRAS")
cantidad_usuario = float(input("Introduce cantidad:"))
mensaje = ""
code = ""
if(eleccion_usuario == "DOLARES"):
    code = "USD"
elif(eleccion_usuario == "EUROS"):
    code = "EUR"
elif(eleccion_usuario == "LIBRAS"):
    code = "GBP"
else:
    mensaje = "No se reconoce esa opción"

f = request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json")
datos_json = f.read().decode("utf-8")
datos_diccionario = loads(datos_json)

#moneda es la clave y info es el valor asociado a la clave
moneda = datos_diccionario['bpi'][code]
equivalente_numerico = moneda['rate_float']
resultado = equivalente_numerico * cantidad_usuario
print(f"{cantidad_usuario} de {eleccion_usuario} equivale a {resultado} bitcoins")