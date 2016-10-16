import math

def getNumberOfDigit(n, base = 10):
    if n > 0:
        return int(math.log(n, base)) + 1
    elif n == 0:
        return 1
    else:
        return int(math.log(-n, base)) + 1

## WARNING: works only with positive number and base = 10
def karatsuba(int1, int2, base = 10):
    if (int1 < base) or (int2 < base):
      return int1 * int2
    else:
      m = max(getNumberOfDigit(int1, base), getNumberOfDigit(int2, base))
      m2 = m/2
      
      high1 = int1 / 10**m2
      low1 = int1 % 10**m2
      high2 = int2 / 10**m2
      low2 = int2 % 10**m2
      z0 = karatsuba(low1, low2)
      z2 = karatsuba(high1, high2)
      z1 = karatsuba((low1 + high1), (low2 + high2))
      return (z2)*(10**(2*m2)) + ((z1-z2-z0)*(10**m2)) + (z0)
      
#%% Test case
      
int1 = 3141592653589793238462643383279502884197169399375105820974944592
int2 = 2718281828459045235360287471352662497757247093699959574966967627

     
a = karatsuba(int1, int2)
b = int1 * int2

##Comparing python built in method and mine
if a == b:
    print("It's working !")
else:
    print("It's not working...")
    
    