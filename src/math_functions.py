import math
import sympy

class MathFunctions:
    def is_prime(self, num):
        if sympy.isprime(num):
            return True
        return False

    def inverse_multiplicative(self, e, totiente):
        for i in range(0, totiente-1):
            if (i*e) % totiente == 1:
                return i

    def generate_random_prime_numbers(self):
            p = sympy.randprime(100, 1000)
            q = sympy.randprime(100, 1000)
            e = sympy.randprime(100, 1000)
            return p, q, e
