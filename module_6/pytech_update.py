from pymongo import MongoClient

# MongoDB client database URL 
url = "mongodb+srv://hsv8962:Makework90$@cluster0.dbcpngp.mongodb.net/"

# Establish a connection to the client database
client = MongoClient(url)

# Connect to the pytech database and the students collection
db = client.pytech
students= db.students

# Display all student documents before the update
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find({}):
    print(f"Student ID: {student['student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")

# Update student 1007's last name
print("-- UPDATING STUDENT DOCUMENT FROM Thorin Oakenshield TO King Thorin --")
result = students.update_one(
    {"student_id": "1007"},
    {"$set": {"last_name": "King Thorin"}}
)
print(f"Number of documents updated: {result.modified_count}\n")

# Display the updated student document
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
thorin_updated = students.find_one({"student_id": "1007"})
print(f"Student ID: {thorin_updated['student_id']}")
print(f"First Name: {thorin_updated['first_name']}")
print(f"Last Name: {thorin_updated['last_name']}\n")

# Exit the program
input("End of program, press any key to continue...")
