/*
	C: CREATE
*/

/* 
	Library creation
*/

--INSERT INTO Library (Library_Location,Library_Address,Library_Name,Library_Phone) VALUES ('Πανεπιστήμιο Πατρών','Ypatias, Panepistimioupoli Patron 265 04','Βιβλιοθήκη & Κέντρο Πληροφόρησης, Πανεπιστήμιο Πατρών',2610969621);
--INSERT INTO Library (Library_Location,Library_Address,Library_Name) VALUES ('Τρίπολη','Τρίπολη 221 00','Κεντρική Βιβλιοθήκη Πανεπιστημίου Πελοποννήσου');

/*
	Section creation
*/

--INSERT INTO Section (Section_Name,Library_ID,Section_ID,Section_Floor,Section_Number) VALUES ('Main Section: Ακαδημαικά Συγράματα',1,1,1,001);
--INSERT INTO Section (Section_Name,Library_ID,Section_ID,Section_Floor,Section_Number) VALUES ('Main Section: Ακαδημαικά Συγράματα',2,2,1,001);

/*
	Category creation
*/

--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Μαθηματικά',1,1);
--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Φυσική',2,1);
--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Χημεια',3,1);
--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Φιλολογία',4,1);

--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Μαθηματικά',5,2);
--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Ψυχολογία',6,2);
--INSERT INTO Category (Category_Name,Category_ID,Section_ID) VALUES ('Οικονομικά',7,2);
/*
	Put Categories in position
	
		Library A								|		Library B
												|
												|
												|
												|
												|
												|
*/
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (1,1,1);
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (2,1,2);
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (3,1,3);
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (4,2,1);

--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (5,1,1);
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (6,3,2);
--INSERT INTO Position(Category_ID,Hallway_Number,Shelf_Number) VALUES (7,3,3);
/*
	Book creation 
*/

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Μαθηματική ανάλυση Ι',9789609400251,'Ρασσιάς Θεμιστοκλής Μ.','Συμεών',true,'Good',1);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Μαθηματική ανάλυση ΙΙ',9789607888822,'Ρασσιάς Θεμιστοκλής Μ.','Συμεών',true,'Good',1);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΓΡΑΜΜΙΚΗ ΑΛΓΕΒΡΑ ΚΑΙ ΕΦΑΡΜΟΓΕΣ',9789607309709,'ΣΤΡΑΝΓΚ ΓΚΙΛΜΠΕΡΤ','Πανεπιστημιακές Εκδόσεις Κρήτης',true,'Good',1);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Μερικές διαφορικές εξισώσεις',9789605240905,'Τραχανάς Στέφανος Λ.','Πανεπιστημιακές Εκδόσεις Κρήτης',true,'Good',1);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Συνήθεις διαφορικές εξισώσεις',9789605240899,'Τραχανάς Στέφανος Λ.','Πανεπιστημιακές Εκδόσεις Κρήτης',true,'Good',1);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Εισαγωγή στη Θεωρία Πιθανοτήτων και Εφαρμογές',9789609380935,'Μ. Κούτρας','Μ. Κούτρας',true,'Good',1);

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Φυσική για Επιστήμονες και Μηχανικούς-Τόμος Α',9789605082703,'Knight R.D.','Εκδοτικός Όμιλος ΙΩΝ',true,'Good',2);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΦΥΣΙΚΗ ΓΙΑ ΕΠΙΣΤΗΜΟΝΕΣ ΚΑΙ ΜΗΧΑΝΙΚΟΥΣ',9789604615087,' RAYMOND A. SERWAY, JOHN W. JEWETT','ΕΚΔΟΣΕΙΣ ΚΛΕΙΔΑΡΙΘΜΟΣ ΕΠΕ',true,'Good',2);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Εισαγωγή στα ηλεκτρικά κυκλώματα',9789604182626,'Alexander Charles K., Sadiku Matthew N. O.','Τζιόλα',true,'Good',2);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Εισαγωγή στα ηλεκτρικά κυκλώματα',9789604182626,'Alexander Charles K., Sadiku Matthew N. O.','Τζιόλα',true,'Good',2);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΦΥΣΙΚΗ (ΠΡΩΤΟΣ ΤΟΜΟΣ)',9789600122343,'HALLIDAY DAVID, RESNICK ROBERT, WALKER JEARL','GUTENBERG',true,'Good',2);

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΟΡΓΑΝΙΚΗ ΧΗΜΕΙΑ',9789605244910,'MCMURRY JOHN','ΠΕΚ (ΠΑΝΕΠΙΣΤΗΜΙΑΚΕΣ ΕΚΔΟΣΕΙΣ ΚΡΗΤΗΣ)',true,'Good',3);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΑΝΟΡΓΑΝΗ ΧΗΜΕΙΑ ΤΟΜΟΣ Α ΒΑΣΙΚΕΣ ΑΡΧΕΣ',9603515833,'ΠΝΕΥΜΑΤΙΚΑΚΗΣ Γ.-ΜΗΤΣΟΠΟΥΛΟΥ Χ.-ΜΕΘΕΝΙΤΗΣ Κ.','ΣΤΑΜΟΥΛΗΣ',true,'Good',3);

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΙΣΤΟΡΙΑ ΤΗΣ ΡΩΜΑΪΚΗΣ ΛΟΓΟΤΕΧΝΙΑΣ (ΣΕ ΕΝΑΝ ΤΟΜΟ)',9789605240363,'VON ALBRECHT MICHAEL','ΙΤΕ-ΠΑΝΕΠΙΣΤΗΜΙΑΚΕΣ ΕΚΔΟΣΕΙΣ ΚΡΗΤΗΣ',true,'Good',4);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΑΡΧΑΙΑ ΕΛΛΗΝΙΚΑ ΚΕΙΜΕΝΑ ΤΗΣ ΚΛΑΣΙΚΗΣ ΠΕΡΙΟΔΟΥ. Α. ΡΗΤΟΡΙΚΑ ΚΕΙΜΕΝΑ',9786188335806,'ΑΜΦΙΛΟΧΙΟΣ ΠΑΠΑΘΩΜΑΣ','ΕΚΔΟΣΕΙΣ TRANSVERSA CHARTA',true,'Good',4);


