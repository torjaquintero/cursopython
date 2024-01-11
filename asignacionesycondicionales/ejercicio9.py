# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.9
# Programa que determina si una persona es niña, joven, adulta o de la tercera edad
# ==============================================================================================

edad = int(input('Cual es su edad: '))
if edad >= 65:
    print('Usted es de la tercera edad')
elif edad >= 30:
    print('Usted es un adulto')
elif edad >= 18:
    print('Usted es un joven adulto')
else:
    print('Usted es un niño')
