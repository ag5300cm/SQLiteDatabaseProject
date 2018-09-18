
#Project 2
#Write a database menu program that calls other programs in the same project.
#Menu Option 1 program creates a database and a table.
#Menu Option 2 program adds a row of data to the database table.
#Menu Option 3 program updates a row in the database table.
#Menu Option 4 program deletes a row from the database table.
#Menu Option 5 program displays all the rows in the database table.
#Menu Option 6 program display a single row of data based on an input value.
#Create a database table of products with a unique key and 6 additional of product data columns.
#  Use various data types and constraints such as Not Null, default values, etc.

import sqlite3
from sqlite3 import Error
import CreateDatabaseAndTable
import AddDataToRowInTable
import ReadFromDatabase
import DeleteDataBeCareful

try:
    import tkinter
except ImportError:
    print("No GUI option")


def create_connection():
    # create a database connection to a database that resides in the memory
    try:
        conn = sqlite3.connect(db_name_in_use)
        # TODO find a way to put future code here or something
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


# # PRIMARY KEY, Name TEXT, Job TEXT, Salary REAL, Years INTEGER, Children Null  # letting me know the 6 things in the table
# print("To Create database and table enter 'db'.")
# print("Add a row of data to the database table enter 'add'")
# print("To update a row of data enter 'update'")  #
# print("Delete a row of data by entering 'del'")  # todo
# print("Display all the rows of table by 'all' ")  #
# print("Display a single row of data be 'solo' ")  #
# print("Enter 'q' for quit")
# user_request = input("Enter input here: ")
# user_request = user_request.lower()
db_name_in_use = "data8"
table_name_in_use = "base"



loopMe = True
while loopMe:
    # PRIMARY KEY, Name TEXT, Job TEXT, Salary REAL, Years INTEGER, Children Null  # letting me know the 6 things in the table
    print("To Create database and table enter 'db'.")
    print("Add a row of data to the database table enter 'add'")
    print("To update a row of data enter 'update'")  #
    print("Delete a row of data by entering 'del'")  # todo
    print("Display all the rows of table by 'all' ")  #
    print("Display a single row of data be 'solo' ")  #
    print("Enter 'q' for quit")
    user_request = input("Enter input here: ")
    user_request = user_request.lower()

    if user_request == 'db':
        user_db_name = input("Please enter Database name: ")
        db_name_in_use = db_name_in_use + user_db_name
        #print(db_name_in_use)  # used for testing code
        user_table_name = input("Please enter Table name: ")
        table_name_in_use = user_table_name
        CreateDatabaseAndTable.databaseAndTableStart(user_db_name, user_table_name)
    elif user_request == 'add':
        #PRIMARY KEY, Name TEXT, Job TEXT, Salary REAL, Years INTEGER, Children Null
        primary = input("Enter Primary Key: ")
        name = input("Enter Name: ")
        job_description = input("Enter occupation: ")
        salary = input("Enter salary: ")
        years_employed = input("Enter year employed here: ")
        children = input("Enter number of children: ")
        AddDataToRowInTable.add_row_of_data(db_name_in_use, table_name_in_use, primary, name, job_description, salary, years_employed, children)
    elif user_request == 'update':
        primary = input("Enter Primary Key that need update: ")
        choose_type = str(input("Choose type: Id, Name, Job, Salary, Years, Children: "))
        update_data = input("Enter update data: ")
        AddDataToRowInTable.update_row_of_data(db_name_in_use, table_name_in_use, primary, choose_type, update_data)
    elif user_request == 'del':
        primaryDelete = input("Enter Primary Key that need delete: ")
        DeleteDataBeCareful.deleteARowFromTable(db_name_in_use, table_name_in_use, primaryDelete)
    elif user_request == 'all':
        ReadFromDatabase.read_all_from_database(db_name_in_use)
    elif user_request == 'solo':
        choose_search_type = str(input("Choose search type: Id, Name, Job, Salary, Years, Children: "))
        search_value = input("Enter specific value: ")
        ReadFromDatabase.read_from_database_search(db_name_in_use,  choose_search_type, search_value)
    elif user_request == 'q':
        exit(0)
    else:
        loopMe = True






