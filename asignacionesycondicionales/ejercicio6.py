# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.6
# Programa que captura la edad de una persona y luego 
# imprime en pantalla si es menor o mayor de edad
# ==============================================================================================

#Captura el nombre de la persona
nombre = input('Digite su nombre: ')

#Captura la edad como número entero
edad = int(input('Cual es su edad: '))

#verifica si la edad es igual o mayor a 18
if edad >= 18:
    #si se cumple la condición
    print(nombre, 'es mayor de edad')
else:
    #si no se cumple la condición
    print(nombre, ' es menor de edad')
