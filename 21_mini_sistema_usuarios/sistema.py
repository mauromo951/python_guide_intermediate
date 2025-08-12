"""
Mini Sistema de Usuarios con las siguientes funciones:
Registrar usuario (nombre y contraseña).
Ver lista de usuarios (solo para admins).
Guardar datos en archivo .txt.
Validar que no se registren duplicados.
"""

import os

class Usuario:
    def __init__(self, nombre, contraseña, rol='user'):
        self.__nombre = nombre
        self.__contraseña = contraseña  # Solo 2 guiones bajos
        self.__rol = rol

    # Getters para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre
    
    def get_contraseña(self):
        return self.__contraseña
    
    def get_rol(self):
        return self.__rol

    def verificar_password(self, contraseña):
        return self.__contraseña == contraseña
        
    def __str__(self):
        return f"{self.__nombre} ({self.__rol})"
    

class SistemaUsuarios:
    def __init__(self, archivo='usuarios.txt'):
        self.archivo = archivo
        self.usuarios = []
        self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as file:
                for linea in file:
                    nombre, contraseña, rol = linea.strip().split(',')
                    self.usuarios.append(Usuario(nombre, contraseña, rol))

    def guardar_usuarios(self):
        with open(self.archivo, 'w', encoding='utf-8') as file:
            for u in self.usuarios:
                file.write(f"{u.get_nombre()},{u.get_contraseña()},{u.get_rol()}\n")

    def registrar_usuario(self, nombre, contraseña, rol="user"):
        if any(u.get_nombre() == nombre for u in self.usuarios):
            print("⚠️ Usuario ya existe.")
            return
        nuevo = Usuario(nombre, contraseña, rol)
        self.usuarios.append(nuevo)
        self.guardar_usuarios()
        print(f"✅ Usuario {nombre} registrado.")

    def listar_usuarios(self):
        for u in self.usuarios:
            print(u)


if __name__ == "__main__":
    sistema = SistemaUsuarios()
    while True:
        print("\n1. Registrar usuario")
        print("2. Listar usuarios")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            contraseña = input("Contraseña: ")
            rol = input("Rol (user/admin): ")
            sistema.registrar_usuario(nombre, contraseña, rol)

        elif opcion == "2":
            sistema.listar_usuarios()

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")


        