
from CrearPreguntas import *
import random

class Partida:
	def __init__(self):
		self._puntaje = 0
		self._preguntas_partida = []
		self._nombre = ""
		self._nivel = 0
		self._respuesta = 0
		self._vivo = True

	def get_puntaje(self):
		return self._puntaje

	def get_vivo(self):
		return self._vivo

	def get_nivel(self):
		return self._nivel

	def set_nombre(self, nombre):
		self._nombre = nombre

	def get_nombre(self):
		return self._nombre

	def aumentar_puntaje(self):
		self._puntaje += 10

	def mostrar_puntaje(self):
		print("TU PUNTAJE ES: ", self._puntaje, "\n")

	def configurar_juego(self):
		lista_preguntas = CrearPreguntas()
		lista = lista_preguntas.get_lista_preguntas()
		dificultad = 1
		primera_ves = True
		categoria = ""

		while len(self._preguntas_partida) < 5:
			numero = random.randint(0, 24)
			if primera_ves == True:
				if lista[numero].dificultad == dificultad:
					self._preguntas_partida.append(lista[numero])
					dificultad += 1
					categoria = lista[numero].categoria
					primera_ves = False
					print("\nLa categoria de las preguntas es: ", categoria)
			else:
				if lista[numero].dificultad == dificultad and lista[numero].categoria == categoria:
					self._preguntas_partida.append(lista[numero])
					dificultad += 1
					primera_ves = False

	def jugar(self):
		print(self._preguntas_partida[self._nivel].pregunta)
		print()
		print("1. " + self._preguntas_partida[self._nivel].opcion1)
		print("2. " + self._preguntas_partida[self._nivel].opcion2)
		print("3. " + self._preguntas_partida[self._nivel].opcion3)
		print("4. " + self._preguntas_partida[self._nivel].opcion4)
	
	def subir_nivel(self):
 		self._nivel += 1 

	def responder(self, respuesta):
 		self._respuesta = respuesta
 		if self._respuesta == self._preguntas_partida[self._nivel].respuesta:
 			print("\n¡CORRECTO!")
 			self.aumentar_puntaje()
 			self.mostrar_puntaje()
 		else:
 			print("\n¡INCORRECTO!")
 			self._vivo = False
 			self.mostrar_puntaje()
