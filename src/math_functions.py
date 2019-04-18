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

    def generate_random_prime_number(self):
            return sympy.randprime(10, 100)
