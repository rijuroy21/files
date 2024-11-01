school=['a','b']
student=['shino']
teacher=['abc']
while(True):           
    uc=int(input('''
                1.add
                2.show
                3.exit
                4.go back
                enter your choice:'''))
    while(True):
        if uc==1:
            print(school,student,teacher)
            us=int(input('''
                        1.add school
                        2.add student
                        3.add teacher
                        enter your choice:'''))
            if us==1:
                n=input("Enter school name:")
                school.append(n)
                print(school)
            elif us==1:
                n=input("Enter student name:")
                student.append(n)
                print(student)
            elif us==1:
                n=input("Enter teacher name:")
                teacher.append(n)
                print(teacher)    