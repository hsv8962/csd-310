# Pascual B. Villar
# CYBR410-305J
# Assignment: PySports_update
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="pysports_user",
  password="Makework90$",
  database="pysports"
)

# Create a cursor object
cursor = db.cursor()

# Function to insert a new player
def add_player_to_team(first_name, last_name, team_name):
    # Get the team_id for the given team_name
    cursor.execute("SELECT team_id FROM team WHERE team_name = %s", (team_name,))
    result = cursor.fetchone()
    if result:
        team_id = result[0]
        # Insert new player into player table
        cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES (%s, %s, %s)", (first_name, last_name, team_id))
        db.commit()
        print("Player added successfully.")
    else:
        print("Team not found.")

# Ask user for player details
first_name = input("Enter player's first name: ")
last_name = input("Enter player's last name: ")
team_name = input("Enter the team name the player is joining: ")

# Add player to team
add_player_to_team(first_name, last_name, team_name)

# Close the cursor and the connection
cursor.close()
db.close()