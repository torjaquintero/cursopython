# Bienvenidos a Sys On Chip
# ==============================
# Ejercicio No.12
# Programa que simula un inicio de sesión en un sistema verificando el nombre de usuario y la contraseña
# ==============================================================================================

#Guarda datos de nombre de usuario y contraseña
usuarioGuardado = 'Alejandro'
claveUsuario = '123'

#captura por teclado el nombre de usuario
usuario = input('Cual es su nombre de usuario: ')

#verifica si el dato ingresado es igual al guardado
if usuario == usuarioGuardado:
    #si son iguales imprime un mensaje
    print('Usuario correcto')
    
    #pide la clave de usuario
    clave = input('Digite su clave: ')
    
    #verifica si clave ingresada es correcta
    if clave == claveUsuario:
        print('Sesión iniciada')
    else:
        print('Clave incorrecta')    

#si los nombres de usuario no coindiden imprime:
else:
    print('Usuario incorrecto')
