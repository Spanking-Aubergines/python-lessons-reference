# multiple inheritance = inherit from more than on parent class
#                         C(A, B)

# multilevel inheritance = inherit from a parent which inherits from anoter parent
#                         C(B(C)


class Animal:

    def __init__ (self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# multiple inheritance
class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

# multiple inheritance
fish.flee()
fish.hunt()

# multilevel( Fish <- (Prey, Predator) <- Animal)
rabbit.sleep()
hawk.eat()

# the constructor can also be inherited
rabit = Rabbit("Fofinho")

rabbit.eat()