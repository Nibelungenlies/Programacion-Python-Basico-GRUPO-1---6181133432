# Lista de productos
productos = [
    {"nombre": "Camiseta", "precio": 25.0},
    {"nombre": "Pantalón", "precio": 40.0},
    {"nombre": "Zapatos", "precio": 60.0},
    {"nombre": "Gorra", "precio": 15.0},
]

def filtrar_productos_por_precio(productos, umbral):
    """
    Retorna una lista con los nombres de los productos cuyo precio es mayor al umbral.
    """
    return [producto["nombre"] for producto in productos if producto["precio"] > umbral]

productos_caros = filtrar_productos_por_precio(productos, 30)
print("Productos con precio mayor a 30:", productos_caros)