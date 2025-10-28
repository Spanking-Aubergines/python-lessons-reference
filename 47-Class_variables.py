# class variables =   shared among all instances of a class
#                     defined outside the constructor
#                     allow you to share data among all objects created from that class

class Student:

    # class variables here
    class_year = 2020
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1




student1 = Student("Spiro", 30)
student2 = Student("Mario", 50)
student3 = Student("Luigi", 27)

print(student1.name)
print(student1.age)
print(student1.class_year)

# for readability call var from class and not constructor/object

print(Student.class_year)
print(Student.num_students)

print(f"The class of {Student.class_year} has {Student.num_students} students")
print(student1.name, student2.name, student3.name)