#25_SQLITE3
#26_consultas(SELECT, UPDATE, DELETE...)
#modificar consultas por uso de parametros 
#para evitar sqlinjection
import sqlite3 as sql

def createDB():
    conn = sql.connect("streammers.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE jugadores (
        name text,
        equipo text,
        numero integer,
        goles integer)"""
    )
    conn.commit()
    conn.close()


def insertRow(nombre, equipo, numero, goles): #INSERT
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO jugadores VALUES('{nombre}', '{equipo}', {numero}, {goles})"
    cursor.execute(
        instruccion
    )
    conn.commit()
    conn.close()

def read_row(): #SELECT
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM jugadores"
    cursor.execute(
        instruccion
    )
    datos = cursor.fetchall() #devuelve valores en una lista
    conn.commit()
    conn.close()
    print(datos)

def insert_rows(jugadoreslista): #Insertar mas de una fila de datos
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO jugadores VALUES (?,?,?,?) "
    # el ? es un placeholder o marcador
    cursor.executemany( #para hacer varios inserts
        instruccion, jugadoreslista
    )
    conn.commit()
    conn.close()
    
def read_ordered(goles): #SELECT 
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    #Menos goles a mas goles
    #instruccion = f"SELECT * FROM jugadores ORDER BY {goles}"

    #Mas goles a menos goles, usando DESC
    instruccion = f"SELECT * FROM jugadores ORDER BY {goles} DESC"
    cursor.execute(
        instruccion
    )
    datos = cursor.fetchall() #devuelve valores en una lista
    conn.commit()
    conn.close()
    print(datos)

def search(): #WHERE, busqueda particular por  valor o condicion
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    ###Busqueda exacta
    #instruccion = f"SELECT * FROM jugadores WHERE name='Messi'"

    ###Busqueda sin respetar mayus y minus.
    #instruccion = f"SELECT * FROM jugadores WHERE name like 'messi'"

    ###Busqueda con comodin para buscar iniciales 
    ### o que empiece con cierta inicializacion
    instruccion = f"SELECT * FROM jugadores WHERE name like 'Cris%'"


    cursor.execute(
        instruccion
    )
    datos = cursor.fetchall() #devuelve valores en una lista
    conn.commit()
    conn.close()
    print(datos)

def update_fields(): #UPDATE
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE jugadores SET goles=10000 WHERE name='Rooney'"
    cursor.execute(
        instruccion
    )
    
    conn.commit()
    conn.close()

def delete_row(): #DELETE
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM jugadores WHERE ROWID = 2"
    cursor.execute(
        instruccion
    )
    
    conn.commit()
    conn.close()

def asignar_id(): #ASIGNAR ROWID id oculto
    conn = sql.connect("streammers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT ROWID, * FROM jugadores;"
    cursor.execute(
        instruccion
    )
    
    conn.commit()
    conn.close()
    




if __name__ == '__main__':
    #createDB()
    #createTable()
    #insertRow("Messi","Barcelona", 10, 100)
    #insertRow("Cristiano","Real Madrir", 7, 200)
    #read_row()
    """DEFINIR LISTA"""
    jugadores =[
        ("Xavi", "Barcelona", 8, 90),
        ("Modric", "Real Madrid", 10, 60),
        ("Rooney", "Man U", 9, 500)
    ]
    #insert_rows(jugadores)
    #read_row()
    #read_ordered('goles')
    #search()
    #update_fields()
    #asignar_id()
    delete_row()

