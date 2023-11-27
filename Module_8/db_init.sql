# Pascual B. Villar
# CYBR410-305J
# Assignment 8.2 PySports Setup
# November 26, 2023

USE pysports;
SHOW TABLES;

# Drop user and tables if they exist (to be run before creating them)
DROP USER IF EXISTS 'pysports_user'@'localhost';
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;

# Create user and grant privileges
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Makework90$';
GRANT ALL PRIVILEGES ON pysports.* TO 'pysports_user'@'localhost';

# Create the team table
CREATE TABLE team (
    team_id INT NOT NULL AUTO_INCREMENT,
    team_name VARCHAR(75) NOT NULL,
    mascot VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

# Create the player table and set the foreign key
CREATE TABLE player (
    player_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY (player_id),
    CONSTRAINT fk_team FOREIGN KEY (team_id) REFERENCES team(team_id)
);

# Insert team records
INSERT INTO team (team_name, mascot) VALUES ('Team Gandalf', 'White Wizards');
INSERT INTO team (team_name, mascot) VALUES ('Team Sauron', 'Orcs');
