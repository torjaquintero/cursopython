# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.4
# Programa que almacena en una lista los datos personales del usuario y luego los imprime en pantalla
# ==============================================================================================

#Guarda en variables los textos con las peticiones de
#datos al usuario y los guarda en la lista cuestionario
pregunta1 = '1. Digite su nombre: '
pregunta2 = '2. Digite su número de identificación: '
pregunta3 = '3. Digite su número de teléfono: '
cuestionario = [pregunta1, pregunta2, pregunta3]

#crea una lista vacía para almacenar los datos de usuario
datosPersonales = []

#en cada iteración guarda el dato que pide cada elemento
#de la lista cuestionario
for i in range(len(cuestionario)):
    dato = input(cuestionario[i])
    #con el método .append se ingresa y almacena un dato
    #en la lista datosPeronales
    datosPersonales.append(dato) 

#recorre todas las posiciones de la lista de datos personales
for i in range(len(datosPersonales)):
    if i == 0: #imprime la posicion 0 correspondiente al nombre
        print('Su nombre es: ', datosPersonales[i])
    elif i == 1: #imprime la posicion 1 de la identificación
        print('Su identificación es: ', datosPersonales[i])
    else: #imprime la posicion 2 que corresponde al teléfono
        print('Su teléfono es: ', datosPersonales[i])
