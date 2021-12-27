
from math import sqrt, pow

def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    
    x=pow(int(sqrt(a)),2)==a


    return x

x=main(81)
print(x)
