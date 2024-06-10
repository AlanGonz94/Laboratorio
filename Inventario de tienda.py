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

Producto = ["nombre","cantidad","precio"]

print ("""
Opcion 1 = agregar producto
Opcion 2 = eliminar producto
Opcion 3 = actualizar cantidades
Opcion 4 = consultar el inventario
Opcion 5 = salir

""")
Opcion = ""

while Opcion != 5:
    Opcion = input("Que opcion desea ejecutar ? 1 o 2 o 3 o 4 o 5    ")

    if Opcion == ("1"):  #Opcion 1 es igual a agregar producto y todas sus cosas
        
        Nombre = str(input("Ingrese el nombre de su producto  "))
        Producto[0] = Nombre
        Cantidad = str(input("Ingrese la cantidad de su producto  "))
        Producto[1] = ((", Cantidad ") + (Cantidad))
        Precio = str(input("Ingrese el precio de su producto  "))
        Producto[2] = ((", con precio de  Q") + (Precio))

        Inventario.append(Producto)
        indice = 0
        indice += 1
        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()
        print (("Este producto ") + (Nombre) + (" es " + (str(indice))))

    if Opcion == ("2"):  
        
        Eliminar = ("Que producto eliminara? el primero, segundo, etc.  Responder 1 2 o 3, etc      ")
        for Producto in Inventario: #eligiendo grupo por grupo en la lista de grupos
            for x in range(0, 3): #metiendolos en los espacios 2,3,4 de la lista
                Producto[Producto] = Inventario.remove([Eliminar]) #Aqui va cambiando el grupo cuando se llena y cada
                
        for Producto in Inventario:
            for cosa in Producto:
                print(cosa, end=" ")  #esto mostrara como se mira inventario actualizado
            print ()



"""
#Crear una lista agarando los paises que no son cabezas de grupo
paises_disponibles = [pais for pais in paises if pais not in [Cabeza1, Cabeza2, Cabeza3, Cabeza4, Cabeza5, Cabeza6, Cabeza7, Cabeza8]]

# revolver las posiciones en la nueva lista
random.shuffle(paises_disponibles)

# Asignar aleatoriamente los demás países a los grupos
indice = 0
for grupo in Grupos: #eligiendo grupo por grupo en la lista de grupos
    for x in range(2, 5): #metiendolos en los espacios 2,3,4 de la lista
        grupo[x] = paises_disponibles[indice] #Aqui va cambiando el grupo cuando se llena y cada
        indice += 1#pais de la lista de disponibles va avanzando al siguiente que haya recordando que tienen un nuevo orden

for Grupo in Grupos:
        for lugar in Grupo:
            print(lugar, end=" ")  #esto mostrara como se mira grupos actualizado
        print ()
"""