from student import add,add_course,score,record_attendance,calculate_gpa,attendence_summary,course_average,get_top_oerformers,genetate_report_card
def main():
 while True:
    print("="*50)
    print("student performance tracker")
    print("="*50)
    print(''' 1.add new student 
            2.add new course
            3.record marks
            4.record attendence
            5.cal gpa
            6.generate repork card
            7.view top performer
            8.course wise avg
            9.attendence summry
            10.exit
    ''')

    choice = int(input("enter your choice:"))
    if choice==10:
      print("exiting...")  
      break
    elif choice==1:
     name=input("enter your name:")
     stu_id=input("enter your id:")
     grade=input("enter yourgrade:")
     add(stu_id,name,grade)
    elif choice==2:
     cid=input("course id:")
     cname=input("course name:")
     add_course(cid,cname)
    elif choice==3:
     sid=input("student id:")
     cid=input("course id:")
     score_1=float(input("enter tour marks:"))
     score(sid,cid,score_1)
    elif choice==4:
     sid = input("Student ID: ")
     cid = input("Course ID: ")
     present = int(input("Present? (1 for Yes, 0 for No): "))
     record_attendance(sid, cid, present)

    elif choice==5:
            sid = input("Student ID: ")
            print("GPA:", calculate_gpa(sid))
    elif choice==6:
       sid = input("Student ID: ")
       genetate_report_card(sid)
    elif choice==7:
     grade=int(input("grade:"))
     count=int(input("how many top students you need:"))
     get_top_oerformers(grade,count)

    elif choice==8:
     cid=input("course id:")
     course_average(cid)
    elif choice==9:
     sid=input("enter sid:")
     print("attendence:",attendence_summary(sid),"%")

if __name__ == "__main__":
    main()