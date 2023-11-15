from pymongo import MongoClient

# MongoDB URL
url = "mongodb+srv://admin:admin@cluster0.dbcpngp.mongodb.net/"

# Connection to the MongoDB server
client = MongoClient(url)

# Connect to the pytech database and the students collection
db = client.pytech
students = db.students

# Find all documents in the collection
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students.find():
    print(f"Student ID: {student['student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")

# Find a single document using the find_one() method
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
bilbo = students.find_one({"student_id": "1008"})
print(f"Student ID: {bilbo['student_id']}")
print(f"First Name: {bilbo['first_name']}")
print(f"Last Name: {bilbo['last_name']}")

# End of program prompt
input("End of program, press any key to continue...")
