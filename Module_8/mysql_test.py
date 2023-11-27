import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'pysports_user',
    'password':'Makework90$',
    'host':'localhost',
    'database': 'pysports',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    print("Database connection succesful!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print ("Database not found!")
    else:
        print(err)
else:
    db.close()    