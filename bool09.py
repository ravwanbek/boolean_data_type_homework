def main(a):
    """Check the natural number.Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=a>0 and a%1==0   
    
    return x
    
x=main(5)
print(x)