--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Μαθηματική ανάλυση Ι',9789609400251,'Ρασσιάς Θεμιστοκλής Μ.','Συμεών',true,'Good',5);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Αριθμητική Γραμμική Άλγεβρα',9789609495462,'Καραγιαννάκης Δημήτρης','Δίσιγμα',true,'Good',5);
--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('ΓΡΑΜΜΙΚΗ ΑΛΓΕΒΡΑ ΚΑΙ ΕΦΑΡΜΟΓΕΣ',9789607309709,'ΣΤΡΑΝΓΚ ΓΚΙΛΜΠΕΡΤ','Πανεπιστημιακές Εκδόσεις Κρήτης',true,'Good',5);

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Εκπαιδευτική Ψυχολογία',9789605082994,'Anita Woolfolk','Εκδοτικός Όμιλος ΙΩΝ',true,'Good',6);

--INSERT INTO Book (Title,ISBN,Author,Publisher,Availability,Condition,Category_ID) VALUES ('Μακροοικονομική θεωρία-Ενιαίο',9789600109370,'Mankiw Gregory N.','Gutenberg',true,'Good',7);

/*
	Employee creation
*/

--INSERT INTO Employee ("Employee_ID ",First_Name,Last_Name,Email,Phone,Address,Section_ID) VALUES (23080002895,'John','Papadopoulos','JP@gmail.com',6978901211,'Agia Sofia 23',1);
--INSERT INTO Employee ("Employee_ID ",First_Name,Last_Name,Email,Phone,Mgr_ID,Address,Section_ID) VALUES (23080002896,'Alexandros','Mikelis','AM@gmail.com',6978901212,23080002895,'Agia Sofia 24',1);
--INSERT INTO Employee ("Employee_ID ",First_Name,Last_Name,Email,Phone,Mgr_ID,Address,Section_ID) VALUES (23080002897,'John','Skarpetis','JS@gmail.com',6978901213,23080002895,'Agia Sofia 25',1);

/*
	Employee Contract creation
*/

--INSERT INTO Employee_Contract(Employee_ID,Days_Off,Standard_Payment,Employee_Job,Start_Date,End_Date) VALUES (23080002895,25,1200,"Διαχειρηστής","24-5-2020","24-5-2025");
--INSERT INTO Employee_Contract(Employee_ID,Days_Off,Standard_Payment,Employee_Job,Start_Date,End_Date) VALUES (23080002896,14,800,"Yπάλληλος","26-8-2021","26-8-2024");
--INSERT INTO Employee_Contract(Employee_ID,Days_Off,Standard_Payment,Employee_Job,Start_Date,End_Date) VALUES (23080002897,14,800,"Βιβλιοθηκάριος","12-3-2021","12-3-2024");

/*
	Customer creation
*/

--INSERT INTO Customer(First_Name,Last_Name,Phone_Number,Email,Address) VALUES ("George","Giannopoulos",6989029455,"G.Giannopoulos@gmail.com","Riga Feraiou 29");
--INSERT INTO Customer(First_Name,Last_Name,Phone_Number,Email,Address) VALUES ("Anastasia","Papadimitriou",6979079385,"AnaPapa@gmail.com","Korinthou 90");
--INSERT INTO Customer(First_Name,Last_Name,Phone_Number,Email,Address) VALUES ("Periklis","Papanikolaou",6979899435,"Periklis@gmail.com","Maizonos 46");

/*
	Customer Membership creation
*/

