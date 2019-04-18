import mysql.connector


class Mysql:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            database='rsa',
            password=''
        )
        self.mycursor = self.mydb.cursor(buffered=True)

    def insert_table(self, login, password, text, n, d):
        try:
            query = 'INSERT INTO rsa_user_datas (login, password, text, public_key, private_key) values(%s, %s, %s, %s, %s)'
            self.mycursor.execute(query, (login, password, text, n, d))
            self.commit_table()
        except mysql.connector.Error as err:
            print('ERROR in insert table {}'.format(err))

    def select_table(self):
        try:
            self.mycursor.execute('SELECT * FROM rsa_user_datas')
            return list(self.mycursor.fetchall())
        except mysql.connector.Error as err:
            print('ERROR in select table {}'.format(err))

    def select_login(self):
        try:
            query = 'SELECT login, public_key, private_key FROM rsa_user_datas'
            self.mycursor.execute(query)
            return self.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('ERROR in select user {}'.format(err))

    def delete_user_table(self, login):
        try:
            query = 'DELETE FROM rsa_user_datas WHERE login = "' + login + '"'
            self.mycursor.execute(query)
            self.commit_table()
        except mysql.connector.Error as err:
            print('ERROR in delete user {}'.format(err))

    def commit_table(self):
        try:
            self.mydb.commit()
        except mysql.connector.Error as err:
            print('ERROR in commit {}'.format(err))

    def close_database_connection(self):
        self.mydb.close()

