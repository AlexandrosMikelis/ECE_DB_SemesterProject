def insert_category(conn):
    print("    ","-"*60)
    print("    Welcome to Category Manager.\n        Here you can add a new category for your books")
    print("    ","-"*60)
    
    try:
        Name = input("    Please enter a new Category name : ")
        Category_ID = input("    Add an ID for your Category : ")
        Section_ID = input("    Add the Section ID : ")

        conn.execute('''INSERT INTO Category (Name,Section_ID,Category_ID) VALUES ('{}',{},{})'''.format(Name,Section_ID,Category_ID))
        
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        
def select_category(conn):
    Categories = []
    cursor = conn.execute("SELECT Name from Category")
    for row in cursor:
        Categories.append(row[0])

    Categories = list(dict.fromkeys(Categories))
    return Categories

def insert_book(conn):
    print("-"*60)
    print(" Welcome to Book Manager.\n    Here you can add a new book into your Library.")
    print("-"*60)
    try:
        Title = input("Title         : ")
        ISBN = int(input("ISBN          : "))
        Author = input("Author        : ")
        Publisher = input("Publicher     : ")
        Availability = bool(input("Availability  : "))
        Quantity = int(input("Quantity      : "))
        Condition = input("Condition     : ")
        
        print(select_category(conn))
        if(input("Does the category of the book belong here [Y/n]?") in "Yy" ):
            pass
        else:
            insert_category(conn)
        Category = int(input("Category ID :"))   
        Book_ID = int(input("Book_ID :"))
        
        conn.execute('''INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Quantity,Condition,Category_ID,Book_ID) \
                     VALUES ('{}',{},'{}','{}',{},{},'{}',{},{})'''.format(Title,ISBN,Author,Publisher,Availability,Quantity,Condition,Category,Book_ID))

        print("The book succefully inserted.Please provide us the Library you want it")
        select_library()
        #MUST BE A DIFFERENT FUNCTION
        Library_ID = input("Enter Library ID: ")
        conn.execute('''INSERT INTO Library_Link_Book (Book_ID,Library_ID) \
                     VALUES ({},{})'''.format(Book_ID,Library_ID))
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        
def select_book(conn):
    cursor = conn.execute("SELECT Title,ISBN,Author,Publisher,Availability,Quantity,Condition from Book")
    for row in cursor:
        print(row[0]," ",row[1]," ",row[2]," ",row[3]," ",row[4]," ",row[5]," ",row[6])
    
def select_library(conn):
    cursor = conn.execute("SELECT Name,Library_ID from Library")
    for row in cursor:
        print(row[0]," "*30,row[1])

def App(conn):
    print("Welcome to DBManager")
    while(1):
        print("Option 0: Type '0' to Save")
        print("Option 1: Type '1' to Insert a new Book")
        print("Option 2: Type '2' to Review all Books in DB")
        print("Press nothing to exit")
        
        try:
            choice = int(input("Please Enter the option you want : "))
        except:
            break
        if choice == 0:
            conn.commit()
        elif choice == 1:
            insert_book(conn)
        elif choice == 2:
            select_book(conn)
        else:
            break
        
import sqlite3

conn = sqlite3.connect('LibNetwork.db')
App(conn)
conn.commit()
conn.close()
