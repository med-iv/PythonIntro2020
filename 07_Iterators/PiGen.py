from math import factorial
from decimal import Decimal, getcontext



def PiGen():
    getcontext().prec = 10000
    sum_vals = Decimal('0')
    k = 0
    mul_545140134 = 13591409
    deg_262537412640768000 = 1
    dec_426880 = Decimal(426880)
    dec_10005 = Decimal(10005).sqrt()
    while True:
        
        value = Decimal(factorial(6*k)) * mul_545140134 / (Decimal(factorial(3*k)*(factorial(k)**3))*deg_262537412640768000)
        sum_vals += value
        res = (dec_426880 * dec_10005) / sum_vals
        yield res
        k += 1
        mul_545140134 += 545140134
        deg_262537412640768000 *= -262537412640768000
        
#for i, p in enumerate(PiGen()):
    #if i>120:
        #break
#print(str(p)[1400:1470])