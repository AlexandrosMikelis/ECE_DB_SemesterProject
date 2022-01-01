from types import TracebackType
import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class DBManager:
    """
    A class to represent a Manager of our DB.
    Basic CRUD operation executes here in a dynamic way.

    ...

    Attributes
    ----------
    path : str
        The full name of the DB file with .db at the end

    Methods
    -------
    SELECT(table,data="*",condition="")
        Execute SQL SELECT operation or R operation within given table.
        data represent which data we want to choose from table , default value -> all ("*")
        condition represent the condition to select the given data.

        Example:

            SELECT("Book","*",condition="Book_ID > 4")
            - This will print all fields of Books where Book ID is bigger than 4

    INSERT(table,fields,data)
        Execute SQL INSERT operation or C operation withing given table.
        fields represent the fields of table that we want to add data
        data represent the actual data we want to insert in the given fields

    UPDATE(table,setter,condition)
        Execute SQL UPDATE operation or U operation within given table.
        setter represent the updates(with data) that you want to change
        condition represent in which row we are going to update data

    DELETE(table,condition)
        Execute SQL DELETE operation or D operation within given table.
        condition represent which row or rows we are going to delete

    ErrorInfo(er)
        If an error occurs while CRUD operations this function will print all error info

    save()
        Will save the changes that we did in DB.

    close()
        Will close the connection that we have with DB.
    """

    __DBPath = ""

    def __init__(self,path):

        DBManager.__DBPath=os.path.join(BASE_DIR,path)
        self.connection = sqlite3.connect(DBManager.__DBPath)
        self.cursor = self.connection.cursor()
        
    def SELECT(self,table,data="*",condition=""):
        df = []
        sql = f"SELECT {data} FROM {table} WHERE {condition}" if condition else f"SELECT {data} FROM {table}" 

        self.cursor = self.connection.execute(sql)
        for row in self.cursor:
            df.append(row)
        
        return df
    
    def INSERT(self,table,fields,data):

        try:
            self.connection.execute(f"INSERT INTO {table} {fields} VALUES {data}")

        except sqlite3.Error as er:
            self.ErrorInfo(er)

    def UPDATE(self,table,setter,condition):

        try:
            self.connection.execute(f"UPDATE {table} SET {setter} WHERE {condition}") 

        except sqlite3.Error as er:
            self.ErrorInfo(er)

    def DELETE(self,table,condition):
        
        try:
            self.connection.execute(f"DELETE FROM {table} WHERE {condition}")

        except sqlite3.Error as er:
            self.ErrorInfo(er)

    def ErrorInfo(self,er):

        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(TracebackType.format_exception(exc_type, exc_value, exc_tb))

    def save(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

class Employee:
    Section = {"Name":"","ID":None}
    Library = {"Name":"","ID":None}

    def __init__(self,email,ssn,Manager):
        self._email = email
        self._ssn = int(ssn)
        self.Manager = Manager

        self.__Configure()

    def __Configure(self):
        E_data = self.Manager.SELECT("Employee","*",f"Email='{self._email}' and SSN = {self._ssn}")

        if(E_data):
            self.name = E_data[0]
            self.surname = E_data[1]

            Employee.Section["ID"] = E_data[-1]
            S_data = self.Manager.SELECT("Section","*",f"Section_ID = {E_data[-1]}")
            Employee.Section["Name"] = S_data[0]

            Employee.Library["ID"] = S_data[1]
            L_data = self.Manager.SELECT("Library","*",f"Library_ID = {S_data[1]}")
            Employee.Library["Name"] = L_data[2]

            print(f"Welcome {self.name} {self.surname} ")
        else:
            print("Please enter valid Employee credentials")
    
    def addBook(self):
        pass
    def addCustomer(self):
        pass
    def LendBook(self):
        pass

class DBAdmin(Employee):

    def __init__(self, email, ssn, Manager):
        super().__init__(email, ssn, Manager)

    def __Configure(self):
        return super().__Configure()  

    def addLibrary(self):
        pass

    def addSection(self):
        pass

    def addEmployee(self):
        pass
          
''' 
    RULES:

    BOOK:
        1) If a book is deleted then it must be deleted from Library link Book as well
        2) If a book is created it must have a category and section if they dont exist they must be created first
        3) If a book is created then a connection to a library must be created
    
    CATEGORY:
        1) If a category is created it must have a section otherwise create a section
        2) If a category is deleted then we must deleted all the containing books 
'''        
Manager = DBManager("LibNetwork.db")
Manager.SELECT("Book","Title","Book_ID=9")
Manager.save()
Manager.close()
