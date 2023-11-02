#Profundizando en los sistemas de numeracion
#Sistema decimal
a = 10
print(f'A decimal: {a}')
#Sistema binario
a = 0b1010
print(f'A binario: {a}')
#Sistema Octal
a = 0o12
print(f'A octario: {a}')
#hexadecimal
a = 0xA
print(f'A hexadecimal: {a}')
#Bases
#para esto utilizamos el constructor de int donde lo String '' es el numero q queremos ver (en su tipo)
#y el entero representa el tipo de sistema (ej: si la base es 10 es binario)

#base decimal
a = int('23', 10)
print(f'A = base decimal: {a}')

#base Binario
a = int('10111', 2)
print(f'A = base binario: {a}')

#base octal
a = int('27', 8)
print(f'A = base octal: {a}')

#Base hexadecimal
a = int('17', 16)
print(f'A = base hexadecimal: {a}')

#Base 5 (de 0 a 4)
a = int('43', 5)
print(f'A = base 5: {a}')


