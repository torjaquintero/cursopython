# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.8
# Programa que determina si un alumno ha aprobado una asignatura
# ==============================================================================================

#Captura por teclado las tres notas parciales
print('La primer nota vale el 30% de la nota final')
#con float() permitimos ingresar números con decimales
nota1 = float(input('Digite la primer nota: '))
#Calcula el valor de la nota parcial
nota1 = nota1 * 0.3

print('La segunda nota vale el 30% de la nota final')
nota2 = float(input('Digite la segunda nota: '))
nota2 = nota2 * 0.3

print('La tercer nota vale el 40% de la nota final')
nota3 = float(input('Digite la tercer nota: '))
nota3 = nota3 * 0.4

#la nota final es la suma las tres notas
notaFinal = nota1 + nota2 + nota3

#Comprueba si la nota final es mayor o igual a 3
if notaFinal >= 3:
    #si cumple la condición, aprueba la asignatura
    print('Usted ha aprobado la asignatura de programación')
#en caso contrario, imprime un no aprobado
else:
    print('Lamentablemente, no ha aprobado la asignatura')
