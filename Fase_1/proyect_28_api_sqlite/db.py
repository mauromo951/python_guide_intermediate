# Conexión y funciones con SQLite

import sqlite3 as sql

def create_table():
    conn = sql.connect("pokemones.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            altura INTEGER,
            peso INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_pokemon(nombre, altura, peso):
    conn = sql.connect("pokemones.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (nombre, altura, peso) VALUES (?, ?, ?)",
                   (nombre, altura, peso))
    conn.commit()
    conn.close()

def get_all_pokemons():
    conn = sql.connect("pokemones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon")
    result = cursor.fetchall()
    conn.close()
    return result
