from rsa import Rsa
from user_admin import UserAdmin

class Menu:
    def __init__(self):
        self.rsa = Rsa()
        self.user_admin = UserAdmin()
        self.user_admin.decrypt_users()

    def print_main_menu(self):
        print('-- MAIN MENU --')
        print('1 - Generate keys')
        print('2 - Encrypt')
        print('3 - Decrypt')
        print('4 - Delete User')
        print('5 - Show Users')

    def main_menu(self):
        while True:
            try:
                self.print_main_menu()
                choice = int(input())
                if choice == 1:
                    self.rsa.setup()
                elif choice == 2:
                    self.user_admin.receive_datas_to_add_new_user()
                elif choice == 3:
                    self.rsa.pre_decrypt()
                elif choice == 4:
                    self.user_admin.delete_user()
                elif choice == 5:
                    self.user_admin.print_users()
                else:
                    continue
            except ValueError:
                print("Please, Just Type a integer number")