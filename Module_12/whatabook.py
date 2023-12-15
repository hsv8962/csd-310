
# Pascual B. Villar
# CYBR410-305J
# WhatABook Project: whatabook.py
# December 10, 2023



import mysql.connector
from mysql.connector import errorcode

# Database config object
config = {
    'user': 'whatabook_user',
    'password': 'MySQL8IsGreat!',
    'host': 'localhost',
    'database': 'whatabook',
    'raise_on_warnings': True
}

try:
    # Connection to the whatabook database
    db = mysql.connector.connect(**config)
    print('Database connection successful.')

    # Curson for executing queries
    cursor = db.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" Username or Password is incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# Access the Main Menu (User Interface Requirement)
def show_menu(): # User Interface (1)
    print("\nMain Menu")
    print("1. View Books") # Displays all the books
    print("2. View Store Locations") # Displays store locations
    print("3. My Account") # Prompt to enter a user_id (1,2,3)
    print("4. Exit Program")

def show_books(cursor): # User Interface (2)
    # Simulate fetching books from the database
    cursor.execute("SELECT book_id, book_name, details, author FROM book")
    books = cursor.fetchall()
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Details: {book[2]}, Author: {book[3]}")

def show_location(cursor): # User Interface (3)
    # Simulate fetching store locations from the database
    cursor.execute("SELECT store_id, locale FROM store")
    locations = cursor.fetchall()
    for location in locations:
        print(f"Location ID: {location[0]}, Address: {location[1]}")

def validate_user(cursor, user_id): # User Interface (4)
    """
    Check if the provided user_id exists in the database.
    """
    try:
    # Simulate user validation
        cursor.execute("SELECT user_id FROM user WHERE user_id = %s", (user_id,))
        return cursor.fetchone() is not None
    except mysql.connector.Error as err:
        print("Error validating user: ", err)
        return False

# Display the Wishlist Menu (User Interface Requirement)
def show_account_menu(): # User Interface (5)
    print("\nAccount Menu")
    print("1. View Wishlist") # Display wishlist
    print("2. Add Book") # Displays all available books to be addedd
    print("3. Main Menu") # User's option to go back to the main menu

def show_wishlist(cursor, user_id): # User Interface (6)
    """
    Display the books in the user's wishlist.
    """
    # Simulate fetching user's wishlist from the database
    cursor.execute("SELECT book.book_id, book.book_name FROM wishlist JOIN book ON wishlist.book_id = book.book_id WHERE wishlist.user_id = %s", (user_id,))
    wishlist_books = cursor.fetchall()
    for book in wishlist_books:
        print(f"Book ID: {book[0]}, Title: {book[1]}")

def show_book_to_add(cursor, user_id): # User Interface (7)
    """
    Display the books not currently in the user's wishlist.
    """
    # Simulate fetching books not in user's wishlist
    cursor.execute("SELECT book_id, book_name FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)", (user_id,))
    available_books = cursor.fetchall()
    for book in available_books:
        print(f"Book ID: {book[0]}, Title: {book[1]}")

def add_book_to_wishlist(cursor, user_id, book_id): # User Interface (8)
    """
    Add a book to the user's wishlist.
    """
    try:
    # Simulate adding a book to the wishlist
        cursor.execute("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
        db.commit()
        print("Book added to wishlist")
    except mysql.connector.Error as err:
        print("Error adding book to wishlist: ", err)

def main():
    while True:
        show_menu() # User Interface Display the account menu (9) 
        choice = input("\nEnter your choice: ")
        if choice == '1':
            show_books(cursor)
        elif choice == '2':
            show_location(cursor)
        elif choice == '3':
            user_id = input("\nEnter your user ID: ") # Variable to capture the user's entry for user_id
            if validate_user(cursor, user_id):
                show_account_menu()
                account_choice = input("\nEnter your choice: ")
                if account_choice == '1':
                    show_wishlist(cursor, user_id)
                elif account_choice == '2':
                    show_book_to_add(cursor, user_id)
                    book_id = input("\nEnter the book ID to add to your wishlist: ")
                    add_book_to_wishlist(cursor, user_id, book_id) # Include a variable to capture user's entry for book_id
                elif account_choice == '3':
                    continue
            else:
                print("\nInvalid user ID.")
        elif choice == '4':
            print("\nThank you for using WhatABook!")
            break
        else:
            print("\nInvalid option, please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram exited by user")
    except Exception as e:
        print("An error occured: ", e)
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db.is_connected():
            db.close()
        print ('Database connection closed.') # Program Exits
