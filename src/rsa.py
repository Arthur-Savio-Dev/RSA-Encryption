from math_functions import MathFunctions

class Rsa:
    def __init__(self):
        self.mf = MathFunctions()
        self.public_key = None
        self.private_key = None
        self.e = None

    def setup(self):
        p = self.receive_prime_number()
        q = self.receive_prime_number()
        e = self.receive_prime_number()

        n = p * q
        d = self.mf.inverse_multiplicative(e, (p-1) * (q-1))

        self.public_key = n
        self.private_key = d
        self.e = e

        print('\nPublic | Private')
        print(self.public_key, ' | ', self.private_key)

    def receive_prime_number(self):
        while True:
            number = input('Type a prime number or press ENTER to generate random keys:  ')
            if number == '':
                return self.mf.generate_random_prime_number()
            elif number.isnumeric():
                if self.mf.is_prime(int(number)):
                    return int(number)
                else:
                    print('Please, just type prime numbers. Try again!')
            else:
                print('The input is invalid. Try again!')

    def encrypt(self, input):
        encrypted_message = list()
        list_num = [ord(char) for char in input]
        for i in list_num:
            value = pow(i, self.e)
            mod = value % self.public_key
            encrypted_message.append(mod)
        return encrypted_message

    def pre_decrypt(self):
        text = input('Message encrypted: ')
        text = list(text.split(' '))
        for i in text:
            if not i.isnumeric():
                return print('Invalid Input')

        public = int(input('Type your public key: '))
        private = int(input('Type your private key: '))
        result = self.decrypt(text, public, private)
        print('Your message: ', result, '\n')

    def decrypt(self, message_list, public, private):
        decrypted_message = ""
        for i in message_list:
            result = pow(int(i), private) % public
            decrypted_message += (chr(result))
        return decrypted_message
