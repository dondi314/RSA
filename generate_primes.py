from numpy.random import randint as rand
from miller_rabin import miller_rabin


def generate_primes(bits=512, n_primes=1):
    r"""
    Generate any number of primes of specified
    bitlength.
    """
    primes = [0] * n_primes
    for i in range(n_primes):
        prime = 1
        for j in range(1, bits):
            prime += pow(2, j) * rand(0, 2)
        while not miller_rabin(prime):
            prime += 2
        primes[i] = prime
    return primes

