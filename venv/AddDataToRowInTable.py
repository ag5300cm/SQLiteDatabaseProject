

import sqlite3
from sqlite3 import Error


def add_row_of_data(db_name_in_use, table_name_in_use, name, job_description, salary, years_employed, children):
    # Connecting to the database file
    #conn = sqlite3.connect(sqlite_file)
    conn = sqlite3.connect(db_name_in_use + ".sqlite")  # Todo change to variable so will user database user wants
    c = conn.cursor()

    try:
        #insert_statement = ("INSERT INTO 6Columns (primary, name, job_description, salary, years_employed, children) VALUES (?, ?, ?, ?, ?, ? )")
        c.execute("INSERT INTO base (name, Job, Salary, Years, Children) VALUES ( ?, ?, ?, ?, ? )",
                  (name, job_description, salary, years_employed, children))
        #c.execute(insert_statement, (primary, name, job_description, salary, years_employed, children))
        conn.commit()

    except sqlite3.IntegrityError:
        print("ID already exists ")

    c.close()
    conn.close()