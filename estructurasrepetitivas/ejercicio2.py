# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.2
# Este programa imprime los números enteros que se encuentran almacenados en una lista
# ==============================================================================================

#Una lista es un tipo de variable que almacena
#varios elementos de cualquier tipo de dato.

#A diferencia de las tuplas, las listas pueden
#modificar su tamaño y su contenido

#La lista "numeros" almacena 10 números enteros
#en 10 posiciones de memoria
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#la función len() devuelve como valor, el número
#de elementos que tiene almacenados
elementos = len(numeros)

#la variable "iterable" se incrementa en una unidad
#hasta llegar al número de elementos que haya en la
#lista "numeros"
for iterable in range(elementos):
    #imprime cada una de las posiciones de memoria 
    #que tiene la lista "numeros"
    print(numeros[iterable])
