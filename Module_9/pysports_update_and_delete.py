# Pascual B. Villar
# CYBR410-305J
# Module 9.3 Assignment: PySport (Update & Delete)
# December 3, 2023


import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="pysports_user",
    password="Makework90$",
    database="pysports"
)

cursor = db.cursor()

# INSERT a new player into Team Gandalf (team_id = 1)
insert_query = "INSERT INTO player (first_name, last_name, team_id) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('Smeagol', 'Shire Folk', 1))
db.commit()
print("-- DISPLAYING PLAYERS AFTER INSERT --")

# SELECT query to display all player records
select_query = """
SELECT player.player_id, player.first_name, player.last_name, team.team_name
FROM player
INNER JOIN team ON player.team_id = team.team_id
ORDER BY player.player_id;
"""
cursor.execute(select_query)
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam Name: {player[3]}\n")
print()

# UPDATE the player's team to Team Sauron (team_id = 2)
update_query = "UPDATE player SET team_id = 2 WHERE first_name = 'Smeagol' AND last_name = 'Shire Folk'"
cursor.execute(update_query)
db.commit()
print("-- DISPLAYING PLAYERS AFTER UPDATE --")

# SELECT query to display the updated player record
cursor.execute(select_query)
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam Name: {player[3]}\n")
print()

# DELETE the player record
delete_query = "DELETE FROM player WHERE first_name = 'Smeagol' AND last_name = 'Shire Folk'"
cursor.execute(delete_query)
db.commit()
print("-- DISPLAYING PLAYERS AFTER DELETE --")

# SELECT query to display all player records after deletion
cursor.execute(select_query)
players = cursor.fetchall()
for player in players:
    print(f"Player ID: {player[0]}\nFirst Name: {player[1]}\nLast Name: {player[2]}\nTeam Name: {player[3]}\n")
print()
# Exit the program
input("press any key to continue...")

# Clean up and close the connection
cursor.close()
db.close()
