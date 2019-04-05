import math

class MathFunctions:
    def mdc(self, n1, n2):
        if n1 % n2 == 0:
            return n2
        self.mdc(n1, n1 % n2)

    def is_co_prime(self, n1, n2):
        flag = self.mdc(n1, n2)
        if flag:
            return True
        return False

    def is_prime(self, num):
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def inverse_multiplicative(self, e, totiente):
        for i in range(0, totiente-1):
            if (i*e) % totiente == 1:
                return i

