# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.5
# Programa que captura por el teclado tres notas de una asignatura.
# Calcula el promedio y lo muestra en la pantalla
# ==============================================================================================

#Se capturan las notas en variables independientes

nota1 = float(input('Digite primer nota: '))
nota2 = float(input('Digite segunda nota: '))
nota3 = float(input('Digite tercer nota: '))

#Calcula el promedio de las notas
#con round() se obtiene un número con dos decimales
#la sintaxis es round(variable, numerodedecimales)
promedio = round((nota1 + nota2 + nota3)/3, 2)

#Imprime el resultado
print('El promedio de las notas es: ', promedio)
