
from math import sqrt, pow

def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    
    x=pow(int(sqrt(a)+0.5),2)==a


    return x

x=main(85)
print(x)
