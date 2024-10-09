import mysql.connector

def conectar_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="placass"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None