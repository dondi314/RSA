def extended_gcd(a, b):
    r"""
    >>> a, b = 7, 5
    >>> s, t, r = extended_gcd(a, b)
    >>> print("%d * 5 + %d * 7 = %d" % (s, t, r))
    3 * 5 + -2 * 7 = 1
    """
    r, old_r = a, b
    s, old_s = 0, 1
    t, old_t = 1, 0
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s, old_t, old_r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
