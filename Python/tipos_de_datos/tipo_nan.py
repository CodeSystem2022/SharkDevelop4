import math
from decimal import Decimal
#NaN (Not a Number)
a = float('nAN')
print(f'a: {a}')

#Modulo math
a = float('nan')
print(f'Es de tipo NaN (not a number)?: {math.isnan(a)}')

#modulo decimal
a = Decimal('nan')
print(f'Es de tipo NaN (not a number)?: {math.isnan(a)}')

