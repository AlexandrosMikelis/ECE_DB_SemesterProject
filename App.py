from logging import PlaceHolder, error
import streamlit as st
from DBManager import DBManager
from DBEmployeeUsers import Employee
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

DBPath = "Database/LibNetwork.db"

def ClearData(data):
    clearedData = []
    for d in data:
        clearedData.append(d[0])
    return tuple(clearedData)

st.set_page_config(layout="wide")
st.sidebar.title("Welcome to LibNet")

email = st.sidebar.text_input("Email")
ssn = st.sidebar.text_input("SSN")

if st.sidebar.checkbox("Login") :

    Manager = DBManager(DBPath)
    Emp = Employee("JP@gmail.com",23080002895,Manager)
    menu = st.sidebar.radio("Options",('Home','Book','Customer'))

    if menu == "Home":
        inf = Emp.Info()
        st.subheader(f"Welcome {inf[0]} {inf[1]}")
        st.write("**Employee Information**")

        Labels = ["Name","Surname","Email","SSN","Section","Library","Hours_Of_Work"] 
        image = Image.open('Photos/Icon.jpg')
        EmployeeContainer = st.columns([2,2,2])

        EmployeeContainer[0].image(image, caption='Employee Photo')

        for blank in range(3):
            EmployeeContainer[1].write(" ")
            EmployeeContainer[2].write(" ")

        for i in range(len(Labels)):
            if i == 4 or i == 5:
                EmployeeContainer[1].write(Labels[i])
                EmployeeContainer[2].write(str(inf[i]["Name"]) + " | ID: " + str(inf[i]["ID"]) )
            else:
                EmployeeContainer[1].write(Labels[i])
                EmployeeContainer[2].write(inf[i])

    elif menu == "Book":
        st.subheader("Manage Library Books") 
        BookMenu = st.radio("Book Section",('Show Books','Add Book','Update Book','Delete Book','Lend a Book','Inter Loaning','New Order','New warning'))

        if BookMenu == "Show Books":

            results = []
            fbv_string = ""

            filters = st.columns(2)
            filters_by_value = st.columns(4)

            filters[0].write("**Filter**")
            filter_option = filters[0].selectbox("Choose showcase filter",('Library','Section'))
            filter_ = 0 if filter_option == 'Library' else 1 

            filters[1].write("**Fields**")
            fields = filters[1].multiselect("Choose fields to display",['Title','ISBN','Author','Publisher','Availability','Condition'])

            filters_by_value[0].write("**Filter by value**")
            filter_by_value = filters_by_value[0].multiselect("Choose specific values",['Title','Author','Publisher'])
            
            if filter_by_value:
                for indx in range(0,len(filter_by_value)) :
                    filters_by_value[indx+1].write(f"**{filter_by_value[indx]}**")
                    results.append(filters_by_value[indx+1].text_input(f"Enter {filter_by_value[indx]}"))

            st.subheader("Books Showcase")

            if fields:
                for length in range(len(results)):fbv_string = fbv_string + f" {filter_by_value[length]} = '{results[length]}' and"
                fbv_string = fbv_string[:-3]
                st.write(fbv_string)
                DataArray = np.array(Emp.showBook(filter_,fields,fbv_string))
                st.write(DataArray)
            
        elif BookMenu == "Add Book":
            st.subheader("Add a Book in the Library") 

            cols = st.columns(3)

            CategoriesTable = Manager.SELECT("Category","Category_Name,Category_ID",f"Section_ID = '{Emp.Section['ID']}'")

            Title = cols[0].text_input("Add the title of the Book")
            Publisher = cols[0].text_input("Publisher")
            Category_ID = cols[0].selectbox("Category",ClearData(CategoriesTable))
            Submit = cols[0].button("Submit")

            ISBN = cols[1].text_input("ISBN")
            Availability = cols[1].selectbox("Availability",("True","False"))
            Availability = "" if Availability=="False" else "True"

            Author = cols[2].text_input("Author")
            Condition = cols[2].selectbox("Condition",("Good","Medium","Bad"))
            
            Category_ID = [content[1] for content in CategoriesTable if content[0]==Category_ID][0]
            
            if Submit :
                try:
                    Emp.addBook(Title,ISBN,Author,Publisher,Availability,Condition,Category_ID)
                    st.write("Congratulations, You successfully add a new Book.")
                except error as e :
                    st.write(e)

        elif BookMenu == "Update Book":
            st.subheader("Update a Book from Library")

            S_results = []
            C_results = []
            con_string = ""
            set_string = ""
            TwoColumnOrder = st.columns(2)
            ThreeColumnOrder = st.columns(6)
            Submit = st.button("Submit")

            Setter = TwoColumnOrder[0].multiselect("Setters",['Title','ISBN','Author','Publisher','Availability','Condition','Category_ID'])
            Condition = TwoColumnOrder[1].multiselect("Conditions",['Book Title','Book Category_ID','Book ISBN','Book Author','Book Publisher','Book Availability','Book Condition'])

            if Setter :
                S_results = [ThreeColumnOrder[indx%3].text_input(f"Enter {Setter[indx]}") for indx in range(0,len(Setter))] 
                for length in range(len(S_results)):set_string = set_string + f" {Setter[length]} = '{S_results[length]}' and" if Setter[length] not in ('Category_ID','ISBN') else set_string + f" {Setter[length]} = {S_results[length]} and"
                set_string = set_string[:-3]

            if Condition :
                C_results = [ThreeColumnOrder[3+(indx%3)].text_input(f"Enter {Condition[indx]}") for indx in range(0,len(Condition))]
                for length in range(len(C_results)):con_string = con_string + f" {Condition[length]} = '{C_results[length]}' and" if Condition[length] not in ('Book Category_ID','Book ISBN') else con_string + f" {Condition[length]} = {C_results[length]} and"
                con_string = con_string[:-3]
                con_string = con_string.replace("Book ","")
            
            if Submit:
                try:
                    Emp.updateBook(set_string,con_string)
                    st.write("Congratulations, Book is up to date.")
                except error as e :
                    st.write(e)
                
        elif BookMenu == "Delete Book":
            st.subheader("Delete a Book from Library")

            C_results = []
            con_string = ""
            TwoColumnOrder = st.columns(2)
            ThreeColumnOrder = st.columns(3)
            Submit = st.button("Submit")

            Condition = TwoColumnOrder[0].multiselect("Conditions",['Title','ISBN','Author','Publisher','Availability','Condition','Category_ID'])

            if Condition :
                C_results = [ThreeColumnOrder[(indx%3)].text_input(f"Enter {Condition[indx]}") for indx in range(0,len(Condition))]
                for length in range(len(C_results)):con_string = con_string + f" {Condition[length]} = '{C_results[length]}' and" if Condition[length] not in ('Category_ID','ISBN') else con_string + f" {Condition[length]} = {C_results[length]} and"
                con_string = con_string[:-3]
                con_string = con_string.replace("Book ","")
            
            if Submit and Condition:
                try:
                    st.write(con_string)
                    Emp.deleteBook(con_string)
                    st.write("Congratulations, Book is deleted.")
                except error as e :
                    st.write(e)
        elif BookMenu == 'Lend a Book':
            st.subheader("Lend a Book from Library")

            C_email = st.text_input("Please Enter Customer Email")
            Book_Title = st.text_input("Title")
            Submit = st.button("Submit")

            if Submit:
                values = Emp.LendBook(C_email,Book_Title)
                st.write(values)
        elif BookMenu == 'Inter Loaning':
            pass
        elif BookMenu == 'New Order':
            pass
        elif BookMenu == 'New warning':
            pass
        Manager.close()
    elif menu == "Customer":
        pass
else:
    st.subheader("Welcome Guest")
    st.write("Please **Login** with your **Employee Credentials**")
            

