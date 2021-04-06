#Joey Spielman Module 5.3 04|06|21
#Insert documents into the PyTech collection

from pymongo import MongoClient 

#connection info
url = "mongodb+srv://admin:admin@cluster0.qco89.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

#students to be added to collection
scott = {
    "student_id":"1007",
    "first_name":"Scott",    
    "last_name":"Pilgrim",
    "enrollments":
    [
        {
            "term":"Summer",
            "gpa":"4.0",
            "start_date":"08/01/2021",
            "end_date":"11/21/2021",
            "courses":
            [
                {
                    "course_id":"310",
                    "description":"Database Development",
                    "instructor":"Soriano",
                    "grade":"A"
                },
                {
                    "course_id":"320",
                    "description":"Programming with Java",
                    "instructor":"Payne",
                    "grade":"A"
                }
            ]
        },
        {
            "term":"Winter",
            "gpa":"4.0",
            "start_date":"01/01/2021",
            "end_date":"03/21/2021",
            "courses":
            [
                {
                    "course_id":"380",
                    "description":"DevOps",
                    "instructor":"Soriano",
                    "grade":"A"
                },
                {
                    "course_id":"430",
                    "description":"Server Side Development",
                    "instructor":"Payne",
                    "grade":"A"
                }
            ]
        }
    ]
}

ramona = {
    "student_id":"1008",
    "first_name":"Ramona",    
    "last_name":"Flowers",
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

stephen = {
    "student_id":"1009",
    "first_name":"Stephen",    
    "last_name":"Stills",
    "enrollments":
    [
        {
            "term":"Summer",
            "gpa":"4.0",
            "start_date":"08/01/2021",
            "end_date":"11/21/2021",
            "courses":
            [
                {
                    "course_id":"310",
                    "description":"Database Development",
                    "instructor":"Soriano",
                    "grade":"A"
                }
            ]
        },
        {
            "term":"Winter",
            "gpa":"3.0",
            "start_date":"01/01/2021",
            "end_date":"03/21/2021",
            "courses":
            [                
                {
                    "course_id":"430",
                    "description":"Server Side Development",
                    "instructor":"Payne",
                    "grade":"B"
                }
            ]
        }
    ]
}

#get inserted_ids for output info
students = db.students

scott_student_id = students.insert_one(scott).inserted_id
ramona_student_id = students.insert_one(ramona).inserted_id
stephen_student_id = students.insert_one(stephen).inserted_id

#output 
print("--- Insert Statements ---")
print("  Inserted student record Scott Pilgrim into the students collection with document_id " + str(scott_student_id))
print("  Inserted student record Ramona Flowers into the students collection with document_id " + str(ramona_student_id))
print("  Inserted student record Stephen Stills into the students collection with document_id " + str(stephen_student_id))
input("\n  End of program, press any key to exit... ")