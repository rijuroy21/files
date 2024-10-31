class school:   
    def teachers(self):
        print('teachers')
class classroom(school):
    def notes(self):
        print('notes')
class student(classroom):
    def name(self):
        print('name')
std1=student()
std1.teachers()
std1.notes()
std1.name()