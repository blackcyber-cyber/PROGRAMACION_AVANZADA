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
contador_folios = 0


def generar_folio():
    """Genera un folio único incremental tipo F001, F002, etc."""
    global contador_folios
    contador_folios += 1
    return f"F{contador_folios:05d}"


def pago_carrito(total_efectivo):
    """Solicita el pago en efectivo y calcula el cambio correspondiente."""
    
    while True:
        try:
            efectivo = float(input("¿Con cuánto pagará?: $"))
            if efectivo < total_efectivo:
                print(f"Monto insuficiente. El total es de ${total_efectivo:.2f}")
                continue
            cambio = efectivo - total_efectivo
            return efectivo, cambio
        except ValueError:
            print("Por favor, ingrese un número válido.")


def generar_ticket(carrito, catalogo, total):
    """Genera un ticket de venta inmutable y muestra el resumen."""
    if not carrito:
        print("No se puede generar un ticket: el carrito está vacío.")
        return None
    print(f"El total a pagar es de  ${total:.2f}")
    efectivo, cambio = pago_carrito(total)
    folio = generar_folio()
    fecha = date.today().isoformat()

    print("\n"* 4 + "-" * 40)
    print("\033[3;34m" + "TIENDA PARANGARICUTIRIMICUARO".center(40) + "\033[0m")
    print("-" * 40)
    print("\033[34m" + "TICKET DE VENTA".center(40) + "\033[0m")
    print("\033[1m" + f"Folio: {folio}".center(40) + "\033[0m")
    print("\033[1m" + f"Fecha: {fecha}".center(40) + "\033[0m")
    print("-" * 40)

    # Mostrar productos en el carrito
    for id_producto, cantidad in carrito:
        producto = catalogo.get(id_producto)
        if producto is not None:
            subtotal_linea = producto["precio"] * cantidad
            nombre = producto['nombre']
            print(f"\033[90m {nombre:<20} x{cantidad:<3} ${subtotal_linea:.2f}\033[0m")

    print("-" * 40)
    print(f"TOTAL: ${total:.2f}")
    print("-" * 40)
    print("Pago en efectivo".center(40))
    # Proceso de pago (se llama una sola vez)
    print(f"Efectivo: ${efectivo:.2f}")
    print(f"Cambio:   ${cambio:.2f}")
    print("-" * 40 )
    print("\033[7;32m" + "PRODUCTOS PAGADOS".rjust(40) + "\033[0m")
    print("-" * 40 )
    print("\033[34m" + "GRACIAS POR SU COMPRA".center(40) + "\033[0m")
    print("-" * 40 + "\n")

    # Registro inmutable
    registro_venta = (folio, fecha, total)
    return registro_venta


def guardar_historial_ventas(historial, registro_venta):
    """Agrega un registro de venta a la lista de historial general."""
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