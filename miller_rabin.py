from random import randint as rand


def miller_rabin(n, k=40):
    r"""
    Miller-Rabin Primality Test
    
    Tests
    -----
    >>> miller_rabin(13)
    True
    >>> miller_rabin(2)
    True
    >>> miller_rabin(121)
    False
    >>> miller_rabin(1000004233)
    True
    >>> miller_rabin(1000004237)
    False
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1
    for _ in range(k):
        a = pow(rand(1, n), d, n)
        if a not in [1, n - 1]:
            witness = True
            for _ in range(1, s):
                a = pow(a, 2, n)
                if a == n - 1:
                    witness = False
            if witness == True:
                return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
