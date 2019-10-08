#!/usr/bin/python

import sqlite3

conn = sqlite3.connect(r"C:\Users\user\Desktop\dbases\ckdb")
print ("Opened database successfully")

#'conn.execute('''CREATE TABLE COMPANY
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         AGE            INT     NOT NULL,
#         ADDRESS        CHAR(50),
#         SALARY         REAL);''') '
# print ("Table created successfully")


# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

# conn.commit()
# print ("Records created successfully")

cursor = conn.execute("SELECT * from Newgeneral  where groupid = 1")
for row in cursor:
   print ("serialid = ", row[0])
   print ("ename = ", row[1])
   print ("hname = ", row[2])
   print ("groupid = ", row[3])
   print ("image = ", row[6], "\n")

print ("Operation done successfully")
cursor = conn.execute("SELECT image from Newgeneral where serialid = 1")
for row in cursor:
   print ("serialid = ", row[0])
   print ("image = ", row[6])
 #  print ("hname = ", row[2])
 #  print ("groupid = ", row[3], "\n")

print ("Operation done successfully")
