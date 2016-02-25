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

# A class definition can be compared to the recipe to bake a cake. A recipe is needed to bake a cake.
# The main difference between a recipe (class) and a cake (an instance or an object of this class) is obvious.
# A cake can be eaten when it is baked, but you can't eat a recipe, unless you like the taste of printed paper.
# Like baking a cake, an OOP program constructs objects according to the class definitions of the program program.
# A class contains variables and methods. If you bake a cake you need ingredients and instructions to bake the cake.
# Accordingly a class needs variables and methods.
# There are class variables, which have the same value in all methods and there are instance variables,
# which have normally different values for different objects. A class also has to define all the necessary methods,
# which are needed to access the data.


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
