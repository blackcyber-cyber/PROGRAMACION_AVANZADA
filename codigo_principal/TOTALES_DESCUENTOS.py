
# -*- coding: utf-8 -*-
"""
Esta rama es encargada de crear y validar los totales, descuentos
(y las reglas de estos mismos).
 
Rama encargada de:
    1. Calcular el subtotal de las compras
    2. Aplicar descuentos
    3. Generar el Ticket de compra con el descuento o no aplicado
"""
 
from datetime import date

 
# Reglas de descuento:

'''Reglas de descuento:'''


DESCUENTO = {
    "Remate ¡2x1! ": 0.50,
    "Porcentaje -50%": 0.40,
    "Ninguno N/A": 0.0,
}
 
# Aplicacion de folio para la identificación de cada ticket impreso
contador_folio = 0
 
 
def calcular_subtotal(carrito, catalogo):
    """Calcula el Subtotal de los productos añadidos al carrito"""
    subtotal = 0.0
 
    # Cuando el carrito esta vacio
    if not carrito:
        print("El carrito está vacío: Subtotal igual a 0")
        return subtotal
 
    # Verificación de los productos del carrito
    for id_producto, cantidad in carrito:
        if id_producto in catalogo:
            precio = catalogo[id_producto]["precio"]
            subtotal += precio * cantidad
        else:
            # Aviso si el producto no existe en el catálogo (no corta el ciclo)
            print(f"Aviso: el producto {id_producto} que seleccionó no existe")
 
    return subtotal


    subtotal = 0.0

def aplicar_descuento(subtotal, tipo_de_descuento):
    """
    Se aplicaran los descuentos sobre el subtotal de la compra.
     - Parametros:
         subtotal (del tipo float): Es la cantidad sobre la que se aplica el
         descuento.
         tipo_de_descuento (tipo cadena (string)): Es el tipo "Regla" a
         aplicar, que se encuentra
         en DESCUENTO: ("Remate", "Porcentaje", "Ninguno").
         
         Retornando un float con el total final (con descuento incluido)
         """
         
         # Validación del subtotal
    if subtotal <= 0:
        print("No hay descuento aplicado a su compra, favor de elegir productos")
        return 0.0


 # Condiciones a las que se les aplicará descuento
    if tipo_de_descuento in DESCUENTO:
        porcentaje = DESCUENTO[tipo_de_descuento]
        total = subtotal * (1 - porcentaje)
    elif tipo_de_descuento is None:
        # Se aplica cuando no se especificó el descuento a aplicar
        total = subtotal
    else:
        # Cuando se quiere aplicar un descuento no registrado
        print(f'Tipo de descuento "{tipo_de_descuento}" no reconocido, intente de nuevo')
        total = subtotal
 
    return round(total, 2)
 
 
def generar_ticket(carrito, catalogo, total):
    """
    Se genera el ticket de compra con los datos de subtotal y total de la compra.
    En el que se visualizará el producto y la cantidad adquirida.
 
    Retorna una tupla inmutable con: folio, fecha y total.
    """
    global contador_folio
    contador_folio += 1
    folio = f"F{contador_folio:03d}"
    fecha = date.today().isoformat()
 
    print("\n---- TICKET DE COMPRA ----")
    print(f"Folio: {folio}")
    print(f"Fecha: {fecha}")
 
    # Armamos el ticket con los productos que se seleccionaron
    for id_producto, cantidad in carrito:
        if id_producto in catalogo:
            nombre = catalogo[id_producto]["nombre"]
            precio = catalogo[id_producto]["precio"]
            print(f"  {nombre} x{cantidad} - ${precio * cantidad:.2f}")
 
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------\n")
 
    # Como no se puede cambiar la compra una vez se imprimió el ticket,
    # se retorna como una tupla (registro inmutable).
    return (folio, fecha, total)
 
 
# Bloque de prueba manual del módulo
if __name__ == "__main__":
    catalogo_prueba = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Agua 600ml", "precio": 15.0, "stock": 50},
    }
    carrito_prueba = [("P001", 2), ("P002", 3)]
 
    sub = calcular_subtotal(carrito_prueba, catalogo_prueba)
    print(f"Subtotal: ${sub:.2f}")
 
    total_con_descuento = aplicar_descuento(sub, "Remate")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
 
    generar_ticket(carrito_prueba, catalogo_prueba, total_con_descuento)
 

   
