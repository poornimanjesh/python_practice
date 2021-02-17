# In a family tree ,traits such as hair colour and poor eyesight are passed from generation to generation.
class fruit():
    def __init__(self):
        print("I'm a fruit")
All_type_of_fruits = fruit()


class citrus(fruit):
    def __init__(self):
        super().__init__()
        print("I'm citrus fruit")
Lemon = citrus()
