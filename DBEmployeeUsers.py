from distutils.log import error
from DBManager import DBManager
import datetime 

def ClearData(data):
    clearedData = []
    for d in data:
        clearedData.append(d[0])
    return tuple(clearedData)

class Employee:
    Section = {"Name":"","ID":None}
    Library = {"Name":"","ID":None} 

    def __init__(self,email,ssn,Manager):
        self._email = email
        self._ssn = int(ssn)
        self.Manager = Manager

        self.__Configure()

    def __Configure(self):
        E_data = self.Manager.SELECT("Employee","*",f"Email='{self._email}' and Employee_ID = {self._ssn}")
        if(E_data):
            self.name = E_data[0][1]
            self.surname = E_data[0][2]
            self.Work_Hours = E_data[0][6]

            Employee.Section["ID"] = E_data[0][-2]
            S_data = self.Manager.SELECT("Section","*",f"Section_ID = {E_data[0][-2]}")
            Employee.Section["Name"] = S_data[0][3]

            Employee.Library["ID"] = S_data[0][1]
            L_data = self.Manager.SELECT("Library","*",f"Library_ID = {S_data[0][1]}")
            Employee.Library["Name"] = L_data[0][2]

        else:
            print("Please enter valid Employee credentials")

    def Info(self):
        InfoTable = [] + f"{self.name},{self.surname},{self._email},{self._ssn}".split(",")
        InfoTable.append(Employee.Section)
        InfoTable.append(Employee.Library)
        InfoTable.append(f'{self.Work_Hours}')
        return InfoTable

    def addBook(self,Title,ISBN,Author,Publisher,Availability,Condition,Category_ID):
        self.Manager.INSERT("Book","(Title,ISBN,Author,Publisher,Availability,Condition,Category_ID)",f"('{Title}',{int(ISBN)},'{Author}','{Publisher}',{bool(Availability)},'{Condition}',{int(Category_ID)})")
        self.Manager.save()
    
    def showBook(self,filter,fields,values):
        val = f"and {values}" if values else ""
        if filter == 0:
            showcase = self.Manager.SELECT("Book,Library_Contains_Books",','.join(fields),f"Book.Book_ID = Library_Contains_Books.Book_ID and Library_Contains_Books.Library_ID = {Employee.Library['ID']} {val}")
        elif filter == 1:
            showcase = self.Manager.SELECT("Book,Category",','.join(fields),f"Category.Category_ID = Book.Category_ID and Section_ID = {Employee.Section['ID']} {val}")
        return showcase

    def deleteBook(self,Condition):
        self.Manager.DELETE("Book",Condition)
        self.Manager.save()
    
    def updateBook(self,Setter,Condition):
        self.Manager.UPDATE("Book",Setter,Condition)
        self.Manager.save()
    
    def showCustomer(self):
        pass
    
    def addCustomer(self):
        pass
    
    def updateCustomer(self):
        pass

    def deleteCustomer(self):
        pass

    def LendBook(self,Customer_Email,Book_Title):
        Book_ID = None
        Customer_ID = None

        Book_ID = ClearData(self.Manager.SELECT("Book","Book_ID",f"Book.Title = '{Book_Title}' and Book_ID IN (SELECT Library_Contains_Books.Book_ID FROM Library_Contains_Books WHERE Library_ID = {int(Employee.Library['ID'])})"))[0] 
        Customer_ID = ClearData(self.Manager.SELECT("Customer","Customer_ID",f"Email = '{Customer_Email}'"))[0]
        MaxBooks = ClearData(self.Manager.SELECT("Customer_Membership","Max_Books",f"Customer_ID = {int(Customer_ID)}"))[0]

        Start_Date = datetime.datetime.today().strftime('%Y-%m-%d')
        End_Date = datetime.datetime.strptime(Start_Date,'%Y-%m-%d') + datetime.timedelta(days=30)
        End_Date = End_Date.strftime('%Y-%m-%d')

        if MaxBooks > ClearData(self.Manager.SELECT("Borrowing_Contains_Books","COUNT(Customer_Borrowing_ID)",f"Customer_Borrowing_ID={int(Customer_ID)}"))[0]:
            if Book_ID==None or Customer_ID==None:
                return Book_ID,Customer_ID

            if self.Manager.SELECT("Borrowing","Borrow_Customer_ID,Start_Date,End_Date",f"Borrow_Customer_ID = {int(Customer_ID)} and Start_Date = '{Start_Date}' and End_Date = '{End_Date}'"):
                pass
            else:
                self.Manager.INSERT("Borrowing","(Borrow_Customer_ID,Start_Date,End_Date)",f"({int(Customer_ID)},'{Start_Date}','{End_Date}')")

            self.Manager.INSERT("Borrowing_Contains_Books",'(Book_ID,Customer_Borrowing_ID)',f"({int(Book_ID)},{int(Customer_ID)})")
            self.Manager.UPDATE("Book","Availability=false",f"Book_ID={int(Book_ID)}")
            self.Manager.save()

            return "Successful Lend"
        else:
            return "Sorry but the User cant Lend more Books from our library"

    def InterLibLoan(self,isbn,quantity):
        Book_ID = ClearData(self.Manager.SELECT("Book","Book_ID",f"ISBN = {isbn}"))[0]
        Library_Getter_ID = Employee.Library["ID"]
        Library_Sender_ID = ClearData(self.Manager.SELECT("Library_Contains_Books","Library_ID",f"Book_ID = {int(Book_ID)}"))[0]
        
        self.Manager.INSERT("Inter_Library_Loaning","(Library_Sender,Library_Getter,Book_ID,Quantity)",f"({int(Library_Sender_ID)},{int(Library_Getter_ID)},{int(Book_ID)},{int(quantity)})")
        self.Manager.save()
        return Book_ID,Library_Getter_ID,Library_Sender_ID,quantity

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

    def deleteEmployee(self):
        pass

    def deleteLibrary(self):
        pass

    def deleteSection(self):
        pass
