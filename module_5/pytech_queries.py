#Joey Spielman Module 5.3 04|06|21
#find() and findOne() queries

from pymongo import MongoClient 

#connection info
url = "mongodb+srv://admin:admin@cluster0.qco89.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#get collection to work with
students = db.students.find({})

#get single student 
single = db.students.find_one({"student_id":"1007"})

#loop to display all students
print("--- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY ---")
for student in students:
    print("  Student ID: " + student["student_id"] + "\n  First Name: " + student["first_name"] + "\n  Last Name: " + student["last_name"] + "\n")

#display single student
print("--- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY ---")
print("  Student ID: " + single["student_id"] + "\n  First Name: " + single["first_name"] + "\n  Last Name: " + single["last_name"] + "\n")

input(" End of program, press any key to continue...")