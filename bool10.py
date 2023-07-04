def main(a):
    ((a)**(1/2))%1==0 and a>=0
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return ((a)**(1/2))%1==0 and a>=0
print(main(16))