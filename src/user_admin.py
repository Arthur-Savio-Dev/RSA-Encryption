from mysql_connector import Mysql
from rsa import Rsa

class UserAdmin:
    def __init__(self):
        self.mysql = Mysql()

    def receive_datas_to_add_new_user(self):
        login = input('Type the name: ')
        password = input('Type the password: ')
        text = input('Now, type the text to encrypt ou decrypt: ')
        self.encrypt_user_datas(login, password, text)

    def encrypt_user_datas(self, login, password, text):
        rsa = Rsa()
        rsa.setup()
        login_encrypted = ' '.join(map(str, rsa.encrypt(login)))
        password_encrypted = ' '.join(map(str, rsa.encrypt(password)))
        text_encrypted = ' '.join(map(str, rsa.encrypt(text)))
        n = rsa.public_key[0]
        d = rsa.private_key[2]

        self.mysql.insert_table(login_encrypted, password_encrypted, text_encrypted, n, d)

    def change_user_text(self, login, text):
        if self.mysql.existing_user_in_table(login):
            self.mysql.update_text(login, text)
        else:
            print('This user not existing')
