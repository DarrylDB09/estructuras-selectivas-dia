#Definir las constantes
from xml.etree.ElementTree import canonicalize

PRECIO_SENCILLA = 20000
PRECIO_DOBLE = 25000
PRECIO_TRIPLE  = 28000
IMPUESTO_TARGETA = 0.07

#Funcio para calcular el precio
def calcularPrecio(tipo_hamburguesa, medio_pago, cantidad):
    #Definir los precios segun el tipo de hamburgesa
    if  tipo_hamburguesa ==1:
        precio = PRECIO_SENCILLA
        descripcion = "Sencilla"

    elif tipo_hamburguesa ==2:
        precio = PRECIO_DOBLE
        descripcion = "Doble"

    elif tipo_hamburguesa ==3:
        precio = PRECIO_TRIPLE
        descripcion = "Triple"

    else:
        return None # Tipo de hamburguesa no valido

    #Calcular el total sin cargos
    TOTAL_SIN_CARGO = precio * cantidad

    #Aplicar impuesto si el numero de pago es tarjeta
    if medio_pago ==1:
        impuesto = round(TOTAL_SIN_CARGO * IMPUESTO_TARGETA)
    else:
        impuesto = 0
    total = round(TOTAL_SIN_CARGO + impuesto)

    #Retornar datos relevantes
    return descripcion, precio, cantidad, impuesto, total

#Funcion para generar mensaje
def generar_mensaje(descripcion, precio, cantidad, impuesto, total):
    return (f"Tipo de Hamburguesa: {descripcion}\n"
            f"Precio: ${precio}\n"
            f"Cantidad: {cantidad}\n"
            f"Impuesto: ${impuesto}\n"
            f"Total: ${total}\n")
#Funcion para validar los datos
def validar_datos (tipo_hamburguesa, medio_pago, cantidad):
    if 1 <= tipo_hamburguesa <3 and 1 <=medio_pago<=2 and cantidad > 0:
        resultado = calcularPrecio(tipo_hamburguesa, medio_pago, cantidad)

        #Print(resultado: ",resultado)
        descripcion, precio, cantidad, impuesto, total = resultado
        mensaje = generar_mensaje(descripcion, precio,cantidad, impuesto, total)
        print("_________________________\n" + mensaje)
    else:
        print("Verifique las opciones ingresadas, ")


#Entradas
tipo_hamburguesa = int (input("Ingrese tipo de hamburguesa \n1. Sencilla 'n2. Doble \n3.Triple \n"))
medio_pago = int(input("Ingrese medio de pago\n1. Tarjeta \n2. Otro \n"))
cantidad = int(input("Ingrese la cantidad: "))

#Salidas
validar_datos(tipo_hamburguesa,medio_pago,cantidad)