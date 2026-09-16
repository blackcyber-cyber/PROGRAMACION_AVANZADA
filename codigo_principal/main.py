# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:03:35 2026

@author: hugoc
"""
"""
Módulo principal del punto de venta.
"""

import catalogo
import Carrito
import TOTALES_DESCUENTOS as descuentos
import registro_ventas

# 1. Cargar datos e inicializar variables del sistema
micatalogo = catalogo.cargar_catalogo()
lista_productos = []
historial_ventas = []

# 2. Bucle principal del menú
while True:
    print("\n\033[34m" + "🏪BIENVENIDO A TIENDA PARANGARICUTIRIMICUARO🏪".center(40) + "\033[0m")
    print("-" * 40)
    print("🏪🏪🏪 MENÚ PRINCIPAL 🏪🏪🏪")
    print("1.🛍️ Ver catálogo de productos")
    print("2.➕ Agregar producto al carrito")
    print("3.➖ Eliminar producto del carrito")
    print("4.🛒 Ver carrito")
    print("5.💳 Cerrar venta y aplicar descuento")
    print("6.🧾 Ver historial de ventas")
    print("0.🔚 Salir")
    print("-" * 40)
    opcion = input("Selecciona una opción: ").strip()

    # OPCIÓN 1: Ver catálogo
    if opcion == "1":
        catalogo.mostrar_catalogo(micatalogo)

    # OPCIÓN 2: Agregar productos
    elif opcion == "2":
        print("\n--- AGREGAR PRODUCTOS ---")
        while True:
            id_p = input("Ingresa ID del producto (o ENTER para terminar): ").strip().upper()

            if id_p == "":
                break
            try:
                cantidad = int(input(f"¿Cuántos {id_p} llevará?: "))
                lista_productos = Carrito.agregar_producto(
                    lista_productos, micatalogo, id_p, cantidad
                )
            except ValueError:
                print("  ❌ La cantidad debe ser un número entero.")

    # OPCIÓN 3: Eliminar productos
    elif opcion == "3":
        id_p = input("Ingresa ID del producto a eliminar: ").strip().upper()
        respuesta = input("¿Eliminar todo (T) o solo una cantidad (C)?: ").strip().upper()

        if respuesta == "C":
            try:
                cantidad = int(input("¿Cuántos quieres quitar?: "))
                lista_productos = Carrito.eliminar_producto(
                    lista_productos, id_p, micatalogo, cantidad
                )
            except ValueError:
                print("  ❌ La cantidad debe ser un número entero.")
        else:
            lista_productos = Carrito.eliminar_producto(
                lista_productos, id_p, micatalogo
            )

    # OPCIÓN 4: Mostrar carrito
    elif opcion == "4":
        Carrito.mostrar_carrito(lista_productos, micatalogo)

    # OPCIÓN 5: Cerrar venta y cobrar
    elif opcion == "5":
        if not lista_productos:
            print("⚠️ Venta cancelada (sin productos en el carrito).")
        else:
            subtotal = descuentos.calcular_subtotal(lista_productos, micatalogo)
            print(f"\nSubtotal: ${subtotal:.2f}")

            print("\nTipos de descuento disponibles:")
            for nombre in descuentos.DESCUENTO:
                print(f"  - {nombre}")

            tipo_descuento = input("¿Qué descuento desea aplicar? (ENTER para ninguno): ").strip()
            if tipo_descuento == "":
                tipo_descuento = None

            total_venta = descuentos.aplicar_descuento(subtotal, tipo_descuento)

            ticket = registro_ventas.generar_ticket(lista_productos, micatalogo, total_venta)

            if ticket is not None:
                registro_ventas.guardar_historial_ventas(historial_ventas, ticket)
                lista_productos = []  # Vaciar carrito tras cobro exitoso

    # OPCIÓN 6: Historial
    elif opcion == "6":
        print("\n--- HISTORIAL DE VENTAS ---")
        if not historial_ventas:
            print("Aún no hay ventas registradas.")
        else:
            for folio, fecha, total in historial_ventas:
                print("-" * 60)
                print(f"Folio: {folio} | Fecha: {fecha} | Total: ${total:.2f}")

    # OPCIÓN 0: Salir
    elif opcion == "0":
        print("\n¡Gracias por usar el sistema!")
        break

    else:
        print("❌ Opción no válida, intenta de nuevo.")