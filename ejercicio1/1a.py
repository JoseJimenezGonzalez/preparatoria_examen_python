from urllib import request
from json import loads

f = request.urlopen("https://api.coindesk.com/v1/bpi/currentprice.json")
datos_json = f.read().decode("utf-8")
datos_diccionario = loads(datos_json)
#La fecha
fecha = datos_diccionario['time']['updateduk']
print(fecha)
#moneda es la clave y info es el valor asociado a la clave
for moneda, info in datos_diccionario['bpi'].items():
    code = info['code']
    rate_float = info['rate_float']
    print("Moneda:", code)
    print("Precio:", rate_float)