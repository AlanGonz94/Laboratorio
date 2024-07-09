"""
Crear un programa que permita al usuario ingresar una matriz de números y 
luego realizar varias operaciones y análisis sobre esta matriz.

1. Pedir al usuario que ingrese las dimensiones de la matriz (número de filas y columnas).
2. Solicitar al usuario que ingrese los elementos de la matriz fila por fila.
3. Implementar funciones para:
    Calcular la suma de todos los elementos de la matriz.
    Encontrar el número máximo y mínimo en la matriz.
    Calcular la suma de cada fila y cada columna.
4. Mostrar los resultados de las operaciones y análisis.

"""

matriz = []

print ("""
En este programa deberes ingresar como quieres que sea tu matriz
 * El numero de filas (horizontal)
 * El numero de columnas (vertical)
       

""")

numfilas = int(input("Cuantas filas desea?  "))
numcolumnas = int(input("Cuantas columnas desea?   "))


for x in range(0,numfilas):

    matriz.append([])#empezar a hacer los espacios en la lista para llenarlos de mas espacios despues

for y in matriz:#Lista por lista dentro de la matriz se va añadiendo la cantidad de espacios que dijo el usuario

    for x in range(0,numcolumnas):

        y.append([])

print("""
      
      Asi se mira la matriz segun tus instrucciones
      
      """)

for x in matriz:#mostrar la matriz
    print(x)
print()





#meter cosas en x
for cosa, x in enumerate(matriz):
    for sub_indx, y in enumerate(range(1,len(x)+1)):

        dato = int(input(f"Ingrese el dato {y} de la fila {cosa+1}: "))
        x[sub_indx].append(dato)

print("Así se ven los datos de tu matriz:") 
for x in matriz:
    print(x)

sum_dats = 0
mayor = 0

for x in matriz:
    for y in x:
        datox = y[0]

        if datox > mayor:
            mayor = datox

        sum_dats += y[0]
minimo = mayor

for x in matriz:
    for y in x:

        datox = y[0]

        if datox < minimo:
            minimo = datox

for fila,x in enumerate(matriz):

    suma_fila = 0
    for cosa,y in enumerate(x):

        datox = y[0]
        suma_fila += datox

    print(f"La suma de la fila {fila+1} es:",suma_fila)

print()

for x in range(0,len(matriz)):

    suma_columna = 0

    for y in matriz:

        suma_columna += y[x][0]

    print(f"La suma de la columna {x+1} es:",suma_columna)

print()

print("La suma de todos los datos de la matriz es:",sum_dats)
print("El número mayor de la matriz es:",mayor)
print("El número menor de la matriz es:",minimo)
