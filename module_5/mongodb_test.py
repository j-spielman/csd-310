#Joey Spielman 04/06/21 Module 5
#MongoDB connection test
from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.qco89.mongodb.net/pytech"
client = MongoClient(url)

db = client.pytech

print("\n---Pytech Collection List---")
print(db.list_collection_names())
input("\nEnd of program, press any key to exit...")