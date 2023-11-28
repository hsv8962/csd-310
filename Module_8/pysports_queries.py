# Pascual B. Villar
# CYBR420-305J
# Assignment: Module 8.3 (Table Queries)
# November 24, 2023

import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    'user': 'pysports_user',
    'password':'Makework90$',
    'host':'localhost',
    'database': 'pysports',
    'raise_on_warnings': True
}

try:
    # Connection to the pysports database
    db = mysql.connector.connect(**config)

    # Cursor for executing queries
    cursor = db.cursor()

    # SELECT query for the team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    teams = cursor.fetchall()

    print("--DISPLAY TEAM RECORDS--")
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()

    # SELECT query for the team table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()

    print("--DISPLAYING PLAYER RECORDS--")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()


except mysql.connector.Error as err:
        # Handle errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Username or Password is incorrect!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist!")
        else:
            print(err)
else:
    # Add a prompt to press any key to continue
    input ("Press any key to continue...")
    # Close the connection
    db.close()

# End of script



        