--INSERT INTO Customer_Membership(Customer_ID,Start_Date,End_Date,Title,Max_Books,Payment) VALUES (1,"1-1-2022","1-1-2023","Gold Membership",15,40);
--INSERT INTO Customer_Membership(Customer_ID,Start_Date,End_Date,Title,Max_Books,Payment) VALUES (2,"10-1-2022","10-7-2022","Silver Membership",7,20);
--INSERT INTO Customer_Membership(Customer_ID,Start_Date,End_Date,Title,Max_Books,Payment) VALUES (3,"21-12-2021","21-1-2023","Free Membership",2,0);
/*
	Relate customers with there Library
*/
--INSERT INTO Library_Serves_Customers(Library_ID,Customer_ID) VALUES (1,1);
--INSERT INTO Library_Serves_Customers(Library_ID,Customer_ID) VALUES (1,2);
--INSERT INTO Library_Serves_Customers(Library_ID,Customer_ID) VALUES (1,3);

--INSERT INTO Library_Serves_Customers(Library_ID,Customer_ID) VALUES (2,2);
/*

*/

/*
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (2,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (3,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (4,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (5,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (6,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (7,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (8,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (9,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (10,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (11,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (12,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (13,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (14,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (15,1);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (16,2);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (17,2);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (18,2);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (19,2);
INSERT INTO Library_Contains_Books(Book_ID,Library_ID) VALUES (20,2);
*/

/* Let's say now that Anastasia Papadimitriou wants to borrow 'Μαθηματική ανάλυση Ι' and she is a customer of 'Βιβλιοθήκη & Κέντρο Πληροφόρησης, Πανεπιστήμιο Πατρών'
	Anastasia is a silver member so the books she borrows must be return within one month of start date.Let's say Anastasia comes to our library in 12-1-2022 to take the book.*/
	
--INSERT INTO Borrowing (Customer_ID,Start_Date,End_Date) VALUES (2,"12-1-2022","12-2-2022");
--INSERT INTO Borrowing_Contains_Books(Book_ID,Customer_Borrowing_ID) VALUES (1,2);

/* LEND A BOOK  -  REAL LIFE SCENARIO*/
------------------------------------------------------------------------------------------------------------------------------------------
 /* Let's say that now Anastasia brought back the Book ON 18-1-2022*/
 -- UPDATE Borrowing SET Final_End_Date="18-1-2022" WHERE Customer_ID = 2;
/*But Anastasia brought the Book in a bad condition*/
--UPDATE Book SET Condition='Bad' WHERE Book_ID=1;
/*Anastasia have to take a penalty in her payment and we need to put the book in maintanance*/
--UPDATE Customer_Membership SET Payment = (SELECT Payment FROM Customer_Membership WHERE Customer_ID = 2) + 5 WHERE Customer_ID=2;
--INSERT INTO Maintenance(Start_Date,Maintainance_Type) VALUES ("18-1-2022","Bad Damage");
--UPDATE Book SET Availability=false WHERE Book_ID=1;
/* And we get that book in 20-1-2022*/
--UPDATE Maintenance SET End_Date="20-1-2022" WHERE Maintenance_ID=1;
--UPDATE Book SET Availability=true , Condition="Good" WHERE Book_ID=1;
-------------------------------------------------------------------------------------------------------------------------------------------

/*TAKE A DAY OFF AND GET PAID IN THE SAME DAY AS EMPLOYEE*/
-------------------------------------------------------------------------------------------------------------------------------------------
/* Lets say Alexandros Mikelis wants to take a day off on his payment day 1-2-2022 to 4-2-2022*/
--INSERT INTO Employee_Day_Off (Description,End_Date,Start_Date,Employee_ID) VALUES ("Αναρωτική Αδεια","4-2-2022","1-2-2022",23080002896);
--INSERT INTO Employee_Payment(Payment_With_Insurance,Date,Bonus,FPA,Employee_ID,Library_ID) VALUES (1000,"1-2-2022",0,12,23080002896,1);
-------------------------------------------------------------------------------------------------------------------------------------------

/*ORDER A BOOK THAT LIBRARY DOSENT HAVE AND LEND IT FROM ANOTHER Library
-------------------------------------------------------------------------------------------------------------------------------------------
/*Lets say John Skarpetis wants "Μακροοικονομική θεωρία-Ενιαίο" and ask Anastasia Papadimitriou for that 13-1-2022*/
-------------------------------------------------------------------------------------------------------------------------------------------
--INSERT INTO Customer_Orders_Book(Customer_ID,Book_ID,Date_Of_Order) VALUES (3,20,"13-1-2022");
--INSERT INTO Inter_Library_Loaning(Library_Sender,Library_Getter,Book_ID,Quantity) VALUES (2,1,20,1);

UPDATE Maintenance SET Start_Date="2022-01-18",End_Date="2022-01-20",Book_ID=1 WHERE Maintainance_Type="Bad Damage";