
######### Aqui es donde se debe correr el programa para poder jugar  ##########

from Partida import *
from Conexion import *

def insertar(nombre, puntaje):
	base_datos = BaseDatos()
	base_datos.insertar(nombre, puntaje)

def consultar():
	base_datos = BaseDatos()
	print()
	base_datos.consultar()
	print()

while(True):

	partida = Partida()

	print("\n¡Bienvenido al juego de preguntas y respuestas!")
	print("¿Que desea hacer?")
	print("1. Jugar")
	print("2. Ver el historial de partidas")
	print("3. Salir")

	accion = input("\nIngrese un numero: ")

	if accion == '1':
		partida = Partida()

		partida.configurar_juego()

		while(partida.get_vivo() and partida.get_nivel() < 5):

			partida.jugar()

			try:
				respuesta = int(input("\nDigite el número de la respuesta: "))
				partida.responder(respuesta)
			except ValueError:
				print("\n¡ENTRADA INCORRECTA!\nSe debe ingresar un número\n")
				respuesta = int(input("\nDigite el número de la respuesta: "))
				partida.responder(respuesta)	

			if partida.get_vivo() == True:
				continuar = input("Desea continuar (y/n): ")
				if continuar == 'n' or continuar == 'N':
					break

			
			partida.subir_nivel()

		nombre = input("Ingrese su nombre: ")
		partida.set_nombre(nombre)
		insertar(partida.get_nombre(), partida.get_puntaje())


	elif accion == '2':
		consultar()

	elif accion == '3':
		break
	else:
		print("\nDebe ingresar el número de la acción que desea realizar\n")

print("\n¡HASTA PRONTO!")