# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.5
# Programa que calcula la nómina para un número de empleados solicitado por el usuario y los guarda en una lista
# ==============================================================================================

salarioMinimo = 930000
salud = 0.02
pension = 0.03
transporte = 0.1

nomina = []
empleado = []

totalEmpleados = int(input('Digite el número de empleados en la nómina: '))

for i in range(totalEmpleados):
    print('Nómina para el empleado No.', i+1)
    
    nombre = input('Digite el nombre del empleado: ')
    salarios = float(input('Digite el numero de salarios minimos que gana el empleado: '))
    
    sueldoBruto = (salarios * salarioMinimo)
    
    sueldoNeto = sueldoBruto - (sueldoBruto * salud) - (sueldoBruto * pension) + (sueldoBruto * transporte)
    
    print('El sueldo bruto que ganará el empleado No.', i+1, 'es: $', sueldoBruto)
    print('El sueldo neto que ganará el empleado No.', i+1, 'es: $', sueldoNeto)

                     
