from api import get_pokemon
from db import create_table, insert_pokemon, get_all_pokemons

def main():
    create_table()
    nombre = input("Escribe el nombre de un Pokémon: ")
    data = get_pokemon(nombre)

    if data:
        insert_pokemon(data["name"], data["height"], data["weight"])
        print(f"{data['name']} guardado en la base de datos.")
    else:
        print("Pokémon no encontrado.")

    print("Pokémones guardados:")
    for p in get_all_pokemons():
        print(p)

if __name__ == "__main__":
    main()
