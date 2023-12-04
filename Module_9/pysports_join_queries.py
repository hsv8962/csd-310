# Pascual B. Villar
# CYBR410-305J
# Module 9.2 Assignment: Pysports (Basic Table Joins)
# December 3, 2023

import mysql.connector

# Create a new database connection
db = mysql.connector.connect(
    host="localhost",       
    user="pysports_user",       
    password="Makework90$",   
    database="pysports"     
)

# Create a cursor object using the database connection
cursor = db.cursor()

# SQL query to perform an INNER JOIN
query = """
SELECT player.player_id, player.first_name, player.last_name, team.team_name
FROM player
INNER JOIN team ON player.team_id = team.team_id;
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
players = cursor.fetchall()

# Display the results
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print(f"Player ID: {player[0]}")
    print(f"First Name: {player[1]}")
    print(f"Last Name: {player[2]}")
    print(f"Team Name: {player[3]}\n")

# Close the cursor and database connection
cursor.close()
db.close()
