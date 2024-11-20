class Producto:
    def __init__(self, nombre:str, precio:float, cantidad:int, material:str) -> None:
        self.nombre = nombre 
        self.precio = precio
        self.cantidad = cantidad 
        self.material = material

    def __str__(self) -> str:
        return f' Producto: {self.nombre} -- Precio: {self.precio} -- Disponible: {self.cantidad}'