import math
import sys
import struct
import numpy as np
sys.version

### NaN -> '0x7ff8'

def findExpMant(num):
    if hex(struct.unpack('Q', struct.pack('d', num))[0])[2:5] == '7ff':
        return [0,1024]
    elif hex(struct.unpack('Q', struct.pack('d', num))[0]) == '0x1':
        return [0,-1022]
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
            if exp == 2047 and mant != 0:
                return float('NaN')
            return [mant, exp]

def sign(x):
    """returns -1 if the x is negative, 0 if x is (either positive or negative) zero, 1 if x is positive. 
    """
    x_bin = struct.unpack('Q', struct.pack('d', x))
    if (bin(x_bin[0])[2] == 1 or bin(x_bin[0])[2] == 0) and (len(bin(x_bin[0])[3:]) == '00000000'):
        return 0
    elif x < 0:
        return -1
    elif x > 0:
        return 1
        
def fraction(x):
    """returns the IEEE fractional part of x as a decimal floating-point number. You must convert 
    binary to decimal. The fraction portion does not include the leading 1 that is not stored. """ 
    return (findExpMant(x)[0]-1)
    

def exponent(x):
    """returns the unbiased (true) binary exponent of x as a decimal integer. Remember that 
    subnormals are a special case. Consider 0 to be a subnormal. """
    return findExpMant(x)[1]
 

def mantissa(x): 
    """returns the full IEEE mantissa of x as a decimal floating-point number (which is the same as 
    fraction() + 1  for normalized numbers; same as fraction() for subnormals). """ 
    return findExpMant(x)[0]

def is_posinfinity(x):
    """returns true if x is positive infinity """
    x_bin = struct.unpack('Q', struct.pack('d', x))
    if hex(x_bin[0])[2:5] == '7ff':
        return True
    else: return False
 
def is_neginfinity(x):
    """returns true if x is negative infinity 
    """
    x_bin = struct.unpack('Q', struct.pack('d', x))
    if hex(x_bin[0])[2:5] == 'fff':
        return True
    else: return False
    
def ulp(x):
    """returns the magnitude of the spacing between x and its floating-point successor 
    """
    pass
def ulps(x, y) :
    """returns the number of intervals between x and y by taking advantage of the IEEE standard"""   
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
   
        smaller_mant, smaller_exp = findExpMant(smaller)
        larger_mant, larger_exp = findExpMant(larger)
        
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
    y = 6.5 
    subMin = np.nextafter(0,1) ##subMin = 5e-324 
    print(sign(y)) ##1 
    print(sign(0.0)) ## 0 
    print(sign(-y)) ## -1 
    print(sign(-0.0)) ##0 
    print(exponent(y)) ## 2 
    print(exponent(16.6)) ## 4 
    print(fraction(0.0)) ##0.0
    print(mantissa(6.5)) ##0.0 
    print(mantissa(0)) ##1.625 
    var1 = float('nan') 
    print(exponent(var1)) ## 1024 
    print(exponent(0.0)) ## 0 
    print(exponent(subMin)) ## -1022 
    print(is_posinfinity(math.inf)) ## True 
    print(is_neginfinity(math.inf)) ## False 
    print(not is_posinfinity(-math.inf)) ##True 
    print(is_neginfinity(-math.inf)) ##True 
    print(ulp(y)) ## 8.881784197001252e-16 
    print(ulp(1.0)) ## 2.220446049250313e-16 
    print(ulp(0.0)) ## 5e-324 
    print(ulp(subMin)) ## 5e-324 
    print(ulp(1.0e15)) ## 0.125 
    print(ulps(1,2)) ## 4503599627370496 

    


if __name__ == "__main__":
    main()