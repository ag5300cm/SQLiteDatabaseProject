
# Quick overview of all data types supported by SQLite 3
# INTEGER
# REAL : a floating point value
# TEXT
# BLOB : a blob of data for storing binary data
# NULL


import sqlite3
from sqlite3 import Error


def databaseAndTableStart(user_db_name, user_table_name):

    try:
        #sqlite_file = 'db.sqlite'    # name of the sqlite database file
        sqlite_file = user_db_name + ".sqlite"
        #table_name1 = 'table1'	 # name of the table to be created
        table_name1 = user_table_name
        new_field = 'Id_number'  # name of the column
        field_type = 'INTEGER'  # column data type

        # Connecting to the database file
        conn = sqlite3.connect(sqlite_file)  # if no table exists one should be created here with the 'db.sqlite' filename
        c = conn.cursor()

        # Creating a new SQLite table with 1 column
        #c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)' \
        #         .format(tn=table_name1, nf=new_field, ft=field_type))  # for different table name enter new one above same with columns
        c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY, Name TEXT, Job TEXT, Salary REAL, Years INTEGER, Children Null)'\
                .format(tn=table_name1, nf=new_field, ft=field_type))  # for different table name enter new one above same with columns

        # Committing changes and closing the connection to the database file
        conn.commit()
        #conn.close()
    except Error as e:  # this will prevent the program from crashing if database and table already exist
        print(e)
    finally:
        conn.close()
