# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:03:35 2026

@author: hugoc
"""

# -*- coding: utf-8 -*-
import catalogo
import registro_ventas


def ejecutar_menu():
    # 1. Cargar datos iniciales
    micatalogo = catalogo.cargar_catalogo()
    historial_ventas = []
    print("\n\033[34m" + "🏪TIENDA PARANGARICUTIRIMICUARO🏪".center(40) + "\033[0m")    
    print("-" * 40)
    print("\n🏪🏪🏪 MENÚ PRINCIPAL 🏪🏪🏪")
    print("\n1.🛍️ Ver catálogo de productos")
    print("\n2.🛒 Registrar una venta      ")
    print("\n3.🧾 Ver historial de ventas  ")
    print("\n0.🔚 Salir                    ")
    print("-" * 40)
    # 2. Bucle principal del menú
    while True:

        opcion = input("Selecciona una opción: ")

        # OPCIÓN 1: Mostrar productos
        if opcion == "1":
            catalogo.mostrar_catalogo(micatalogo)

        # OPCIÓN 2: Realizar una venta simple1
        
        elif opcion == "2":
            lista_productos = []
            total_venta = 0.0

            print("\n--- NUEVA VENTA ---")
            
            while True:
                id_p = input("Ingresa ID del producto (o ENTER para cobrar/terminar): ").strip().upper()
                
                # Si presiona ENTER, sale de pedir productos
                if id_p == "":
                    break

                producto = catalogo.buscar_producto(micatalogo, id_p)

                if producto is not None:
                    cantidad = int(input(f"¿Cuántos {producto['nombre']}s llevará?: "))

                    if cantidad <= producto["stock"]:
                        # Restamos stock y sumamos al total
                        producto["stock"] -= cantidad
                        total_venta += producto["precio"] * cantidad
                        
                        # Guardamos en la lista
                        lista_productos.append((id_p, cantidad))
                        print(f"👍Producto agregado: {producto['nombre']} x{cantidad}")
                    else:
                        print("  ❌ No hay suficiente stock.")
                else:
                    print("  ❌ Producto no encontrado.")

            # Si agregó al menos un producto, genera el ticket
            if lista_productos:
                ticket = registro_ventas.generar_ticket(lista_productos, micatalogo, total_venta)
                registro_ventas.guardar_historial_ventas(historial_ventas, ticket)
            else:
                print("⚠️ Venta cancelada (sin productos).")

        # OPCIÓN 3: Mostrar ventas realizadas
        elif opcion == "3":
            print("\n--- HISTORIAL DE VENTAS ---")
            if not historial_ventas:
                print("Aún no hay ventas registradas.")
            else:
                for folio, fecha, total in historial_ventas:
                    print(f"Folio: {folio} | Fecha: {fecha} | Total: ${total:.2f}")

        # OPCIÓN 0: Salir del programa
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


# Permite ejecutar el menú directamente desde la terminal
if __name__ == "__main__":
    ejecutar_menu()