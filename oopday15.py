class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name is {self.name}')
        print(f'Age is {self.age}')
st1=Student(name='Arun',age=40)
st1.display()
st2=Student('Brun',age=50)
st2.display()
st3=Student('Hari',56)
st3.display()




