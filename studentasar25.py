ClassStudent:
    def__init__(self,name,phone):
        self.name= name
        self.phone= phone
        

    def display(self):
        print(f"student name : {self.name}\tstudent phone : {self.phone}")

t1= Student(name="ram",phone=30)
t1.display()

t2= Student(name="Hari",age=410)
t2.display()