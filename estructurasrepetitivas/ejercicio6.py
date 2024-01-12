# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.6
# Programa de gestión de una agenda telefónica
# ==============================================================================================

#almacena en variables las opciones del menú
opcion1 = 'Guardar nuevo contacto'
opcion2 = 'Editar contacto'
opcion3 = 'Eliminar contacto'
opcion4 = 'Salir'

#guarda en la lista menú todas las opciones
menu = [opcion1, opcion2, opcion3, opcion4]

#el iterador i 
for i in range(len(menu)):
    print(i+1, menu[i])

eleccion = int(input('Elija una opcion: '))


if opcion == 1:
    print('Usted a elegido la opcion 1')
elif opcion == 2:
    print('Usted a elegido la opcion 2')
elif opcion == 3:
    print('Usted a elegido la opcion 3')
elif opcion == 4:
    print('Hasta pronto')
else:
    print('Opcion no disponible')
