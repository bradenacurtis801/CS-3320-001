import math
import sys

def sign(x):
    """returns -1 if the x is negative, 0 if x is (either positive or negative) zero, 1 if x is positive. 
    """
    pass

def exponent(x):
    """returns the unbiased (true) binary exponent of x as a decimal integer. Remember that 
    subnormals are a special case. Consider 0 to be a subnormal. """
    pass
 
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
    pass
 
def is_neginfinity(x):
    """returns true if x is negative infinity 
    """
    pass
    
def ulp(x):
    """returns the magnitude of the spacing between x and its floating-point successor 
    """
    pass
def ulps(x, y) :
    """returns the number of intervals between x and y by taking advantage of the IEEE standard
"""   
pass
      
def main():
    # print(ulps(20,30)) #1
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