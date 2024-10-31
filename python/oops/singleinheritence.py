class school:
    def notes():
        print('notes')       
    def teachers():
        print('teachers')
class students(school):
    def house():
        print('house')
std1=students
std1.notes()
std1.teachers()
std1.house()