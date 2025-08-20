import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import insert_pokemon, get_all_pokemons, create_table
def test_insert_and_get():
    create_table()
    insert_pokemon("testmon", 10, 100)
    data = get_all_pokemons()
    assert any(p[1] == "testmon" for p in data)
