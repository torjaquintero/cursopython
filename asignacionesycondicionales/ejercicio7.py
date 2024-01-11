# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.7
# Programa que suma un bono de 15% al sueldo de un trabajador, 
# siempre y cuando gane menos de 2 salarios mínimos
# ==============================================================================================

#Captura por el teclado los datos del trabajador
nombre = input('Digite el nombre del trabajador: ')

#se declaran la variable salario mínimo
salarioMinimo = 930000
#se captura por teclado el sueldo
sueldo = float(input('Digite el sueldo del trabajador: '))

"""utilizamos if como condicional. En caso de que se cumpla
    la condición de que el sueldo sea menor a dos salarios, 
    se tiene derecho a la bonificación"""

if sueldo < (2 * salarioMinimo):
    print('Tiene derecho a una bonificación!')
    #calcula de nuevo el sueldo sumando la bonificación
    sueldo = sueldo + (sueldo * 0.15)

#imprime en pantalla la variable sueldo
print('Su sueldo neto es: $', sueldo)
