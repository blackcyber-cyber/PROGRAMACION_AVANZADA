# -*- coding: utf-8 -*-
"""
Módulo de registro de ventas y generación de tickets.

Estructura de datos: tupla.
Se eligió tupla porque un ticket ya emitido es un registro histórico
que NO debe modificarse después de creado (folio, fecha y total son
inmutables una vez que la venta se cerró).
"""

from datetime import date

# Contador simple para generar folios consecutivos.
# En un programa más grande, esto vendría de una base de datos.
_contador_folios = 0


def _generar_folio():
    """
    Genera un folio único incremental tipo F001, F002, etc.

    Retorna:
        str: folio generado.
    """
    global _contador_folios
    _contador_folios += 1
    return f"F{_contador_folios:03d}"


def generar_ticket(carrito, catalogo, total):
    """
    Genera un ticket de venta inmutable y muestra el resumen.

    Parámetros:
        carrito (list): lista de tuplas (id_producto, cantidad).
        catalogo (dict): catálogo de productos para obtener nombres/precios.
        total (float): total ya calculado con descuentos aplicados.

    Retorna:
        tuple: registro inmutable de la venta con la forma
               (folio, fecha, total)
    """
    if not carrito:
        print("No se puede generar un ticket: el carrito está vacío.")
        return None

    folio = _generar_folio()
    fecha = date.today().isoformat()  # ej. "2026-09-15"

    print("\n" + "-" * 40)
    print(f"TICKET DE VENTA  Folio: {folio}")
    print(f"Fecha: {fecha}")
    print("-" * 40)

    # Iteración con for para mostrar cada producto vendido
    for id_producto, cantidad in carrito:
        producto = catalogo.get(id_producto)
        if producto is not None:
            subtotal_linea = producto["precio"] * cantidad
            print(f"{producto['nombre']:<20} x{cantidad:<3} "
                  f"${subtotal_linea:.2f}")

    print("-" * 40)
    print(f"TOTAL: ${total:.2f}")
    print("-" * 40 + "\n")

    # Tupla inmutable: una vez generado el ticket, no se puede alterar
    registro_venta = (folio, fecha, total)
    return registro_venta


def guardar_historial_ventas(historial, registro_venta):
    """
    Agrega un registro de venta a la lista de historial general.

    Parámetros:
        historial (list): lista donde se acumulan las tuplas de venta.
        registro_venta (tuple): tupla (folio, fecha, total) a agregar.

    Retorna:
        list: historial actualizado.
    """
    if registro_venta is not None:
        historial.append(registro_venta)
    return historial


# Bloque de prueba
if __name__ == "__main__":
    catalogo_prueba = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P003": {"nombre": "Galletas", "precio": 28.5, "stock": 30},
    }
    carrito_prueba = [("P001", 2), ("P003", 1)]
    total_prueba = 45.0 * 2 + 28.5 * 1

    historial_ventas = []
    ticket = generar_ticket(carrito_prueba, catalogo_prueba, total_prueba)
    guardar_historial_ventas(historial_ventas, ticket)

    print("Historial acumulado:", historial_ventas)
