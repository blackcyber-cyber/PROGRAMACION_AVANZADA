
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
    "Remate": 0.50,
    "Porcentaje": 0.40,
    "Ninguno": 0.0,
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


    Subtotal = 0.0

def aplicar_descuento(subtotal, tipo_de_descuento):
    """
    Se aplicaran los descuentos sobre el subtotal de la compra.
     - Parametros:
         subtotal (del tipo float): Es la cantidad sobre la que se aplica el descuento.
         tipo_de_descuento (tipo cadena (string)): Es el tipo "Regla" a aplicar, que se encuentra
         en DESCUENTO: ("Remate", "Porcentaje", "Ninguno").
         
         Retornando un float con el total final (con descuento incluido)
         """
         
         # Validación del subtotal
    if subtotal <= 0:
        print("No hay descuento aplicado a su compra, favor de elegir productos")
        return 0.0


# Condiciones para aplicar descuentos

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
 
             
             
    

    if not carrito:
        print("El carrito está vacío: Subtotal igual a 0")
        return Subtotal

#Verificación de los productos del carrito
    for id_producto, cantidad in carrito:
        if id_producto in catalogo:
            precio = catalogo[id_producto]['precio']
            Subtotal += precio * cantidad
        else:
        # Comprobación para saber si hay stock de los productos
            print(f"Aviso: EL producto{id_producto} que selecciono no existe")
    return Subtotal

