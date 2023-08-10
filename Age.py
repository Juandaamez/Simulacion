__author__       = "Juan David Amezquita Nuñez"
__copyright__    = "Copyright 2023, USTA Tunja"
__credits__      = ["JF Mendoza"]
__license__      = "GPL"
__version__      = "1.0.0"
__maintainer__   = "Juan David Amezquita Nuñez"
__email__        = "juan.amezquita@usantoto.edu.co"
__status__       = "SUCCESSS"

import random


ages = []
T1 = 0
T2 = 0
T3 = 0
T4 = 0
T5 = 0
T6 = 0
T7 = 0

for i in range(100):
    number = random.randint(0, 100)
    ages.append(number)

for age in ages:

    if age < 10:
        T1 += 1

    elif age == 10:
        T2 += 1

    elif age < 20:
        T3 += 1

    elif age == 20:
        T4 += 1

    elif age < 60:
        T5 += 1

    elif age == 60:
        T6 += 1

    else:
        T7 += 1

print(f"People who will remain kids --------{T1}%")
print(f"Kids who will be teenagers ---------{T2}%")
print(f"People who will remain teenagers ---{T3}%")
print(f"Teenagers who will be adults -------{T4}%")
print(f"People who will remain adults ------{T5}%")
print(f"Adults who will be grandparents ----{T6}%")
print(f"Grandparent ------------------------{T7}%")