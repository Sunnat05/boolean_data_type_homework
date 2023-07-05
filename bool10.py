def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a>=0 and type((a)**(1/2))==type(1.0)
print(main(16))