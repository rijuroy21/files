class synneffo:
    def __init__(self):
        self.name=input("Enter student name:")
        self.age=input("Enter student age:")
        self.address=input("Enter student address:")
    def python(self):
        print('python',self.name,self.age,self.address)
    def php(self):
        print('php',self.name,self.age,self.address)  
std1=synneffo()
std1.python()   
std2=synneffo()
std2.php()
        
        