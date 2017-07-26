import mysql.connector

config = {
          'user': 'root',
          'password': '',
          'host': '127.0.0.1',
          'database': 'information_schema',
          'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

#try:
#    cnx = mysql.connector.connect(**config)
    #print("Connection successful")
#except mysql.connector.Error as err:
#    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#        print("Something is wrong with your user name or password")
#    elif err.errno == errorcode.ER_BAD_DB_ERROR:
#        print("Database does not exist")
#    else:
#        print(err)
#else:
#    cnx.close()

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = cnx.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM character_sets")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

#close the connection
cnx.close()