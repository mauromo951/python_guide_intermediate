#__str__ __repr__
#Métodos especiales, que sirven para definir comportamientos personalizados de objetos.

#__str__ → define cómo se muestra el objeto cuando lo imprimes con print().
#__repr__ → define cómo se representa el objeto para depuración o en la consola interactiva

import datetime

hoy = datetime.datetime.now()

print(str(hoy)) #Usuario final o comun formato, 
print(repr(hoy)) #Desarrollador formato

### Otro ejemplo

class Auto():
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def __str__(self):
        # Versión amigable para el usuario final
        return f"Auto : {self.marca} {self.año}"
    
    def __repr__(self):
        # Versión técnica (idealmente podría recrear el objeto)
        return f"Auto : {self.año} {self.marca}"
    
auto_uno = Auto("Prosche" , 2025) #Creacion del objeto

print(str(auto_uno))
print(repr(auto_uno))

class Servidor:
    def __init__(self, nombre, ip, estado):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def __repr__(self):
        return f"Servidor(nombre='{self.nombre}', ip='{self.ip}', estado='{self.estado}')"

s1 = Servidor("web01", "192.168.1.10", "activo")

print(s1)      # Si no hay __str__, esto usa __repr__
repr(s1)       # Siempre llama __repr__
s1             # En consola también llama __repr__


"""Adicional""" 
# __add__

class BankAccount:

    # Set the balance attribute to some initial deposit amount
    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    # Output the balance    
    def print_balance(self):
        print("Balance:", self.balance)

    # Defines how the addition operator (+) will behave for BankAccount 
    # objects, where if we have account1 + account2, this method will be 
    # called with "self" set to account1 and "other" set to account2.  We 
    # then have the method return a new BankAccount object with the combined
    # balance of both bank accounts (exactly what we have the __add__method 
    # do is up to us, but this is sensible behaviour).
    def __add__(self, other):
        total = self.balance + other.balance 
        return BankAccount(total)

# Create two bank account objects together
account1 = BankAccount(1000)
account2 = BankAccount(2000)
 
# After adding the two bank accounts we'll find the newly created and returned
# BankAccount object has the combined balance of both BankAccount objects.
new_account = account1 + account2   
new_account.print_balance()