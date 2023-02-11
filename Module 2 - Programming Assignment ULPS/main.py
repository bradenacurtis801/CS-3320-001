import math
import sys


def findExp(num):
    exp = 0
    mant = num
    while True:
        if mant >= 2:
            mant /=2
            exp += 1
        elif mant < 1:
            mant *= 2
            exp -=1
        else:
            return [mant, exp]

def ulps(x,y):
    precision = sys.float_info.mant_dig
    eps = sys.float_info.epsilon
    inf = math.inf
    base = sys.float_info.radix
    
    if ((x < 0 and y > 0) or (x > 0 and y < 0)) or (x == 0 or y == 0) or (abs(x) == inf or abs(y) == inf):
        return inf
    else: 
        if abs(x) < abs(y): 
            smaller = abs(x)
            larger = abs(y)
        else:
            smaller = abs(y)
            larger = abs(x)
   
        smaller_mant, smaller_exp = findExp(smaller)
        larger_mant, larger_exp = findExp(larger)
        
        total_ulps = 0
        exp = smaller_exp
        while True:
            if exp < larger_exp:
                if exp == smaller_exp:
                    total_ulps = (base**(smaller_exp+1) - smaller)/(eps*base**(smaller_exp))
                else:
                    total_ulps += (base -1)*(base**(precision-1))
                exp += 1
            else:
                space = eps*base**(larger_exp)
                total_ulps += (larger-base**(larger_exp))/space
                break
        return total_ulps
         
def main():
    # print(ulps(20,30)) #1
    findExp(0)
    print(ulps(-1.0, -1.0000000000000003)) #1
    print(ulps(1.0, 1.0000000000000003)) #1
    print(ulps(1.0, 1.0000000000000004)) #2
    print(ulps(1.0, 1.0000000000000005)) #2
    print(ulps(1.0, 1.0000000000000006)) #3
    print(ulps(0.9999999999999999, 1.0)) #1
    print(ulps(0.4999999999999995, 2.0)) #9007199254741001
    print(ulps(0.5000000000000005, 2.0)) #9007199254740987
    print(ulps(0.5, 2.0)) #9007199254740992
    print(ulps(1.0, 2.0)) #4503599627370496
    print(2.0**52) # 4503599627370496.0
    print(ulps(-1.0, 1.0)) #inf
    print(ulps(-1.0, 0.0)) #inf
    print(ulps(0.0, 1.0)) #inf
    print(ulps(5.0, math.inf)) #inf
    print(ulps(15.0, 100.0)) # 12103423998558208

    


if __name__ == "__main__":
    main()