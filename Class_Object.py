# class are blue print EX: house blue print
# object: by using the class(blue print) we will create multiple objects(houses)

class human:

    def get_name(self):
        print("Enter your name")
        self.name=input()

    def get_age(self):
        print("Enter your age")
        self.age=input()
    def put_name(self):
        print("your name is",self.name)
    def put_age(self):
        print("your age is", self.age)

person1 = human()
person1.get_name()
person1.get_age()

person1.put_name(),person1.put_age()

