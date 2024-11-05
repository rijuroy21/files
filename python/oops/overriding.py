class school:
    def __init__(self):
        print('school')
    def teacher (self):
       print('teacher')
class std(school):
    def __init__(self):
        super().__init__()
        print('std details')
    def teacher (self):
        super().teacher()
        print('teacher2')
std1=std()
std1.teacher()       