#oops:object oriented programming : is a programming paradigm based on the concept of “objects,” which bundle data (attributes) and behavior (methods) to create modular, reusable, and maintainable software. 
#Procedures = functions/methods jo specific kaam karte hain.
#Modularity = bade program ko chhote-chhote modules (parts) me divide karna taaki manage karna aasan ho.
#Reusability = ek baar code likho aur use kai jagah dobara use kar sako.
#classes = blueprints/templates for creating objects. They define the attributes and methods that the objects will have.
#objects = instances of classes. They represent specific entities with their own unique data and behavior.
class Student:#showing the blueprint of student class
    subject = "python"
    college = "chaitanya bharthi institute of technology"
    year = 2027
a=10
stu1=Student()#creating an instance of the Student class
stu2=Student()#creating another instance of the Student class
print(stu2.college)
print(stu1.subject)
print(stu2.year)
print(stu1.college)
print(type(stu1))
#constructor = special method that is automatically called when an object is created. It is used to initialize the attributes of the object.
def __init__(self):
    print("this is the constructor of the class")
__init__(stu1)
__init__(stu2)
class Teacher:
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    def display(self):
        print("name of the teacher is :", self.name)
        print("subject of the teacher is :", self.subject)
    def get_name(self):
        return self.name
stu3=Teacher("syed mohammed","dsa")
stu3.display()
print(stu3.get_name())
#types of constructors :
#1. Default Constructor : A constructor without any parameters.
#2. Parameterized Constructor : A constructor with parameters.
#Attributes = variables that hold data associated with an object. They define the state or characteristics of the object.
print(stu3.name)# is the object of the class Teacher and name is the attribute of the class Teacher
print(stu3.subject) # class attributes 

#Instance Methods
class Laptops:
    storage_type="ssd"
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    def get_info(self):#instance method because it has the self parameter which refers to the instance of the class
        print("the ram is", self.ram, "the storage is", self.storage)
l1=Laptops("16gb","512ssd")
l2=Laptops("8gb","1tb")
l1.get_info()
l2.get_info()
#class methods = methods that are bound to the class and not the instance of the class. They can be called on the class itself, rather than on an instance of the class. They are defined using the @classmethod decorator and take cls as their first parameter, which refers to the class itself.
class Laptop:
    storage_type="ssd"
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    @classmethod
    def get_storage_type(cls):
        return cls.storage_type
print(Laptop.get_storage_type())#class method ko class ke naam se call karte hain
#static methods = methods that are bound to the class and not the instance of the class. They can be called on the class itself, rather than on an instance of the class. They are defined using the @staticmethod decorator and do not take self or cls as their first parameter.
class Laptop:
    storage_type="ssd"
    def __init__(self,ram,storage):
        self.ram=ram
        self.storage=storage
    @staticmethod#yai bina instance ke class ke naam se call karte hain
    def get_storage_type():
        return Laptop.storage_type
    def calc_price(self,price):
        final_price=price+1000
        return final_price
l1=Laptop("16gb","512ssd")
print(l1.calc_price(5000))
print(Laptop.get_storage_type())#static method ko class ke naam se call karte hain

#4 pillers of the oops:
#1. Encapsulation
#2. Inheritance
#3. Polymorphism
#4. Abstraction

#Encapsulation = wrapping data and functions into single unit (class) and restricting access to some of the object's components. It is a way to hide the internal state of an object and only expose a controlled interface to the outside world. This is typically done by making attributes private (using double underscores) and providing public getter and setter methods to access and modify them.
class BankAccount:
    def __init__(self,acc_no,balance,ph_no):
        self.acc_no=acc_no#public attributes
        self.__balance=balance#private   attribute consist of double underscore
        self._phone_number=ph_no#protected attribute consist of single underscore
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance=balance
acc1=BankAccount("1234567890",1000,"9876543210")
print(acc1._phone_number) #protected attribute can be accessed outside the class but it is not recommended
#private attribures consists of getter and setter methods to access and modify them
acc1.set_balance(3000)
print(acc1.get_balance())
#Inheritance = mechanism that allows a class to inherit attributes and methods from another class. The class that inherits is called the child class or subclass, and the class being inherited from is called the parent class or superclass. Inheritance promotes code reusability and establishes a hierarchical relationship between classes.
class Employee:
    start_time="9:00am"
    end_time="5:00pm"
    def change_time(self,new_end_time):
        self.end_time=new_end_time
