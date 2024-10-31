class school:
    def notes():
        print('notes')       
    def teachers():
        print('teachers')
class tution:
    def books():
        print('books')
    def name():
        print('name')
class students(school,tution):
    def id():
        print('id')
std1=students
std1.notes()
std1.teachers()
std1.books()
std1.name()
std1.id()