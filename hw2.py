studentList = []


def addStudent(name, surname):
    studentName = name+" "+surname
    studentList.append(studentName)
    print(studentName + " student successfully added!!")


def addMultipleStudent(students):
    for student in students:
        for name in student:
            studentName = name+" "+student[name]
            studentList.append(studentName)
            print(studentName + " successfully added!!")


def deleteStudent(name, surname):
    studentName = name+" "+surname
    studentList.remove(studentName)
    print(studentName + " successfully deleted!!")



def getStudents():
    print("-"*8+" "+"All student of database"+" "+"-"*8)
    i = 0
    while(len(studentList) > i):
        print(studentList[i])
        i += 1


def getStudentNumber(name, surname):
    studentName = name+" "+surname
    if studentName in studentList:
        print("Student number of " + studentName+" : " +
              str(studentList.index(studentName)))
    else:
        print("Stundet not found")


# Print operations
addStudent("Ali", "Veli")
addMultipleStudent([{"Ayse": "11"}, {"Fatih": "99"}])
getStudents()
getStudentNumber("Ayse", "11")
deleteStudent("Ayse", "Ali")
getStudents()