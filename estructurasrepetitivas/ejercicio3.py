# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.3
# Este programa imprime en pantalla un menú de opciones para la gestíon de un hotel
# ==============================================================================================

#Imprime un saludo de bienvenida 
print('Software de gestión de un hotel')

#almacena en variables las opciones del menú
opcion1 = 'Registrar un nuevo huesped'
opcion2 = 'Mostrar huespedes por habitación'
opcion3 = 'Realizar check out'
opcion4 = 'Ingresar pedido de room service'

#crea una lista llamada menú con todas las opciones
menu = [opcion1, opcion2, opcion3, opcion4]

#el iterador i recorre todas las posiciones de la
#lista para imprimir el menú de opciones
for i in range(len(menu)):
    #como las posiciones de la lista se enumeran
    #desde 0, se suma una unidad para que en pantalla
    #se enumeren las opciones a partir de 1
    print(i+1, menu[i])

#se ingresa por teclado la opción elegida por el usuario
eleccion = int(input('Elija una opcion: '))
