#Lab (Trabajo 1)

print("Elaboracion de sistema de pago de articulos")

#Entrada de datos

dato1 = int(input(" Ingrese el precio de el articulo: "))
dato2 = int(input(" Ingrese el pago del cliente: "))
Vuelto = dato2 - dato1
#Calcular el cambio

if Vuelto > 0:
    print("Su cambio es: ", dato2 - dato1)
    if Vuelto < 0:
        print("Su deuda es de: ", dato1 - dato2)
    if Vuelto == 0:
        print("Su cambio es: ", dato2 - dato1)
else:
    print("El total de su factura es de: ", dato2 - dato1)
    
    
print("Fin del programa")






















