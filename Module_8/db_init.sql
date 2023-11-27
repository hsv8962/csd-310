USE pysports;
SHOW TABLES;

# create pysports_user and grant them all priviledges to the pysports database
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY Makework90$;

# grant all priviledges to the pysports database to user pysports user on localhost
GRANT ALL PRIVILEDGES ON pysports.* TO'pysports_user'@'localhost';

# drop test user if exists
DROP USER IF EXISTS 'pysports_user'@'localhost';

DROP TABLE IS EXISTS team;

# create the team table
CREATE TABLE team (
    team_id INT
    team_name VARCHAR(75) NOT NULL AUTO_INCREMENT,
    mascot    VARCHAR(75) NOT NULL,
    PRIMARY KEY(team_id)
);

# create the player table and set the foreign key
CREATE TABLE player (
    player_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    team_id INT NOT NULL,
    PRIMARY KEY (player_id)
    CONSTRAINT fk_team
    FOREIGN KEY (team_id)
        REFERENCES team(team_id)
);

# insert tean records
INSERT INTO team (team_name, mascot)
VALUES ('Team Gandalf', 'White Wizards')
INSERT INTO team (team_name, mascot)
VALUES ('Team Sauron', 'Orcs');

# drop table if they are present
DROP TABLE IF EXISTS player;
SELECT team_id FROM team WHERE team_name = 'Team Sauron';


