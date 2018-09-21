from extended_gcd import extended_gcd
from generate_primes import generate_primes


def rsa(bits=512, e=pow(2, 16)+1):
    r"""
    >>> e, d, n = rsa()
    >>> message = 109
    >>> encrypted_message = encrypt(e, n, message)
    >>> decrypted_message = decrypt(d, n, encrypted_message)
    >>> message == decrypted_message
    True
    """
    gcd = None
    while gcd != 1:
        p, q = generate_primes(bits=bits, n_primes=2)
        n = p * q
        phi = (p - 1) * (q - 1)
        d, k, gcd = extended_gcd(phi, e)
        while d < 0 and gcd == 1:
            d += phi
    return e % n, d % n, n


def encrypt(e, n, message):
    return pow(message, e, n)


def decrypt(d, n, encrypted_message):
    return pow(encrypted_message, d, n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

