# class
#   Tell Python to make a new type of thing.
# object
#   Two meanings: the most basic type of thing, and any instance of some thing.
# instance
#   What you get when you tell Python to create a class.
# def
#   How you define a function inside a class.
# self
#   Inside the functions in a class, self is a variable for the instance/object being accessed.
# inheritance
#   The concept that one class can inherit traits from another class, much like you and your parents.
# composition
#   The concept that a class can be composed of other classes as parts, much like how a car has wheels.
# attribute
#   A property classes have that are from composition and are usually variables.
# is-a
#   A phrase to say that something inherits from another, as in a "salmon" is-a "fish."
# has-a
#   A phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth."


class Animal(object):
    pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
