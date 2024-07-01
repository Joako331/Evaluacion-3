jugadores = []
IDs = []
Juego = []
Puntaje = []


print('''
    ***Sistema de registro de puntos jugadores de eShirlitos***
1.Registrar puntajes torneo
2.Listar todos los puntajes
3.Imprimir por Tipo
4.Salir del programa'''
)
opt=""
opt=int(input("Elija la opción que desea para continuar(1-4)\n -->: "))
if opt == 1:
    input("Ingrese nombre, apellido e ID del jugador: ").split()
    categoria=input("Ingrese su nivel de juego: ")

elif opt == 2:

elif opt == 3:

elif opt == 4:

else:
    print("La opción seleccionada no es válida, vuelva a intentar.")