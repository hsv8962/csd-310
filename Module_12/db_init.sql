
# Pascual B. Villar
# CYBR410-305J
# Assignment 10.3 WhatABook Database and Table Creation
# December 10, 2023

--  Drop the whatabook database
DROP DATABASE IF EXISTS whatabook;

-- Create the whatabook database
CREATE DATABASE whatabook;

USE whatabook;
SHOW TABLES;

-- Drop user and tables if they exist 
DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

-- Create user and grant privileges
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(user_id)
);

-- Create the Book table
CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(150) NOT NULL,
    details TEXT,
    author VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (book_id)
);

-- Create the Store table 
CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(150) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (store_id)
);

-- Create the Wishlist table
CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);

-- Insert records into the User table
INSERT INTO user (first_name, last_name) VALUES 
('Will', 'Smith'), 
('John', 'Travolta'), 
('Bruce', 'Willis');

-- Insert records into the Book table
INSERT INTO book (book_name, details, author) VALUES 
('In Search of Lost Time', 'Swann Way', 'Marcel Proust'), 
('Ulysses', 'Ulysses Chronicle', 'James Joyce'),
('Don Quixote', 'A retired country gentleman', 'Miguel de Cervantes'),
('One Hundred Years of Solitude', '20th century enduring works', 'Gabriel Garcia Marquez'),
('The Great Gatsby', 'Jazz Age', 'Scott Fitzgerald'),
('Moby Dick', 'Melville Masterpiece', 'Herman Melville'),
('War and Peace', 'Detailed events of War and Peace', 'Leo Tolstoy'),
('Hamlet', 'The Tragedy of Hamlet', 'William Shakespeare'),
('The Odyssey', 'Greek Epic Poem', 'Homer');

-- Insert a record into the Store table
INSERT INTO store (locale) VALUES ('1000 Galvin Rd S, Bellevue, NE 68005');

-- Insert records into the Wishlist table
-- This should only be done after the user and book tables have been created and populated
INSERT INTO wishlist (user_id, book_id) VALUES 
(1, 1),
(2, 2),
(3, 3);
