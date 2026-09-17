# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:33:56 2026

@author: oscar
"""

# -*- coding: utf-8 -*-
"""
Módulo de carrito de compras.

Estructura de datos: lista de tuplas -> [(id_producto, cantidad), ...]
Se eligió esta estructura porque el carrito es una secuencia de
compras que necesitamos recorrer y modificar constantemente
(agregar, quitar, sumar cantidades) mientras el cliente sigue
comprando.
"""


def agregar_producto(carrito, catalogo, id_producto, cantidad):
    """
    Agrega un producto al carrito, validando que exista y tenga stock.

    Parámetros:
        carrito (list): lista de tuplas (id_producto, cantidad).
        catalogo (dict): catálogo de productos disponibles.
        id_producto (str): clave del producto a agregar.
        cantidad (int): cantidad que se desea agregar.

    Retorna:
        list: el carrito actualizado (sin cambios si hubo un error).
    """
    # Validación: producto no encontrado
    if id_producto not in catalogo:
        print(f"❌ El producto '{id_producto}' no existe en el catálogo.")
        return carrito

    producto = catalogo[id_producto]

    # Validación: cantidad inválida
    if cantidad <= 0:
        print("❌ La cantidad debe ser mayor a cero.")
        return carrito

    # Validación: stock insuficiente
    if cantidad > producto["stock"]:
        print(f"❌ Stock insuficiente de {producto['nombre']} "
              f"(disponible: {producto['stock']}).")
        return carrito

    # Si el producto ya estaba en el carrito, se suma la cantidad
    # en vez de dejar dos tuplas separadas del mismo producto.
    nuevo_carrito = []
    ya_estaba_en_carrito = False

    for pid, cant in carrito:
        if pid == id_producto:
            nuevo_carrito.append((pid, cant + cantidad))
            ya_estaba_en_carrito = True
        else:
            nuevo_carrito.append((pid, cant))

    if not ya_estaba_en_carrito:
        nuevo_carrito.append((id_producto, cantidad))

    # Se descuenta el stock del catálogo al momento de agregar al carrito
    producto["stock"] -= cantidad

    print(f"✅ Se agregó {cantidad} x {producto['nombre']} al carrito.")
    return nuevo_carrito


def eliminar_producto(carrito, id_producto, catalogo=None, cantidad=None):
    """
    Elimina un producto del carrito, total o parcialmente.

    Parámetros:
        carrito (list): lista de tuplas (id_producto, cantidad).
        id_producto (str): producto a eliminar.
        catalogo (dict, opcional): si se pasa, se regresa el stock
                                    liberado al catálogo.
        cantidad (int, opcional): cuánto quitar; si se omite, se
                                   elimina el producto por completo.

    Retorna:
        list: el carrito actualizado.
    """
    # Validación: carrito vacío
    if not carrito:
        print("❌ El carrito ya está vacío, no hay nada que eliminar.")
        return carrito

    nuevo_carrito = []
    encontrado = False

    for pid, cant in carrito:
        if pid == id_producto:
            encontrado = True

            if cantidad is None or cantidad >= cant:
                # Elimina el producto por completo del carrito
                if catalogo is not None and pid in catalogo:
                    catalogo[pid]["stock"] += cant
                print(f"🗑️ Se eliminó {pid} del carrito por completo.")
                # No se agrega al nuevo carrito (se descarta)
            else:
                # Elimina solo una parte de la cantidad
                restante = cant - cantidad
                if catalogo is not None and pid in catalogo:
                    catalogo[pid]["stock"] += cantidad
                nuevo_carrito.append((pid, restante))
                print(f"🗑️ Se quitaron {cantidad} unidades de {pid}.")
        else:
            nuevo_carrito.append((pid, cant))

    # Validación: producto no encontrado en el carrito
    if not encontrado:
        print(f"❌ El producto '{id_producto}' no está en el carrito.")

    return nuevo_carrito


def mostrar_carrito(carrito, catalogo):
    """
    Imprime el contenido actual del carrito de forma legible.

    Parámetros:
        carrito (list): lista de tuplas (id_producto, cantidad).
        catalogo (dict): catálogo de productos, para mostrar nombres.

    Retorna:
        None
    """
    if not carrito:
        print("\n🛒 El carrito está vacío.")
        return

    print("\n" + "-" * 40)
    print("🛒 CARRITO ACTUAL")
    print("-" * 40)

    # Iteración con for para recorrer el carrito
    for id_producto, cantidad in carrito:
        producto = catalogo.get(id_producto)
        if producto is not None:
            precio = producto["precio"]
            print(f"{producto['nombre']:<20} x{cantidad:<3} "
                  f"${precio * cantidad:.2f}")

    print("-" * 40 + "\n")


# Bloque de prueba: se ejecuta solo si corres este archivo directamente
if __name__ == "__main__":
    from catalogo import cargar_catalogo

    catalogo_prueba = cargar_catalogo()
    mi_carrito = []

    mi_carrito = agregar_producto(mi_carrito, catalogo_prueba, "P001", 2)
    mi_carrito = agregar_producto(mi_carrito, catalogo_prueba, "P003", 1)
    mostrar_carrito(mi_carrito, catalogo_prueba)

    mi_carrito = eliminar_producto(mi_carrito, "P001", catalogo_prueba,
                                    cantidad=1)
    mostrar_carrito(mi_carrito, catalogo_prueba)