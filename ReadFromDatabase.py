
import sqlite3
from sqlite3 import Error


def read_all_from_database(db_name_in_use):

    conn = sqlite3.connect(db_name_in_use + ".sqlite")  # Todo change to variable so will user database user wants
    c = conn.cursor()

    c.execute('SELECT * FROM base')  # TODO make base a variable
    all_info = c.fetchall()
    #print(all_info)
    for row in all_info:
        print(row)

    c.close()
    conn.close()


def read_from_database_search(db_name_in_use, choose_search_type, search_value):

    conn = sqlite3.connect(db_name_in_use + ".sqlite")  #
    c = conn.cursor()
    table_name = 'base'  # todo change base to whatever variable the user wants

    try:  # todo change base to whatever variable the user wants
            c.execute("SELECT * FROM {tn} WHERE {idf}={my_id}".\
                    format(tn=table_name,  idf=choose_search_type, my_id=search_value))
            id_exists = c.fetchall()
            if id_exists:
                #print('5): {}'.format(id_exists))
                for row in id_exists:  # part of the one that sort works
                    print(row)
            else:
                print('5): {} does not exist'.format(search_value))
            #c.execute("SELECT * FROM base WHERE " + choose_search_type + "=?", (search_value))  # this one sorta works
            #c.execute("SELECT * FROM base WHERE {goal} = ?".\
            #          format(goal=choose_search_type, search_value ))
            #all_info = c.fetchall()  # part of the one that sort works
            # print(all_info)
            #for row in all_info:  # part of the one that sort works
            #    print(row)
                # print(row[0])   # for primary key, use other numbers for different rows
    except Error as e:
            print(e)

    c.close()
    conn.close()


