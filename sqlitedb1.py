'''To query data in an SQLite database from Python, you use these steps:

First, establish a connection to the SQLite database by creating a Connection object.
Next, create a Cursor object using the cursor method of the Connection object.
Then, execute a  SELECT statement.
After that, call the fetchall() method of the cursor object to fetch the data.
Finally, loop the cursor and process each row individually.'''
def create_connection(ckdb):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    import sqlite3

    conn = sqlite3.connect('ckdb')

    print ("Opened database successfully")
    '''conn = None
    try:
        conn = sqlite3.connect(ckdb)
    except Error as e:
        print(e)

    return conn'''


def select_all_items(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Newgeneral")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_newgeneral_by_group(conn, GroupId):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Newgeneral WHERE GroupId=?", (GroupId,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r'C:\Users\user\Desktop\dbases\ckdb.sqlite3'

    # create a database connection
    conn = create_connection(database)
    while conn == True:
        print("1. Query Newgeneral by group:")
        select_newgeneral_by_group(conn, 5)

        print("2. Query all Newgeneral")
        select_all_items(conn)

if __name__ == '__main__':
    main()