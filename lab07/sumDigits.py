"""
Lab 7, Warm-up Task 0

Fruitful recursion with numbers.
Sums the digits of a non-negative number
"""


def sumDigits(num):
    """Given a non-negative integer num, returnm the sum of the
    digits of num.
    >>> sumDigits(1)
    1
    >>> sumDigits(8)
    8
    >>> sumDigits(90)
    9
    >>> sumDigits(178)
    16
    >>> sumDigits(1234567890)
    45
    """
    # Write this code
    if num//10==0:             #base case condition which occurs when num is a single digit
        return num%10               
    else:
        return num%10 + sumDigits(num//10)  #recursive step 


# Standard code to run the doc tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()
