# Pascual B. Villar
# CYBR410-305J
# Assignment 10.3 WhatABook Database and Table Creation
# November 28, 2023

# Create the whatabook database
CREATE DATABASE IF NOT EXISTS whatabook;

USE whatabook;
SHOW TABLES;

# Drop user and tables if they exist (to be run before creating them)
DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Wishlist;
DROP TABLE IF EXISTS Store;

# Create user and grant privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

# Create the User table
CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id)
);

# Create the Book table
CREATE TABLE Book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY (book_id),
);

# Create the Wishlist table
CREATE TABLE Wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

# Create the Store table 
CREATE TABLE Store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY (store_id)
);
# Insert records into the User table
INSERT INTO User(first_name, last_name) VALUES ('Will', 'Smith'), ('John', 'Travolta'), ('Bruce', 'Willis');

# Insert records into the Book table
INSERT INTO Book (book_name, details, author) VALUES ('In Search of Lost Time', 'Swann Way', 'Marce Proust'), 
('Ulysses', 'Ulysses Chronicle', 'James Joyce'),
('Don Quixote', 'a retired country gentlemen', 'Miguel de Cervantes'),
('One Hundred Years of Solitude', '20th century enduring works', 'Gabriel Garcia Marquez'),
('The Great Gatsby', 'Jazz Age', 'Scott Fitzgerald'),
('Molby Dick', 'Melville Masterpiece', 'Herman Malville'),
('War and Peace', 'War and Peace detail events', 'Leo Tolstoy'),
('Hamlet', 'The Tragedy of Hamlet', 'William Shakespear'),
('The Odyssey', 'Greek Epic Poem', 'Homer');

# Insert a record into the STore table
INSERT INTO Store (locale) VALUES ('1000 Galvin Rd S, Bellevue, NE 68005');

# Insert records into the Wishlist table
INSERT INTO Wishlist (user_id, book_id) VALUES 
(1,1),
(2,2),
(3,3);

