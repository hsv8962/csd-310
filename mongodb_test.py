from pymongo import MongoClient
url = "mongodb+srv://hsv8962:Makework90$@cluster0.dbcpngp.mongodb.net/"
client = MongoClient(url)
db = client.pytech
print("---PyTech Collection List----")
print(db.list_collection_names())

input("End of program, press any key to exit...")