# class Dog():
#
#     # Class object Attributes
#     species = "mammal"
#     legs = 4
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
#
#
#
# myDog = Dog("IG", "Leela")
#
# print(myDog.breed)
# print(myDog.name)
# print(myDog.species)
# print(myDog.legs)
#
#
# class Circle():
#
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
#     def set_radius(self, new_r):
#         self.radius = new_r
#
# myc = Circle(radius = 3)
# print(myc.radius)
# print(myc.area)
# print(myc.area())
#
# myc.set_radius(100)
# print(myc.area())

# inheritance
class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("WHOOF")

    def eat(self):
        print("Dog Eating")


mydog = Dog()
mydog.whoAmI()
mydog.eat()

# special Methods

mylist = [1,2,3]
print(mylist)           #Prints the list elements

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Specail method __str__ create the string repesentation of your class object
    def __str__(self):
        return("Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages))

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")

b = Book("Python", "Zach", 250)
print(b)
