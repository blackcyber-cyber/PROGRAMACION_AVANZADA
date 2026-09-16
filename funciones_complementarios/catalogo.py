# -*- coding: utf-8 -*-
"""
Módulo de catálogo de productos.

Estructura de datos: diccionario de diccionarios.
Se eligió esta estructura porque cada producto necesita varios
atributos (nombre, precio, stock) accesibles por su clave única
(id_producto), permitiendo búsqueda directa en O(1) sin recorrer
listas.
"""


def cargar_catalogo():
    """
    Carga el catálogo de productos disponibles.

    Retorna:
        dict: diccionario de diccionarios con la forma
              {"id_producto": {"nombre": str, "precio": float, "stock": int}}
    """
    catalogo = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Té", "precio": 35.0, "stock": 15},
        "P003": {"nombre": "Galletas", "precio": 28.5, "stock": 30},
        "P004": {"nombre": "Chocolate", "precio": 52.0, "stock": 10},
        "P005": {"nombre": "Agua embotellada", "precio": 15.0, "stock": 50},
    }
    return catalogo


def mostrar_catalogo(catalogo):
    """
    Imprime una tabla con los productos disponibles.

    Parámetros:
        catalogo (dict): diccionario de diccionarios de productos.

    Retorna:
        None
    """
    print("\n" + "=" * 50)
    print(f"{'ID':<6}{'PRODUCTO':<20}{'PRECIO':<10}{'STOCK':<6}")
    print("=" * 50)

    # Iteración con for para recorrer el catálogo
    for id_producto, datos in catalogo.items():
        nombre = datos["nombre"]
        precio = datos["precio"]
        stock = datos["stock"]

        # Anidamiento: marca visualmente si el stock está bajo
        if stock == 0:
            estado = " (agotado)"
        elif stock < 5:
            estado = " (stock bajo)"
        else:
            estado = ""

        print(f"{id_producto:<6}{nombre:<20}${precio:<9.2f}{stock}{estado}")

    print("=" * 50 + "\n")


def buscar_producto(catalogo, id_producto):
    """
    Verifica si un producto existe en el catálogo.

    Parámetros:
        catalogo (dict): catálogo de productos.
        id_producto (str): clave del producto a buscar.

    Retorna:
        dict o None: los datos del producto si existe, None si no.
    """
    if id_producto in catalogo:
        return catalogo[id_producto]
    else:
        return None


# Bloque de prueba: se ejecuta solo si corres este archivo directamente,
# no cuando alguien más lo importa con "import catalogo"
if __name__ == "__main__":
    mi_catalogo = cargar_catalogo()
    mostrar_catalogo(mi_catalogo)
