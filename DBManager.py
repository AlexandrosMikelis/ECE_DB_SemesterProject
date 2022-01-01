from types import TracebackType
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class DBManager:
    __DBPath = os.path.join(BASE_DIR,"LibNetwork.db")

    def __init__(self):
        self.connection = sqlite3.connect(DBManager.__DBPath)
        self.cursor = self.connection.cursor()
        
    def SELECT(self,table,data="*"):
        self.cursor = self.connection.execute(f"SELECT {data} FROM {table}")
        for row in self.cursor:
            print(row)
    
    def INSERT(self,table,fields,data):

        try:
            self.connection.execute(f"INSERT INTO {table} {fields} VALUES {data}")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(TracebackType.format_exception(exc_type, exc_value, exc_tb))

    def UPDATE(self,table,setter,condition):

        try:
            self.connection.execute(f"UPDATE {table} SET {setter} WHERE {condition}") 

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(TracebackType.format_exception(exc_type, exc_value, exc_tb))

    def DELETE(self,table,condition):
        
        try:
            self.connection.execute(f"DELETE FROM {table} WHERE {condition}")

        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(TracebackType.format_exception(exc_type, exc_value, exc_tb))

    def save(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
        
Manager = DBManager()
Manager.DELETE("Book","Book_ID = 5")
Manager.save()
Manager.close()
