'''Simple Python class'''


class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_person_data(self):
        args = {'name': self.name, 'age': self.age}
        print('Your name is {name}, your age is {age}'.format(**args))


person1 = person('John Junior Dos Santos', 30)
person2 = person('Rhoda Dest', 24)
person1.get_person_data()
person2.get_person_data()
