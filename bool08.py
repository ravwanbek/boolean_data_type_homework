def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    x=a>=0 and a%1==0
    
    return x

x=main(2)
print(x)