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