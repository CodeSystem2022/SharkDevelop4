
# dar formato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre, edad)

#Creamos una tupla
persona = ('Carla', 'Gomez', 5000.0)
mensaje_con_formato  = 'Hola %s %s. Tu sueldo es $%.2f' #% persona #aqui le pasamos el objeto q es tupla
#print(mensaje_con_formato % persona)

nombre = 'Juan'
edad = 19
sueldo = 1200
#mensaje_con_formato = 'Nombre: {}, Edad: {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)

#mensaje = 'Nombre: {0}, Edad: {1}, Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
#print(mensaje)

mensaje = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
#print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 33, 'sueldo': 3000.00}
mensaje = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)


