#Joey Spielman Module 6.3
#Delete document
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

#new student to be added
john = {
    "student_id":"1010",
    "first_name":"John",    
    "last_name":"Doe",
    "enrollments":
    [
        {
            "term":"Summer",
            "gpa":"3.5",
            "start_date":"08/01/2021",
            "end_date":"11/21/2021",
            "courses":
            [
                {
                    "course_id":"310",
                    "description":"Database Development",
                    "instructor":"Soriano",
                    "grade":"B"
                },
                {
                    "course_id":"320",
                    "description":"Programming with Java",
                    "instructor":"Payne",
                    "grade":"A"
                }
            ]
        }
        
    ]
}

#Insert temp student
john_student_id = students.insert_one(john).inserted_id
print("  Inserted student record John Smith into the students collection with document_id " + str(john_student_id))

#get new student
single = db.students.find_one({"student_id":"1010"})

#display new student
print("--- DISPLAYING STUDENT DOCUMENT 1010 ---")
print("  Student ID: " + single["student_id"] + "\n  First Name: " + single["first_name"] + "\n  Last Name: " + single["last_name"] + "\n")

#delete temp student
result = db.students.delete_one( {"student_id":"1010"})

#refresh student list
students = db.students
all_students = db.students.find({})


#call output function
all_student_display(students)

