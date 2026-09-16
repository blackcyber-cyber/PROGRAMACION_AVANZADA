# -*- coding: utf-8 -*-
''' Esta rama es encargada de crear y validar los totales, descuentos 
# (y las reglas de estos mismos)
 
Rama encargada de:
    1. Calcular el subtotal de las compras
    2. Aplicar descuentos 
    3. Generar el Ticket de compra con el descuento o no aplicado


'''

from datetime import date
'''Reglas de descuento:'''

DESCUENTO = {
    "Remate": 0.50,
    "Porcentaje": 0.40
    "Ninguno": 0.0,
    }

# Aplicacion de folio para la identificación de cada ticket impreso

contador_folio = 0


def calcular_subtotal(carrito, catalogo):
    "Calcula el Subtotal de los productos añadidos al carrito"

Subtotal = 0.0

# Cuando el carrito esta vacio

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
