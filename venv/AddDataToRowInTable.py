

import sqlite3
from sqlite3 import Error


def add_row_of_data(db_name_in_use, table_name_in_use, primary, name, job_description, salary, years_employed, children):
    # Connecting to the database file
    #conn = sqlite3.connect(sqlite_file)
    conn = sqlite3.connect(db_name_in_use + ".sqlite")  # Todo change to variable so will user database user wants
    c = conn.cursor()

    try:
        #insert_statement = ("INSERT INTO 6Columns (primary, name, job_description, salary, years_employed, children) VALUES (?, ?, ?, ?, ?, ? )")
        c.execute("INSERT INTO " + table_name_in_use +" (Id, Name, Job, Salary, Years, Children) VALUES (?, ?, ?, ?, ?, ? )",
                  (primary, name, job_description, salary, years_employed, children))
        #c.execute(insert_statement, (primary, name, job_description, salary, years_employed, children))
        conn.commit()

    except sqlite3.IntegrityError:
        print("ID already exists ")

    c.close()
    conn.close()

def update_row_of_data(db_name_in_use, table_name_in_use, primary, choose_type,  updata_data):

    conn = sqlite3.connect(db_name_in_use + ".sqlite")  # Todo change to variable so will user database user wants
    c = conn.cursor()

    if choose_type == "Children":
        try:  # TODO below code will update Children for people in the data
            c.execute("UPDATE " + table_name_in_use + " SET Children = ? WHERE Id = ? ",
                      (updata_data, primary))
            #c.execute("UPDATE {tn} SET {cn}=('Hi World') WHERE Id = {idf}". \
            #          format(tn=table_name_in_use, cn=updata_data, idf=id_column))
            #insert_statement = ("INSERT INTO 6Columns (primary, name, job_description, salary, years_employed, children) VALUES (?, ?, ?, ?, ?, ? )")
            #c.execute("UPDATE base SET (name, Job, Salary, Years, Children) VALUES ( ?, ?, ?, ?, ? )",
            #          (name, job_description, salary, years_employed, children))
            #c.execute(insert_statement, (primary, name, job_description, salary, years_employed, children))
            conn.commit()
        except sqlite3.IntegrityError:
            print("What the Hell Happened!")
    elif choose_type == "Years":
        try:  #
            c.execute("UPDATE " + table_name_in_use + " SET Years = ? WHERE Id = ? ",
                      (updata_data, primary))
            conn.commit()
        except sqlite3.IntegrityError:
            print("What the Hell Happened!")
    elif choose_type == "Salary":
        try:  #
            c.execute("UPDATE " + table_name_in_use + " SET Salary = ? WHERE Id = ? ",
                      (updata_data, primary))
            conn.commit()
        except sqlite3.IntegrityError:
            print("What the Hell Happened!")
    elif choose_type == "Job":
        try:  #
            c.execute("UPDATE " + table_name_in_use + " SET Job = ? WHERE Id = ? ",
                      (updata_data, primary))
            conn.commit()
        except sqlite3.IntegrityError:
            print("What the Hell Happened!")
    elif choose_type == "Name":
        try:  #
            c.execute("UPDATE " + table_name_in_use + " SET Name = ? WHERE Id = ? ",
                      (updata_data, primary))
            conn.commit()
        except sqlite3.IntegrityError:
            print("What the Hell Happened!")
    else:
        print("Sorry you broke the program, no update.")

    c.close()
    conn.close()

