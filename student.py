students = {
    "S101": {"name": "Riya Mehta", "grade": 9},
    "S102": {"name": "Arjun Rao", "grade": 9},
    "S103": {"name": "Sneha Sharma", "grade": 10}
}
courses ={
    "C101": {"course_name": "Math", },
    "C102": {"course_name": "English", },
    "C103": {"course_name": "Science", }
}
marks_data = {
    "S101": {"C101": 95, "C102": 91, "C103": 88},
    "S102": {"C101": 80, "C102": 85, "C103": 78},
    "S103": {"C101": 89, "C102": 92, "C103": 84}
}
attendence=attendance_data = {
    "S101": {
        "C101": [1, 1, 1, 0, 1],
        "C102": [1, 1, 1, 1, 1],
        "C103": [1, 0, 1, 1, 1]
    },
    "S102": {
        "C101": [1, 0, 1, 1, 0],
        "C102": [1, 1, 0, 1, 1],
        "C103": [1, 1, 1, 0, 1]
    },
    "S103": {
        "C101": [1, 1, 1, 1, 1],
        "C102": [1, 1, 1, 1, 0],
        "C103": [1, 1, 0, 1, 1]
    }
}
def add(student_id,name,grade):
    if student_id in students:
        print("already exists")
        return
    students[student_id]={"name":name,"grade":grade}
    print("added sucessfully")
def add_course(cid,cname):
    if cid in courses:
        print("course already exists")
        return
    courses[cid]={"cname":cname}
    print("added sucesfully")
def score(sid, cid, score_1):
    if sid not in students:
        print("Invalid student ID")
        return
    if cid not in courses:
        print("Invalid course ID")
        return
    if sid not in marks_data:
        marks_data[sid] = {}
    marks_data[sid][cid] = score_1
    print("Marks recorded successfully")
def record_attendance(sid, cid, present):
    if sid not in students:
        print("Invalid student ID!")
        return
    if cid not in courses:
        print("Invalid course ID!")
        return
    attendance_data[sid][cid]={"attendence":present}
    print("Attendance recorded successfully!")

def calculate_gpa(student_id):
    if student_id not in marks_data:
        print("No marks available")
        return 0
    total = 0
    count = 0
    for marks in marks_data[student_id].values():
        total = total + marks
        count = count + 1
    if count == 0:
        return 0
    average = total / count
    gpa = average / 10
    return gpa
def attendence_summary(student_id):
    if student_id not in attendance_data:
        print("No attendance found")
        return
    total = 0
    present = 0
    for course in attendance_data[student_id]:
        for status in attendance_data[student_id][course]:
            total += 1
            if status == 1:
                present += 1
    if total == 0:
        percentage = 0
    else:
        percentage = (present / total) * 100
    print("Total Classes:", total)
    print("Total Present:", present)
    return percentage
def genetate_report_card(student_id):
     if student_id  not in students:
         print("invalid id")
         return
     gpa=calculate_gpa(student_id)
     print("======report card========")
     print(f"name of student is{students[student_id]["name"]}({student_id})")
     print(f"grade of student is:{students[student_id]["grade"]}")
     print(f"gpa:{gpa}")
     print(f"attendence:{attendence_summary(student_id)}%")
     print("subjects and marks")
     if student_id in marks_data:
         for course_id, marks in marks_data[student_id].items():
             print(course_id,":",marks)
     else:         
          print("no marks recorded")
def course_average(course_id):
    total = 0
    count = 0
    for student_id in marks_data:
        if course_id in marks_data[student_id]:
            total += marks_data[student_id][course_id]
            count += 1
    if count == 0:
        print("No marks available!")
        return
    print(f"Course Average:{total/count}")
def get_top_oerformers(grade,count):
    selected=[]
    for student_id in students:
        if students[student_id]["grade"]==grade:
            gpa=calculate_gpa(student_id)
            selected.append((student_id,gpa))
    if len(selected)==0:
        print("no students")
        return
    for i in range(count):
        highest_gpa=0
        top_student=None
        for data in selected:
            if data[1]>highest_gpa:
                highest_gpa=data[1]
                top_student=data
        if top_student is not None:
          print("student Id:",top_student[0],"gpa:",top_student[1])
          selected.remove(top_student)