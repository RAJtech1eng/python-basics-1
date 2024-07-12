
class Teacher:
    def __init__(self,name,age,salary):
        self.name= name
        self.age= age
        self.salary= salary

    def display(self):
        print(f"Teacher name : {self.name}\tteacher age : {self.age}\tteacher salary : {self.salary}")

t1= Teacher(name="ram",age=30,salary=50000)
t1.display()

t2= Teacher(name="Hari",age=41,salary=51000)
t2.display()


