from math_functions import MathFunctions


class Rsa:
    def __init__(self):
        self.mf = MathFunctions()
        self.public_key = tuple()
        self.private_key = tuple()
        self.setup()

    def setup(self):
        p, q, e = list(self.mf.generate_random_prime_numbers())
        n = p * q
        d = self.mf.inverse_multiplicative(e, (p-1) * (q-1))

        self.private_key = p, q, d
        self.public_key = n, e

    def receive_setup(self):
        p = self.receive_prime_number()
        q = self.receive_prime_number()
        e = self.receive_prime_number()

        n = p * q
        d = self.mf.inverse_multiplicative(e, (p-1) * (q-1))
        self.private_key = p, q, d
        self.public_key = n, e

    def receive_prime_number(self):
        while True:
            try:
                number = int(input('Type a prime number P'))
                if self.mf.is_prime(number):
                    return number
            except ValueError:
                print('Please, type just integer numbers')

    def encrypt(self, input):
        encrypted_message = list()
        list_num = [ord(char) for char in input]
        for i in list_num:
            value = pow(i, self.public_key[1])
            mod = value % self.public_key[0]
            encrypted_message.append(mod)
        return encrypted_message

    def decrypt(self, message_list):
        decrypted_message = list()

        d = self.private_key[2]
        n = self.public_key[0]
        for i in message_list:
            result = pow(i, d) % n
            decrypted_message.append(chr(result))

