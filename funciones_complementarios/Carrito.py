# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:33:56 2026

@author: oscar
"""

"""
Módulo de carrito de compras.

Estructura de datos: lista de tuplas [("ID", cantidad)].
Se eligió esta estructura porque preserva el orden secuencial de adición
de productos (lista) y garantiza la inmutabilidad de los pares
identificador-cantidad (tupla), facilitando su modificación y filtrado.
"""

def agregar_producto(carrito: list, catalogo: dict, id_producto: str, cantidad: int) -> list:
    """
    Agrega un producto al carrito o actualiza su cantidad si ya existe,
    validando la disponibilidad de stock en el catálogo.
    """
    if cantidad <= 0:
        print("Error: La cantidad a agregar debe ser mayor a 0.")
        return carrito

    if id_producto not in catalogo:
        print(f"Error: El producto con ID '{id_producto}' no existe en el catálogo.")
        return carrito

    cantidad_en_carrito = 0
    indice_existente = -1

    for i, (prod_id, cant) in enumerate(carrito):
        if prod_id == id_producto:
            cantidad_en_carrito = cant
            indice_existente = i
            break

    stock_maximo = catalogo[id_producto]["stock"]
    if cantidad + cantidad_en_carrito > stock_maximo:
        disponible_real = stock_maximo - cantidad_en_carrito
        print(f"Error: Stock insuficiente para '{catalogo[id_producto]['nombre']}'. Disponible: {disponible_real}")
        return carrito

    if indice_existente != -1:
        carrito[indice_existente] = (id_producto, cantidad_en_carrito + cantidad)
    else:
        carrito.append((id_producto, cantidad))

    print(f"¡Éxito! Se agregaron {cantidad} unidad(es) de '{catalogo[id_producto]['nombre']}'.")
    return carrito


def eliminar_producto(carrito, id_producto):
    """
    Elimina un producto por completo del carrito de compras.
    """
    if not carrito:
        print("Error: El carrito está vacío.")
        return carrito

    encontrado = False
    nuevo_carrito = []

    for prod_id, cant in carrito:
        if prod_id == id_producto:
            encontrado = True
        else:
            nuevo_carrito.append((prod_id, cant))

    if encontrado:
        print(f"¡Éxito! Producto '{id_producto}' eliminado del carrito.")
        return nuevo_carrito
    else:
        print(f"Error: El producto '{id_producto}' no se encuentra en el carrito.")
        return carrito


def modificar_cantidad(carrito, catalogo, id_producto, nueva_cantidad):
    """
    Modifica directamente la cantidad asignada a un producto en el carrito.
    """
    if nueva_cantidad == 0:
        return eliminar_producto(carrito, id_producto)

    if nueva_cantidad < 0:
        print("Error: La cantidad no puede ser negativa.")
        return carrito

    if id_producto not in catalogo:
        print(f"Error: El producto '{id_producto}' no existe en el catálogo.")
        return carrito

    if nueva_cantidad > catalogo[id_producto]["stock"]:
        print(f"Error: Stock insuficiente. Stock máximo: {catalogo[id_producto]['stock']}")
        return carrito

    for i, (prod_id, cant) in enumerate(carrito):
        if prod_id == id_producto:
            carrito[i] = (id_producto, nueva_cantidad)
            print(f"¡Éxito! Cantidad de '{catalogo[id_producto]['nombre']}' actualizada a {nueva_cantidad}.")
            return carrito

    print(f"Error: El producto '{id_producto}' no está en el carrito.")
    return carrito

