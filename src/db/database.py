import sqlite3
from sqlite3 import Error


class Data:
    def __init__(self):
        self.db = './data.db'
        self.conn = None
        self.create_connection()
        self.cursor.execute(
            '''Create table if not exists downloads_test(
            primary_key integer primary key,
            source text,
            date text);''')

    def create_connection(self):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except Error as e:
            print(e)

    def insert(self, link):
        self.cursor.execute(
            '''Insert into downloads_test(source, date)
            Values(?, datetime('now', 'localtime'));''',
            (link,))
        self.conn.commit()

    def select(self):
        self.cursor.execute('Select * from downloads_test;')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    data = Data()
    data.create_connection()
