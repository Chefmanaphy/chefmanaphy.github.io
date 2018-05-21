#author : DURAND Ulysse
#title : Pi calculus

from math import sqrt, factorial
from decimal import *

iter = 500

def main():
    getcontext().prec = 1000
    pi = 0
    for k in range(iter):
        c = 426880*Decimal(10005).sqrt()
        numerator = factorial(6*k)*(545140134*k+13591409)
        denominator = factorial(3*k)*(factorial(k))**3*(-262537412640768000)**k
        pi+=(Decimal(numerator)/Decimal(denominator))
    print(format(Decimal(c)/Decimal(pi),".1000f"))



if __name__=="__main__":
    main()
