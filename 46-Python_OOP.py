# object = a "bundle" of related attributes ( variables ) and methods ( functions )
#             Ex. phone, cup, Book
#             You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object


#for good practice put classes in another file then import
# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

from car import Car

car1 = Car("SpaceStar", 2000, "white", False)
car2 = Car("TransAm Firebird", 1979, "white/blue", True)
car3 = Car("Miata", 1980, "brown", True)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)


# methods 
# in fiel car


car1.drive()
car2.stop()