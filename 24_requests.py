#Request

#Instalar librería requests
#pip install requests

import requests

url = requests.get('https://pythonbasics.org/')
print(url) #Response
#print(dir(url))
#print(url.text) #html de la página, source del website


imagen_url= requests.get('https://pythonbasics.org/wp-content/uploads/2017/10/python.png')
"""
print(imagen_url.content) #Imagen en bytes


with open('imagen_python.png', 'wb') as picture: #Guardar imagen en bytes a png
    picture.write(imagen_url.content)
"""
print(imagen_url.status_code, imagen_url.ok)
print(imagen_url.headers.values())

#https://httpbin.org/

""" #GET
payload = {'page': 2, 'count': 25}
r= requests.get('https://httpbin.org/get', params=payload)
"""

"""POST"""
payload = {'usarname': "test", 'password': "test123"}
r= requests.post('https://httpbin.org/post', data=payload)
print(r.url)
print(r.text)
print(r.json())

r_dict =r.json()
print(r_dict['form'],r_dict['origin'])

#Ejemplo


ejemplo = requests.get('https://httpbin.org/basic-auth/Mauro/admin123', auth=("Mauro", "admin123"))
print(ejemplo.text)