from mysql_connector import Mysql
from rsa import Rsa
from user import User

class UserAdmin:
    def __init__(self):
        self.mysql = Mysql()
        self.rsa = Rsa()
        self.all_users = list()

    def receive_datas_to_add_new_user(self):
        try:
            while True:
                login = input('Your username: ')
                if not self.check_user_existing(login):
                    break
                print('This user already exist. Try again!')

            password = input('Your Password: ')
            text = input('Now, type the text to encrypt: ')
        except UnicodeError:
            print(UnicodeError)

        self.rsa.setup()
        self.encrypt_user_datas_and_insert_database(login, password, text)

    def encrypt_user_datas_and_insert_database(self, login, password, text):
        login_encrypted = ' '.join(map(str, self.rsa.encrypt(login)))
        password_encrypted = ' '.join(map(str, self.rsa.encrypt(password)))
        text_encrypted = ' '.join(map(str, self.rsa.encrypt(text)))

        self.mysql.insert_table(login_encrypted, password_encrypted, text_encrypted, self.rsa.public_key, self.rsa.private_key)
        self.all_users.append(User(login, password, text, self.rsa.public_key, self.rsa.private_key))
        print('Your message encrypted: ')
        print(text_encrypted, "\n\n")

    def decrypt_users(self):
        datas = self.mysql.select_table()
        list_decrypted = list()

        for users in datas:
            for i in range(1, 4):
                public, private = int(users[4]), int(users[5])
                my_list = list(users[i].split(" "))
                list_decrypted.append(self.rsa.decrypt(my_list, public, private))

            self.load_users_in_system(list_decrypted.copy(), public, private)
            list_decrypted.clear()

    def load_users_in_system(self, list_decrypted, public, private):
        username = list_decrypted[0]
        password = list_decrypted[1]
        text     = list_decrypted[2]
        public   = public
        private  = private
        self.all_users.append(User(username, password, text, public, private))

    def print_users(self):
        print('-   USERS   -')
        if len(self.all_users) == 0:
            print("\n - Haven't Users. - \n")
        for user in self.all_users:
            print('User: ', user.login)
            print('Text: ', user.text, '\n')

    def delete_user(self):
        login = input('Type the user login to delete: ')

        result = self.mysql.select_login()
        for logins in result:
            login_encrypted = list(logins[0].split(' '))
            decrypted = self.rsa.decrypt(login_encrypted, logins[1], logins[2])

            if decrypted == login:
                self.mysql.delete_user_table(' '.join(map(str, login_encrypted)))
                for i in self.all_users:
                    if i.login == login:
                        self.all_users.remove(i)
                        break
                return
        print('This user not existing!')

    def return_user_index(self, login):
        for i in range(0, len(self.all_users)):
            if self.all_users[i].login == login:
                return i
        return None

    def check_user_existing(self, login):
        for i in self.all_users:
            if i.login == login:
                return True
        return False

