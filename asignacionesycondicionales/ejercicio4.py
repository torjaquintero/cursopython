# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.4
# Programa que captura la base y la altura de un triangulo para hallar su área.
# El resultado de este cálculo lo muestra luego en pantalla
# ==============================================================================================

#guardamos la base y la altura del triángulo en variables
#con float() permitimos ingresar números con decimales
base = float(input("Digite la base del triángulo: "))
altura = float(input("Digite la altura del triángulo: "))

#calcula el area del triangulo y la imprime 
area = (base * altura) / 2
print('El área del triángulo es: ', area, 'cm^2')

#con round() para tener un número de maximo dos decimales
area = round(area, 2)
print('El área redondeada es: ', area, 'cm^2')
