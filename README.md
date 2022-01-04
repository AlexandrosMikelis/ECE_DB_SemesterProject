# ECE_DB_SemesterProject

## Description
  Make a database for a network of Libraries
  
  Για το συγκεκριμένο project έπρεπε να δημιουργήσουμε μόνοι μας τον μικρόκοσμο και τις ανάγκες τους δικτύου.
  
  **Phase A** :
  - [x] Περιγραφή Μικρόκοσμού και βασικών λειτουργιών της ΒΔ.
  - [x] Σχεδίαση Εννοιολογικού Μοντέλου. (ERD) https://erdmaker.com
  - [x] Μετασχηματισμό απο Εννοιολογικό σε Λογικό Μοντέλο. (DBDesigner) https://www.dbdesigner.net/ (drawio) https://app.diagrams.net/
  
  **Phase B** :
  - [x] Δημιουργία της βάσης δεδομένων, με ιδιαίτερη έμφαση σε περιορισμούς αναφορικής ακεραιότητας.
  - [x] Διατυπώση εντολών SQL που επιτρέπουν αλλαγές στο περιεχόμενο της βάσης δεδομένων. (εντολές CRUD)
  - [ ] Διατυπώση ερωτημάτων SQL για ενδεικτικές τυπικές αναζητήσεις, όπως αυτές προκύπτουν από την προσδοκώμενη χρήση της ΒΔ.
  
  **Phase C** :
  - [ ] Δημιουργία της εφαρμογής που υλοποιεί τυπικά σενάρια χρήσης της βάσης δεδομένων και να επιδείξετε την λειτουργία της εισάγοντας δεδομένα.

## Microcosm
Διαπραγματευόμαστε ένα σύστημα το οποίο διαχειρίζεται πολλές βιβλιοθήκες όπου η κάθε μία έχει ένα όνομα, μία διέυθυνση και μία τοποθεσία. Κάθε βιβλιοθήκη αποτελείται από τομείς, κάθε τομέας χαρακτηρίζεται από ένα όνομα, έναν αριθμό και σε ποιον όροφο της  βιβλιοθήκης βρίσκεται. Για τη διευκόλυνση κάθε βιβλιοθήκης χωρίζουμε τα βιβλία όπου υπάρχουν σε κατηγορίες. Για την ομαλή οργάνωση της βιβλιοθήκης τοποθετούνται τα βιβλία σε συγκεκριμένες θέσεις (Διαδρόμος, Ράφι).  Επίσης, υπάρχει μία ειδική καταγραφή για τα βιβλία τα οποία θέλουν συντήρηση.

Κάθε βιβλιοθήκη εξυπηρετεί πελάτες όπου έρχονται σε αυτή με σκοπό να δανειστούν βιβλία. Δίνουμε την επιλογή στο πελάτη να επιλέξει μεταξύ κάποιων συνδρομών (Επί πληρωμή συνδρομή, Free …) ώστε να έχει τη δυνατότητα να δανειστεί βιβλία. Κάθε πελάτης μπορεί να δανειστεί μέχρι κάποιο ποσό βιβλίων ανάλογα με τη συνδρομή. Ο πελάτης έχει μια συγκεκριμένη ημερομηνία που πρέπει να τα επιστρέψει. Στη περίπτωση όπου ο πελάτης θέλει να δανειστεί ένα βιβλίο το οποίο δεν είναι διαθέσιμο μπορεί να το παραγγείλει και μπαίνει σε λίστα αναμονής. 

Κάθε βιβλιοθήκη έχει κάποιους εργαζόμενους που έχουν κάποιο συμβόλαιο με τη βιβλιοθήκη το οποίο ορίζει την εργασία τους(Τομέας εργασίας, προκαθορισμένο ποσό πληρωμής, ημερομηνία κ.λ.π). Επίσης βάση του συμβολαίου αυτού σε συνδυασμό με έξτρα ώρες εργασίας, μπόνους κ.λ.π βγαίνει και η τελική μηνιαία πληρωμή του εργαζόμενου. Υπάρχουν προϊστάμενοι οπού είναι υπεύθυνοι για μία ομάδα – τομέα. Επίσης όποιος είναι μάγκας δεν παίρνει άδεια αλλά γι’αυτούς που είναι τεμπέληδες υπάρχουν κάποιες μέρες όπου μπορούν να πάρουν άδεια, τις οποίες καταγράφουμε.

Το δικτυο μας θέλουμε να υποστηρίζει InterLibrary Loan , δηλαδή αν μια βιβλιοθήκη δεν έχει κάποιο βιβλιό να μπορεί να δανειστεί απο κάποια άλλη βιβλιοθήκη το εκάστοτε βιβλίο.

## ERD 
![DB Project ERD](https://user-images.githubusercontent.com/62079690/148119061-dd90d805-3b29-4ccb-90b0-5f21815f0677.jpg)

## Conceptual Design 
#### Using **DB Designer**
![Project_Conceptual_Design](https://user-images.githubusercontent.com/62079690/148118946-8242ce48-2933-4dc4-b022-28477d9cc8f8.png)
