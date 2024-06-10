"""
Objetivo:
Crear un programa que permita convertir temperaturas entre Celsius y Fahrenheit. 
El programa debe proporcionar un menú interactivo para que el usuario elija la conversión deseada.

Requisitos:
Crear un menú con opciones para:
Convertir de Celsius a Fahrenheit
Convertir de Fahrenheit a Celsius
Salir del programa

Implementar las fórmulas de conversión:
De Celsius a Fahrenheit
De Fahrenheit a Celsius
Validar que el usuario ingrese un número válido para la temperatura.
Manejar entradas no válidas adecuadamente.

"""
Finalizar = False
si = False

print ("""
Este programa permite convertir temperaturas entre Celsius y Fahrenheit.
       Las instrucciones son las siguientes:
    Ingresa la temperatura que deseas, puede ser un numero entero o decimal.
    Y se te devolvera la misma temperatura convertida a grados celsius o fahrenheit,
    segun como lo elijas.

""")

while Finalizar == False:

    print ("""
Seleccione que conversion desea realizar
Opcion A: Convertir grados celsius a fahrenheit.
Opcion B: Convertir grados fahrenheit a celsius.
Opcion C: Terminar.
                      
""")
    
    while si == False:
        Opcion = input("Que opcion desea ejecutar ? A o B o C    ")
        if Opcion == "A" or Opcion == "B":
            si = True
            print ("")
        elif Opcion == "C":
            si = True
            Finalizar = True
        else:
            print ("Escriba solo A o B o C")
            print ("")

    if Finalizar != True:
        Grados = float(input("Ingrese los grados que quiere convertir "))

        if Opcion == ("A"):
        #formula de celsius a fahrenheit
            Grados_fahrenheit = ((Grados * (9/5)) + 32)
            print (("La conversion de grados celsius a fahrenheit es:  ") + str(Grados_fahrenheit))
            print ("")
            si = False
            Terminar = input("Desea continuar? Si o No  ")
            if Terminar == "No":
                Finalizar = True

        if Opcion == ("B"):
        #formula de fahrenheit a celsius
            Grados_celcius = ((Grados - 32) * (5/9))
            print (("La conversion de grados fahrenheit a celsius es:  ") + str(Grados_celcius))
            si = False
            Terminar = input("Desea continuar? Si o No  ")
            if Terminar == "No":
                Finalizar = True
