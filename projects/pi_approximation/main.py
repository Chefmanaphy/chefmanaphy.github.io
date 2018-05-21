#author :
#title :
import math, random
from decimal import *

def main():
    getcontext().prec = 50
    r = 1
    pi = 0
    all = 0
    okay = 0
    registered_diff = Decimal(1)
    while True:
        for i in range(10000):
            x = Decimal(random.random())
            y = Decimal(random.random())
            all+=1
            if (x**Decimal(2)+y**Decimal(2)<1):
                okay+=1

        pi = Decimal(4)*(Decimal(okay)/Decimal(all))
            # diff = Decimal(math.pi)-pi
            # if(abs(diff)<registered_diff):
                # registered_diff = abs(diff)
                # print("")
        print(pi)



if __name__=="__main__":
    main()
