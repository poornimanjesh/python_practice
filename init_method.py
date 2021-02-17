# __init__ is a special method in python Classes
# is a constructor method for a class
# __init__ is called when ever an object of the class is constructed


class student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age= age
        self.branch=branch

    def print_student(self):
        print("name", self.name)
        print("age",self.age)
        print("branch",self.branch)

student1 = student("Bob",12,"Arts")
student1.print_student()





