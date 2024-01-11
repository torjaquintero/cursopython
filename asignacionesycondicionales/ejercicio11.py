# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.11
# Programa que imprime un menú de opciones y captura la elección del usuario a través del teclado
# ==============================================================================================

#imprime menú en pantalla
print('1. Ingresar datos personales')
print('2. Ingresar datos financieros')
print('3. Ingresar datos educativos')
print('4. Ingresar datos familiares')
print('5. Salir del programa')

#captura por teclado la opción elegida por el usuario
opcion = int(input('Elija una opción de su preferencia: '))

#si la opcion se encuentra dentro del rango de 1 a 5
if opcion > 0 and opcion < 5:
    #segun el valor de la opción imprime un mensaje
    if opcion == 1:
        print('Bienvenido al menú de datos personales')
    elif opcion == 2:
        print('Bienvenido al menú de datos financieros')
    elif opcion == 3:
        print('Bienvenido al menú de datos educativos')
    elif opcion == 4:
        print('Bienvenido al menú de datos familiares')
    else:
        print('Hasta pronto! ')
else:
    print('No es una opcion válida')
