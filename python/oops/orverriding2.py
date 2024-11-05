class school:
    def __init__(self,sname):
        self.school_name=sname
    def teacher (self):
       print('teacher')
class std(school):
    def __init__(self,sname,splace):
        super().__init__(sname)
        print('std details')
        self.splace=splace
    def teacher(self):
        super().teacher()
        print('teacher2')
std1=std("GHSS CU CAMPUS","Malappuram")
std1.teacher()  
print(std1.school_name)
print(std1.splace)     