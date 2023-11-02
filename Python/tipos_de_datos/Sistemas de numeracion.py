#Sistemas de numeracion
import math
from decimal import Decimal

#Sistema decimal
a=10
print(f"a decimal: {a}")

#binario
a=0b1010
print(f"a binario: {a}")

#octal
a=0o12
print(f"a octal: {a}")

#hexadecimal
a=0xA
print(f"a hexadecimal: {a}")

#Base decimal
a= int('23', 10)
print(f"a base decimal: {a}")

#Base binario
a=int('1010',2)
print(f"a base binaria: {a}")

#base octal
a=int('12',8)
print(f"a base octal: {a}")

#base hexadecimal
a=int('A',16)
print(f"a base hexadecimal: {a}")

#base 5
a=int('344',5)
print(f"a base 5: {a}")

#Tipo Float
#profundizando en el tipo float

b=3.0
print(f'b={b:.2f}')

#Constructor tipo float - recibe int y str
b = float(10)
print(f'b={b:.2f}')

b = float('10')
print(f'b={b:.2f}')

#Notacion exponencial
b = 3e5
print(f'b={b:.2f}')

#Valores Infinitos
infinito_positivo = float('inf') #o '-inf'
print(infinito_positivo)
print(math.isinf(infinito_positivo))
infinito_positivo = math.inf #o -math.inf
print(infinito_positivo)

# Modulo Decimal
infinito_positivo = Decimal('Infinity') #o '-Infinity'
print(infinito_positivo)
print(math.isinf(infinito_positivo))