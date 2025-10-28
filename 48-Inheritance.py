# Inheritance = Allows a class to inherit attributes and methods from another class
#                 Helps with code reusability and extensibility
#                     class Child(Parente)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# By listing the parent class, it inherits the class atributes and methods

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass

dog = Dog("jácomias")
cat = Cat("miau")
mouse = ("rata")

print (dog.name)
cat.eat()