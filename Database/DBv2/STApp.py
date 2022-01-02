import streamlit as st
from DBManager import DBManager
from DBEmployeeUsers import Employee
import numpy as np
import pandas as pd
st.set_page_config(layout="wide")
st.sidebar.title("Welcome to LibNet")

email = st.sidebar.text_input("Email")
ssn = st.sidebar.text_input("SSN")

if st.sidebar.checkbox("Login") :
    Manager = DBManager("LibNetwork.db")
    Emp = Employee("JP@gmail.com",23080002895,Manager)
    menu = st.sidebar.radio(
        "Options",
        ('Home','Book','Customer'))
    
    if menu == "Home":
        inf = Emp.Info()
        Labels = ["Name","Surname","Email","SSN","Section","Library"]

        st.subheader(f"Welcome {inf[0]} {inf[1]}")
        st.write("**Employee Information**")
        
        for i in range(len(Labels)):
            cols = st.columns(2)
            cols[0].write(Labels[i])
            cols[1].write(inf[i])

    elif menu == "Book":
        st.subheader("Manage Library Books") 

        BookMenu = st.radio("Book Section",('Show Books','Add Book','Update Book','Delete Book'))
        if BookMenu == "Show Books":
            filters = st.columns(2)

            filters[0].write("**Filter**")
            filters[1].write("**Fields**")

            filter_option = filters[0].selectbox("Choose showcase filter",('Library','Section'))
            fields = filters[1].multiselect("Choose fields to display",['Title','ISBN','Author','Publisher','Availability','Condition'])

            if filter_option == 'Library':
                filter_= 0 
            elif filter_option == 'Section':
                filter_ = 1

            filters_by_value = st.columns(4)
            filters_by_value[0].write("**Filter by value**")
            filter_by_value = filters_by_value[0].multiselect("Choose specific values",['Title','Author','Publisher'])
            results = []
            if filter_by_value:
                for indx in range(0,len(filter_by_value)) :
                    filters_by_value[indx+1].write(f"**{filter_by_value[indx]}**")
                    results.append(filters_by_value[indx+1].text_input(f"Enter {filter_by_value[indx]}"))

            st.subheader("Books Showcase")
            if fields:
                fbv_string = ""
                for length in range(len(results)):
                    fbv_string = fbv_string + f"{filter_by_value[length]} = '{results[length]}' and"
                fbv_string = fbv_string[:-3]
                st.write(fbv_string)
                DataArray = np.array(Emp.showBook(filter_,fields,fbv_string))
                st.write(DataArray)
            
        elif BookMenu == "Add Book":

            st.subheader("Add a Book in the Library") 
            cols = st.columns(3)

            Title = cols[0].text_input("Add the title of the Book")
            ISBN = cols[1].text_input("ISBN")
            Author = cols[2].text_input("Author")
            Publisher = cols[0].text_input("Publisher")
            Availability = cols[1].text_input("Availability")
            Quantity = cols[2].text_input("Quantity")
            Condition = cols[0].text_input("Condition")
            Category_ID = cols[1].text_input("Category")
            Book_ID = cols[2].text_input("Book ID")

            Submit = cols[0].button("Submit")
            if Submit :
                Emp.addBook(Title,ISBN,Author,Publisher,Availability,Quantity,Condition,Category_ID,Book_ID)
else:
    st.write("Please Login with your Employee Credentials")
            

