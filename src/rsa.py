from math_functions import MathFunctions

class Rsa:
    def __init__(self):
        self.mf = MathFunctions()
        self.public_key = tuple()
        self.private_key = tuple()
        self.encrypted_message = list()
        self.decrypted_message = list()
        self.setup()

    def setup(self):
        p, q, e = list(self.mf.generate_random_prime_numbers())
        n = p * q
        d = self.mf.inverse_multiplicative(e, (p-1) * (q-1))

        self.private_key = p, q, d
        self.public_key = n, e

    def encrypt(self, message):
        list_num = [ord(char) for char in message]
        for i in list_num:
            value = pow(i, self.public_key[1])
            mod = value % self.public_key[0]
            self.encrypted_message.append(mod)

    def decrypt(self, message_list):
        d = self.private_key[2]
        n = self.public_key[0]
        for i in message_list:
            result = pow(i, d) % n
            self.decrypted_message.append(chr(result))

rsa = Rsa()
rsa.encrypt("minha casa e grande")
rsa.decrypt(rsa.encrypted_message)
print(rsa.decrypted_message)