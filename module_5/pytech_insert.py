from pymongo import MongoClient

url = "mongodb+srv://hsv8962:Makework90$@cluster0.dbcpngp.mongodb.net/"

client = MongoClient(url)

db = client.pytech
student = db.students

thorin = {'student_id': '1007', 'first_name': 'Thorin', 'last_name': 'Oakenshield'}
bilbo = {'student_id': '1008', 'first_name': 'Bilbo', 'last_name': 'Baggins'}
frodo ={'student_id': '1009', 'first_name': 'Frodo','last_name': 'Baggins'}

print("--INSERT STATEMENT--")
thorin_student_id = student.insert_one(thorin).inserted_id
print(f'Inserted student record Thorin Oakenshield into the students collection with document id {thorin_student_id}')

bilbo_student_id = student.insert_one(bilbo).inserted_id
print(f'Inserted student record Bilbo Baggins into the students collection with document id {bilbo_student_id}')

frodo_student_id = student.insert_one(frodo).inserted_id
print(f'Inserted student record Frodo Baggins into the students collection with document id {frodo_student_id}')

input("End of program, press anu key to exit...")