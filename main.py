import json

def show_menu ():
    print ("press 1 if you want to add students")
    print ("press 2 if you want to get details of all students")
    print ("press 3 if you want to update the student's information")
    print ("press 4 if you want to delete the student's information")
    print ("press 5 if you want to exit")

def add_student_detail ():
    try:
        with open ('data.json', 'r') as json_file:
            students = json.load (json_file)
    except:
        students = []
    
    name = str (input ("enter the student name "))
    student_id = int (input (" enter the student id "))
    age = int ( input ("enter the age of the student "))
    course = str (input ("enter the enrolled course of the student "))
    marks = int (input ("enter the obtain marks of the student "))
    
    student  = {"s_name":name, "s_id":student_id, "s_age": age, "s_course":course, "s_marks":marks }
    students.append(student)
    
    with open ('data.json', 'w') as json_file:
        json.dump (students, json_file, indent= 4)
    
     
def show_student_detail ():
    try:
        with open ('data.json', 'r') as json_file:
            students = json.load(json_file)
    except:
        print ("no data")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<8} {'Name':<20} {'Age':<6} {'Course':<20} {'Marks':<6}")
    print("="*70)
    
    for s in students:
        print(f"{s['s_id']:<8} {s['s_name']:<20} {s['s_age']:<6} {s['s_course']:<20} {s['s_marks']:<6}")
    
    
def update_student_detail ():
    try:
        with open ('data.json', 'r') as json_file:
            students = json.load(json_file)
    except:
        print ("no data")
        return
    
    studentt_id= int (input("enter the id of the student you want to update"))
    found = False
    print (students)

    for s in students:
        print (s)
        if s["s_id"] == studentt_id:
            s["s_name"] = input ("enter the updated name of student: ")
            s["s_age"] = int (input ("enter the new age: "))
            s["s_course"] = input("Enter new course: ")
            s["s_marks"] = int(input("Enter new marks: "))
            found = True
            break

    if found:
        with open('data.json', 'w') as json_file:
            json.dump(students, json_file, indent=4)
        print("Student updated successfully!")
    else:
        print("Student not found!")
    

def delete_student_detail ():
    try:
        with open ('data.json', 'r') as json_file:
            students = json.load(json_file)
    except:
        print ("no data")
        return
    
    student_id= int (input("enter the id of the student you want to delete"))
    for s in students:
        if s["s_id"]== student_id:
            students.remove(s)
    

    with open ('data.json', 'w') as json_file:
        json.dump (students, json_file, indent= 4)

        print("Student deleted successfully!")
        return

    print("Student not found!")
    

def main_function ():
    while True:
        show_menu ()
        press_no = int (input ("enter the number "))
    
        match press_no:
            case 1:
                add_student_detail ()
            case 2:
                show_student_detail ()
            case 3:
                update_student_detail ()
            case 4:
                delete_student_detail ()
            case 5:
                return 
            

main_function ()