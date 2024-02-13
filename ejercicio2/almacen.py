class Producto:
    def __init__(self, nombre, identificador, precio):
        self._nombre = nombre
        self._identificador = identificador
        self._precio = precio

    def __str__(self):
        return f"Nombre: {self._nombre}\nIdentificador: {self._identificador}\nPrecio: {self._precio}"
    def __eq__(self, otro):
        return self._identificador == otro._identificador
    def comprar(self, unidades):
        precio_pagar = unidades * self._precio
        if(unidades > 50):
            precio_pagar /= 2
        return precio_pagar

class Perecedero(Producto):
    def __init__(self, nombre, identificador, precio, dias_caduca):
        super().__init__(nombre, identificador, precio)
        self._dias_caduca = dias_caduca

    def __str__(self):
        return f"Nombre: {self._nombre}\nIdentificador: {self._identificador}\nPrecio: {self._precio}\nDias para caducar: {self._dias_caduca}"
    def comprar(self, unidades):
        precio = 0.0
        if(self._dias_caduca == 1):
            precio = super().comprar(unidades)
        elif(self._dias_caduca == 2):
            precio = unidades * self._precio / 3
        elif(self._dias_caduca == 3):
            precio = unidades * self._precio / 2
        else:
            precio = unidades * self._precio
        return precio


producto1 = Producto("Television", "SONY1", 50)
producto2 = Perecedero("Jamon serrano", "jam1", 100, 1)
print(producto2.comprar(100))