class Developer(Employee):
    def __init__(self,name,language):
        self.name=name
        self.language=language
dev1=Developer("syed mohammed","python")
print(dev1.start_time,"the ending time is ",dev1.end_time)
#types of inheritance :
#1. Single Inheritance : A child class inherits from a single parent class.
#2. Multiple Inheritance : A child class inherits from multiple parent classes.
#3. Multilevel Inheritance : A child class inherits from a parent class, which in turn inherits from another parent class.
#4. Hierarchical Inheritance : Multiple child classes inherit from a single parent class.
#5. Hybrid Inheritance : A combination of two or more types of inheritance.
#show their examples in the code below
# 1. Single: one child inherits from one parent
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

Dog().eat()


# 2. Multiple: one child inherits from multiple parents
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly()
duck.swim()


# 3. Multilevel: inheritance forms a chain
class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    pass

class Puppy(Mammal):
    pass

Puppy().eat()


# 4. Hierarchical: multiple children inherit from one parent
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Dog().eat()
Cat().eat()

# 5. Hybrid: a combination of inheritance forms
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
print([cls.__name__ for cls in D.mro()])
#Abstraction =hiding the internal details and showing only the essential features of an object. It allows the user to focus on what an object does instead of how it does it. In Python, abstraction can be achieved using abstract classes and abstract methods, which are defined in the abc module.jiska inheritance sirf child class me hota hai aur parent class me nahi hota hai. Abstract classes cannot be instantiated, and abstract methods must be implemented by the subclasses.
from abc import ABC, abstractmethod
from turtle import shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Lion(Shape):
    def area(self):
        print("Calculating area of the lion")
class rectangle(Shape):
    def area(self):
        print("a*a")
lion=Lion()
lion.area()
rect=rectangle()
rect.area()

#polymorphism = the ability of different objects to respond to the same method in different ways. It allows for a single interface to be used with different underlying forms (data types). In Python, polymorphism can be achieved through method overriding and operator overloading.
#Method Overriding: When a subclass provides a specific implementation of a method that is already defined in its superclass, it is called method overriding. The subclass method overrides the superclass method, allowing for different behavior based on the object type.
class Employee:
    def work(self):
        print("employee is working")#work is same method but the implementation is different in the child class
class Teacher(Employee):
    def work(self):
        print("teacher is teaching")
t1=Teacher()
t2=Employee()
t1.work()
t2.work()
#overloading=Python doesn’t support traditional signature-based overloading: if you define the same method name more than once, the later definition replaces the earlier one. A common approach is @singledispatchmethod, which selects an implementation based on an argument’s type:
from functools import singledispatchmethod

class Display:
    @singledispatchmethod
    def show(self, value):
        return f"Other: {value}"

    @show.register
    def _(self, value: int):
        return f"Integer: {value}"

    @show.register
    def _(self, value: str):
        return f"Text: {value}"

display = Display()
print(display.show(7))       # Integer: 7
print(display.show("hello")) # Text: hello

#Method overriding
#Definition: A child class provides its own implementation of a method inherited from its parent. The child’s implementation is used when called on a child object.
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):  # Overrides Animal.sound
        return "Bark"

print(Animal().sound())  # Some sound
print(Dog().sound())     # Bark

class Dog(Animal):
    def sound(self):
        return super().sound() + " — Bark!"

print(Dog().sound())  # Some sound — Bark!