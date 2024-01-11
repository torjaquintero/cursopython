# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.1
# Este programa imprime en pantalla un saludo a los amigos guardados en una tupla
# ==============================================================================================

#Una tupla es un tipo de variable que almacena
#varios elementos de cualquier tipo de dato
tuplaAmigos = ('Marta', 'Juan', 'Fabio')

#la instrucción for se repetirá tantas veces como
#sea el número de elementos dentro de la tupla
for nombre in tuplaAmigos:
    #el iterador "nombre" asumirá el valor de 
    #cada posicion de memoria dentro de la tupla
    print('Hola', nombre, ' bienvenid@ al curso')
