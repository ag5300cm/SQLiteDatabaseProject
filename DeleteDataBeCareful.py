
import sqlite3
from sqlite3 import Error

def deleteARowFromTable(db_name_in_use, table_name_in_use, primary):

    conn = sqlite3.connect(db_name_in_use + ".sqlite")  #
    c = conn.cursor()
    #print(db_name_in_use, "   ", table_name_in_use, "   ", primary)  # used for testing code

    try:
        c.execute("DELETE FROM " + table_name_in_use + " Where Id = ?",
                  primary)
        conn.commit()
    except FileNotFoundError as e:
        print(e)

    c.close()
    conn.close()
