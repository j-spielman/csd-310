#Joey Spielman Module 6.2
#Update existing documents
from pymongo import MongoClient 

#function for displaying all students
def all_student_display(students):
    print("--- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY ---")
    for student in all_students:
        print("  Student ID: " + student["student_id"] + "\n  First Name: " + student["first_name"] + "\n  Last Name: " + student["last_name"] + "\n")

#connection info
url = "mongodb+srv://admin:admin@cluster0.qco89.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

# get the students collection 
students = db.students

#get collection to work with
all_students = db.students.find({})

#call output function
all_student_display(students)

#update student 1007
result = db.students.update_one( {"student_id":"1007"},{"$set": {"last_name":"Smith"}})

#get updated student
single = db.students.find_one({"student_id":"1007"})

#display updated student
print("--- DISPLAYING STUDENT DOCUMENT 1007 ---")
print("  Student ID: " + single["student_id"] + "\n  First Name: " + single["first_name"] + "\n  Last Name: " + single["last_name"] + "\n")

input(" End of program, press any key to continue...")