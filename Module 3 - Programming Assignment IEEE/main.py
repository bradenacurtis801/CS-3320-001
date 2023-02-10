import math
import sys
import struct

#sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
sys.float_info
### NaN -> '0x7ff8'

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
        

def exponent(x):
    """returns the unbiased (true) binary exponent of x as a decimal integer. Remember that 
    subnormals are a special case. Consider 0 to be a subnormal. """
    exp = 0
    mant = x
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
            exp = struct.unpack('Q', struct.pack('d', x))
            return [mant, exp]
 
def fraction(x):
    """returns the IEEE fractional part of x as a decimal floating-point number. You must convert 
    binary to decimal. The fraction portion does not include the leading 1 that is not stored. 
""" 
pass

def mantissa(x): 
    """returns the full IEEE mantissa of x as a decimal floating-point number (which is the same as 
    fraction() + 1  for normalized numbers; same as fraction() for subnormals). 
""" 
pass

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
    """returns the number of intervals between x and y by taking advantage of the IEEE standard
"""   
pass
      
def main():
    # y = 6.5 
    # subMin = np.nextafter(0,1) //subMin = 5e-324 
    # print(sign(y)) //1 
    # print(sign(0.0)) // 0 
    # print(sign(-y)) // -1 
    # print(sign(-0.0)) //0 
    # print(exponent(y)) // 2 
    # print(exponent(16.6)) // 4 
    # print(fraction(0.0)) //0.0 
    # print(mantissa(y)) //1.625 
    # print(mantissa(0.0) //0.0 
    # var1 = float(‘nan’) 
    # print(exponent(var1)) // 1024 
    # print(exponent(0.0) // 0 
    # print(exponent(subMin)) // -1022 
    # print(is_posinfinity(math.inf)) // True 
    # print(is_neginfinity(math.inf)) // False 
    # print(not is_posinfinity(-math.inf)) //True 
    # print(is_neginfinity(-math.inf)) //True 
    # print(ulp(y)) // 8.881784197001252e-16 
    # print(ulp(1.0)) // 2.220446049250313e-16 
    # print(ulp(0.0)) // 5e-324 
    # print(ulp(subMin)) // 5e-324 
    # print(ulp(1.0e15)) // 0.125 
    # print(ulps(1,2)) // 4503599627370496 

    


if __name__ == "__main__":
    main()