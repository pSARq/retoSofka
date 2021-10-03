import mysql.connector

###########  La base de datos esta en linea. Es una base en phpMyAdmin  ###########

class BaseDatos:
	def __init__(self):
		self.db = mysql.connector.connect(host="sql10.freemysqlhosting.net", user="sql10441894", password="Zm3lkftGqK", database="sql10441894")
		self.cursor = self.db.cursor()

	def insertar(self, nombre, puntaje):
		sql = "Insert into HistorialJuego(Nombre, Puntaje) values(%s, %s)"
		partida = (nombre, puntaje)
		self.cursor.execute(sql, partida)
		self.db.commit()

	def consultar(self):
		sql = "select * from HistorialJuego"
		self.cursor.execute(sql)
		resultado = self.cursor.fetchall()

		print("[idPartida - Jugador - Puntaje]")
		for fila in resultado:
			print(fila)
			



# mydb = mysql.connector.connect(host="sql10.freemysqlhosting.net", user="sql10441894", password="Zm3lkftGqK", database="sql10441894" )
# mycursor = mydb.cursor()

# #Insertar
# sqlformula = "Insert into HistorialJuego(Nombre, Puntaje) values(%s, %s)"
# partida = ("Santiago", 30)

# mycursor.execute(sqlformula, partida)
# mydb.commit()



# mydb = mysql.connector.connect(host="sql10.freemysqlhosting.net", user="sql10441894", password="Zm3lkftGqK", database="sql10441894" )
# mycursor = mydb.cursor()

# #Consultar
# mycursor.execute("select * from HistorialJuego")
# myresult = mycursor.fetchall()

# for fila in myresult:
# 	print(fila)


# mydb = mysql.connector.connect(host="sql10.freemysqlhosting.net", user="sql10441894", password="Zm3lkftGqK", database="sql10441894" )
# mycursor = mydb.cursor()

# #Eliminar
# sql = "DELETE FROM HistorialJuego WHERE Nombre = 'Santiago'"
# mycursor.execute(sql)

# mydb.commit()



# prueba.insertar("santiago", 10)


