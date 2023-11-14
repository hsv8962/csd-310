# Pascual Villar
# CYBR410-305J
# Assignment: Module 6.3 (PyTech: Deleting Documents)
# November 14, 2023

from pymongo import MongoClient

# Mongo Client URL
url = "mongodb+srv://hsv8962:Makework90$@cluster0.dbcpngp.mongodb.net/"

# Connection to the MongoDB database
client = MongoClient(url)

# Connection to pytech database and the students collection
db = client.pytech
students = db.students

# Display all student documents 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students_documents = students.find({})
for doc in students_documents:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

# Insert a new student document
new_student = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}
insert_result = students.insert_one(new_student)
print("-- INSERT STATEMENTS --")
print(f"Inserted student record into the students collection with document id {insert_result.inserted_id}\n")

# Display the new student document
print("-- DISPLAYING STUDENT TEST DOC --")
test_doc = students.find_one({"student_id": "1010"})
print(f"Student ID: {test_doc['student_id']}")
print(f"First Name: {test_doc['first_name']}")
print(f"Last Name: {test_doc['last_name']}\n")

# Delete the new student document
delete_result = students.delete_one({"student_id": "1010"})
print(f"Deleted student record from the students collection with document id {delete_result.deleted_count}\n")

# Display all student documents 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students_documents = students.find({})
for doc in students_documents:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}\n")

# Exit the program
input("End of program, press Enter to continue...")
