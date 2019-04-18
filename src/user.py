class User:
    def __init__(self, login, password, text, public_key, private_key):
        self.login = login
        self.password = password
        self.text = text
        self.public_key = public_key
        self.private_key = private_key
