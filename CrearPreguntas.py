
from Preguntas import *

class CrearPreguntas:
	def __init__(self):
		self.lista_preguntas = []
		self.pregunta1 = Pregunta('¿Cuál es el simbolo periódico del Hidrogeno?' , 3, 'Hb', 'Hg', 'H', 'He', 1, 'Ciencia')
		self.lista_preguntas.append(self.pregunta1);

		self.pregunta2 = Pregunta('¿Cómo se llama a la caída excesiva de cabello?', 2, 'Pelon', 'Alopecia', 'Calvicie', 'Calvito', 2, 'Ciencia')
		self.lista_preguntas.append(self.pregunta2);

		self.pregunta3 = Pregunta('¿Cómo se llama el vapor que el ser humano lanza al exhalar?', 1, 'Dioxido de carbono', 'Oxigeno', 'Carbono', 'Helio', 3, 'Ciencia')
		self.lista_preguntas.append(self.pregunta3);

		self.pregunta4 = Pregunta('¿Qué osos viven en el artico?', 1, 'Polares', 'De anteojos', 'Grisli', 'Hormiguero', 4, 'Ciencia')
		self.lista_preguntas.append(self.pregunta4);

		self.pregunta5 = Pregunta('¿Cuál fue el primer metal que emplearon los seres humanos?', 3, 'Bronce', 'Acero', 'Cobre', 'Aluminio', 5, 'Ciencia')
		self.lista_preguntas.append(self.pregunta5);

		self.pregunta6 = Pregunta('¿Cuándo terminó la II Guerra Mundial?', 1, '1945', '1947', '1943', '1938', 1, 'Historia')
		self.lista_preguntas.append(self.pregunta6);

		self.pregunta7 = Pregunta('¿En qué año llegó Cristobal Colón a América?', 2, '1429', '1492', '1592', '1545', 2, 'Historia')
		self.lista_preguntas.append(self.pregunta7);

		self.pregunta8 = Pregunta('¿Cuál es el libro sagrado de los musulmanes?', 4, 'La Voragine', 'La Biblia', 'El Talmud', 'El Corán', 3, 'Historia')
		self.lista_preguntas.append(self.pregunta8);

		self.pregunta9 = Pregunta('¿Quién era el general de los Nazis en la Segunda Guerra Mundial?', 2, 'Heinrich Himmler', 'Adolf Hitler', 'Benito Mussolini', 'Abraham Lincoln', 4, 'Historia')
		self.lista_preguntas.append(self.pregunta9);

		self.pregunta10 = Pregunta('¿Quién es el padre del psicoanálisis?', 4, 'Homero', 'Skinner', 'Carl Gustav Jung', 'Sigmund Freud', 5, 'Historia')
		self.lista_preguntas.append(self.pregunta10);

		self.pregunta11 = Pregunta('¿Cuál es el nombre del río más largo del mundo?', 2, 'Río Nilo', 'Río Amazonas', 'Río Danubio', 'Río Misisipi', 1, 'Geografía')
		self.lista_preguntas.append(self.pregunta11);

		self.pregunta12 = Pregunta('¿Cuál es el océano más grande del mundo?', 3, 'Océano Atlántico', 'Océano Índico', 'Océano Pacífico', 'Ocáno Ártico', 2, 'Geografía')
		self.lista_preguntas.append(self.pregunta12);

		self.pregunta13 = Pregunta('¿Cuál es el país más grande del mundo?', 2, 'China', 'Rusia', 'India', 'Colombia', 3, 'Geografía')
		self.lista_preguntas.append(self.pregunta13);

		self.pregunta14 = Pregunta('¿Cuál es el país que tiene forma de bota?', 3, 'España', 'Honduras', 'Italia', 'Venezuela', 4, 'Geografía')
		self.lista_preguntas.append(self.pregunta14);

		self.pregunta15 = Pregunta('¿Cuál es la ciudad de los rascacielos?', 2, 'Tokio', 'New York', 'Hong Kong', 'Perú', 5, 'Geografía')
		self.lista_preguntas.append(self.pregunta15);

		self.pregunta16 = Pregunta('¿Quién escribió La Odisea?', 1, 'Homero', 'Virgilio', 'Cervantes', 'Platón', 1, 'Arte')
		self.lista_preguntas.append(self.pregunta16);

		self.pregunta17 = Pregunta('¿Cuál es la obra más importante de la literatura en español?', 2, 'El Principito', 'Don Quijote de la Mancha', 'Cien años de soledad', 'María', 2, 'Arte')
		self.lista_preguntas.append(self.pregunta17);

		self.pregunta18 = Pregunta('¿Quién pintó el famoso cuadro La última cena?', 3, 'Rembrandt', 'Velazquez', 'Leonardo da Vinci', 'Salvador Dalí', 3, 'Arte')
		self.lista_preguntas.append(self.pregunta18);

		self.pregunta19 = Pregunta('¿Cómo se llama el Himno Nacional de Francia?', 2, 'La Internacional', 'La Marsellesa', 'La solitaria', 'Deutschlandlied', 4, 'Arte')
		self.lista_preguntas.append(self.pregunta19);

		self.pregunta20 = Pregunta('¿A qué se denomina séptimo arte?', 3, 'Pintura', 'Escultura', 'Cine', 'Opera', 5, 'Arte')
		self.lista_preguntas.append(self.pregunta20);

		self.pregunta21 = Pregunta('¿Cuál es el deporte nacional de Canadá?', 3, 'Bolos', 'Baloncesto', 'Lacrosse', 'Fútbol', 1, 'Historia')
		self.lista_preguntas.append(self.pregunta21);

		self.pregunta22 = Pregunta('¿En qué país se celebraron los primeros Juegos Olímpicos?', 3, 'Italia', 'Japón', 'Grecia', 'Francia', 2, 'Historia')
		self.lista_preguntas.append(self.pregunta22);

		self.pregunta23 = Pregunta('¿Cuántos minutos dura un partido de rugby?', 1, '80 minutos', '30 minutos', '120 minutos', '60 minutos', 3, 'Historia')
		self.lista_preguntas.append(self.pregunta23);

		self.pregunta24 = Pregunta('¿Cuántos jugadores hay en un equipo de béisbol?', 2, '8 jugadores', '9 jugadores', '10 jugadores', '11 jugadores', 4, 'Historia')
		self.lista_preguntas.append(self.pregunta24);

		self.pregunta25 = Pregunta('¿Cuál es el único país que ha jugado en todos los mundiales de fútbol?', 1, 'Brasil', 'Inglaterra', 'España', 'Argentina', 5, 'Historia')
		self.lista_preguntas.append(self.pregunta25);

	def agregar(self, pregunta):
		self.lista_preguntas.append(pregunta)

	def get_lista_preguntas(self):
		return self.lista_preguntas






