# -*- coding: utf-8 -*-
"""
Módulo de catálogo de productos.
"""

def cargar_catalogo():
    """
    """
    catalogo = {
        "P001": {"nombre": "🍵Café", "precio": 20.0, "stock": 20},
        "P002": {"nombre": "🫖Té", "precio": 25.0, "stock": 20},
        "P003": {"nombre": "🍪Galletas", "precio": 24.0, "stock": 40},
        "P004": {"nombre": "🍫Chocolate", "precio": 50.5, "stock": 10},
        "P005": {"nombre": "🫗Agua embotellada", "precio": 16.0, "stock": 60},
        "P006": {"nombre": "🥤Refresco 2L", "precio": 29.5, "stock": 40},
        "P007": {"nombre": "🍟Sabritas", "precio": 20.0, "stock": 70},
<<<<<<< Updated upstream
        "P008": {"nombre": "🍬Dulces", "precio": 3.0, "stock": 80}
=======
        "P008": {"nombre": "🍬Dulces", "precio": 3.0, "stock": 80},
>>>>>>> Stashed changes
    }
    return catalogo


def mostrar_catalogo(catalogo):
    """
    Imprime una tabla con los productos disponibles.
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
    """
    if id_producto in catalogo:
        return catalogo[id_producto]
    else:
        return None


# Bloque de prueba: se ejecuta solo si corres este archivo directamente,
# no cuando alguien más lo importa con "import catalogo"
if __name__ == "__main__":
    el_catalogo = cargar_catalogo()
    mostrar_catalogo(el_catalogo)
