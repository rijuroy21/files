class school:   
    def name(self):
        print('name')
class teacher(school):
    def notes(self):
        print('notes')
class student(school):
    def id(self):
        print('id')
std1=student()
std2=teacher()
std1.id()
std2.notes()
std1.name()