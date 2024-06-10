"""
Objetivo:
Crear un programa que gestione el inventario de una tienda. El programa permitirá al usuario realizar diferentes 
operaciones en la matriz de inventario, cómo agregar productos, eliminar productos, actualizar cantidades, y consultar el inventario. 
Cada producto tendrá un nombre, una cantidad y un precio.

Requisitos:
Crear una matriz donde cada fila representa un producto y las columnas sean: nombre del producto, cantidad en inventario, y precio por unidad.
Mostrar un menú de opciones al usuario para elegir la operación a realizar.

Implementar las siguientes funciones:
Agregar un nuevo producto.
Eliminar un producto.
Actualizar la cantidad de un producto.
Consultar el inventario completo.
Realizar la operación elegida por el usuario y mostrar los resultados.
Repetir el menú hasta que el usuario elija salir.

"""
Inventario = []

print ("""
Opcion 1 = agregar producto
Opcion 2 = eliminar producto
Opcion 3 = actualizar cantidades
Opcion 4 = consultar el inventario
Opcion 5 = salir

""")
Opcion = ""
indice = -1

while Opcion != 5:
    Opcion = input("Que opcion desea ejecutar ? 1 o 2 o 3 o 4 o 5    ")

    if Opcion == ("1"):  #Opcion 1 es igual a agregar producto y todas sus cosas
        
        Producto = ["nombre","cantidad","precio"]

        Nombre = str(input("Ingrese el nombre de su producto  "))
        Producto[0] = Nombre
        Cantidad = str(input("Ingrese la cantidad de su producto  "))
        Producto[1] = ((", Cantidad ") + (Cantidad))
        Precio = str(input("Ingrese el precio de su producto  "))
        Producto[2] = ((", con precio de  Q") + (Precio))

        Inventario.append(Producto)
        
        indice += 1
        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()
        print (("Este producto ") + (Nombre) + (" es " + (str(indice))))

    if Opcion == ("2"):  
        
        Eliminar = int(input("Que producto eliminara? el primero, segundo, etc.  Responder 0 1 2 o 3, etc      "))
        Inventario.remove(Inventario[Eliminar]) #Aqui va cambiando el grupo cuando se llena y cada
        
        print ("El inventario ahora que se elimino eso se ve asi: ")
        print("")
        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()

    if Opcion == ("3"):  
        
        Actualizar = int(input("Que producto actualizara? el primero, segundo, etc.  Responder 0 1 2 o 3, etc      "))
        Cantidadnueva = str(input("Ingrese la cantidad de su producto  "))
  
        Inventario[Actualizar][1] = ((", Cantidad ") + (Cantidadnueva))

        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()

    if Opcion == ("4"):  #consultar inventario

        print ("El inventario se ve asi: ")
        print("")
        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()
    
    if Opcion == ("5"):  #consultar inventario
        
        Opcion == "5"
        break