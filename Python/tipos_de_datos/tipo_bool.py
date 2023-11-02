
#Bool contiene los valores True y Flase
#Los tipos numericos, es false para el 0, true para los demas valores
valor = 0
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = -1
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

#Tipo string -> False '', True demas valores
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 'Abcde'
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tipo colecciones -> False para colecciones vacias
#Tipo colecciones -> True para todas las demas
# Lista
valor = []
resultado = bool(valor)
print(f'Valor de una lista: {valor}, Resultado: {resultado}')

valor = ['a', 'b']
resultado = bool(valor)
print(f'Valor de una lista con elementos: {valor}, Resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'Valor de una tupla: {valor}, Resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'Valor de una tupla con elementos: {valor}, Resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor de un diccionario: {valor}, Resultado: {resultado}')

valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'Valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

#Sentencias de cpntrol con bool
if bool(''):
    print('Regresa verdadero')
else:
    print('Regresa falso')

#Ciclos
variable = 3
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')
