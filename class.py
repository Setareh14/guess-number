class Person:
    def __init__ (self,name,lname):
        self.name = name 
        self.lname = lname
        
    def show_deta(self) :
        print(f':نام{self.name},:نام خانوادگی{self.lname}')
        
        
class Student(Person):
    def __init__ (self,name,lname,age,score):
        super().__init__(name,lname)
        self.age = age
        self.score = score
        
    def show_student(self):
        print(f"نام:{self.name},نمره:{self.score}")
        
s1= Student('Sara','Ahmadi',20,19)
s1.show_student()