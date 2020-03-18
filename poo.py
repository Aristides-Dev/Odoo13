class Person():
    name = ""
    age = 10
    color_pleo = ""
    __numero_telef = ""

    def __init__(self, color, name=None, age=None):
        self.name = name
        self.color_pelo = color

persona1 = Person("Negro", "Fransisco", 40)
persona1.__numero_telef = "64910158"

print(persona1.color_pelo, persona1.name, persona1.__numero_telef)


# Herencia

class User(Person):

    def __init__(self, color, name=None):
        super(User, self).__init__(color)
        self.name = name


user1 = User("Rojo", "Juan")
user1.age = 20

print("Hijo ", user1.color_pelo, user1.name, user1.age)