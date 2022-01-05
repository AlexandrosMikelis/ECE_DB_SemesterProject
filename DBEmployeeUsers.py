from DBManager import DBManager

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
            self.name = E_data[0][0]
            self.surname = E_data[0][1]

            Employee.Section["ID"] = E_data[0][-1]
            S_data = self.Manager.SELECT("Section","*",f"Section_ID = {E_data[0][-1]}")
            Employee.Section["Name"] = S_data[0][0]

            Employee.Library["ID"] = S_data[0][1]
            L_data = self.Manager.SELECT("Library","*",f"Library_ID = {S_data[0][1]}")
            Employee.Library["Name"] = L_data[0][2]

        else:
            print("Please enter valid Employee credentials")

    def Info(self):
        InfoTable = [] + f"{self.name},{self.surname},{self._email},{self._ssn}".split(",")
        InfoTable.append(Employee.Section)
        InfoTable.append(Employee.Library)
        return InfoTable

    def addBook(self,Title,ISBN,Author,Publisher,Availability,Quantity,Condition,Category_ID,Book_ID):
        self.Manager.INSERT("Book","(Title,ISBN,Author,Publisher,Availability,Quantity,Condition,Category_ID,Book_ID)",f"('{Title}',{int(ISBN)},'{Author}','{Publisher}',{bool(Availability)},{int(Quantity)},'{Condition}',{int(Category_ID)},{int(Book_ID)})")
        self.Manager.save()
    
    def showBook(self,filter,fields,values):
        val = f"and {values}" if values else ""
        if filter == 0:
            showcase = self.Manager.SELECT("Book,Library_Link_Book",','.join(fields),f"Library_Link_Book.Book_ID = Book.Book_ID {val}")
        elif filter == 1:
            showcase = self.Manager.SELECT("Book,Category",','.join(fields),f"Category.Category_ID = Book.Category_ID and Section_ID = {Employee.Section['ID']}")
        return showcase

    def deleteBook(self):
        pass
    
    def updateBook(self):
        pass
    
    def showCustomer(self):
        pass
    
    def addCustomer(self):
        pass
    
    def updateCustomer(self):
        pass

    def deleteCustomer(self):
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

    def deleteEmployee(self):
        pass

    def deleteLibrary(self):
        pass

    def deleteSection(self):
        pass
