# Abstraction & Encapsulation in Python
class Student:
    def __init__(self , name,marks):
         self.name = name
         self.marks = marks
         print("Student object created")

    def Welcome(self):
        print("Welcome to the class",self.name)

    def Homework(self,hw):
        print("Homework assigned to",self.name,"is",hw)

    def get_avg(self):
        return sum(self.marks)/len(self.marks)

S1 = Student("Prasad Pohnerkar", [99,97,85])
print(S1.name,S1.marks)
print("Average marks:", S1.get_avg())   
S1.Welcome()
S1.Homework("Mathematics")

# Classes and Objects in Python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

A1 = Account("Prasad Pohnerkar", 1000)
print(A1.name, A1.balance)
A1.deposit(500)
A1.withdraw(200)    
print("Final balance:", A1.balance)

# Inheritance in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")
    
    @staticmethod
    def Start(model):
        print(f"Car {model} started")

    @staticmethod
    def Stop(model):
        print(f"Car {model} stopped")

C1 = Car("Toyota", "Camry", 2020)
C1.display_info()

class ToyataCar(Car):
    def __init__(self, model, year):
        super().__init__("Toyota", model, year)

class HondaCar(Car):
    def __init__(self, model, year):
        super().__init__("Honda", model, year)

class FuelType(ToyataCar):
    def __init__(self, model , fuel):
        super().__init__(model, 2021)
        self.fuel = fuel
        print(f"PetrolCar: {model} uses {fuel}")
      
        
T1 = ToyataCar("Corolla", 2021)
T2 = HondaCar("Civic", 2022)
T3 = FuelType("Corolla", "Petrol")
T4 = FuelType("Civic", "Diesel")
T1.display_info()
T1.Start("Corolla")
T1.Stop("Corolla")   
T2.display_info()
T2.Start("Civic")
T2.Stop("Civic")   

# Use of class decorators in Python

class Person:
    name = "John Doe"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def ChangeName(cls, new_name):
        cls.name = new_name
        print(f"Person name changed to: {cls.name}")

P1 = Person("Alice", 30)
print(P1.name, P1.age)
Person.ChangeName("Bob")
print(Person.name)

# Implement @Property decorator in Python
class Circle:   
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

C1 = Circle(5)
print("Radius:", C1.radius) 
C1.radius = 10
print("Updated Radius:", C1.radius)

class Student:
    def __init__(self, phy, chem, math):
        self._phy = phy
        self._chem = chem
        self._math = math

    @property 
    def Percentage(self):
        return str((self._phy + self._chem + self._math) / 3) +"%"
    
S1 = Student(85, 90, 95)
print("Percentage:", S1.Percentage)
S1._phy = 80
print("Updated Percentage:", S1.Percentage)

# Circle with radius, calculate area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def area(self):
        return 3.14 * self._radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self._radius

C1 = Circle(5)
print("Area:", C1.area())
print("Perimeter:", C1.perimeter())

# Write and Employee class with role ,dept, salary and Engineer class
# will inherit Employee class and have method to calculate bonus based on salary.
class Employee:
    def __init__(self, name, role, dept, salary):
        self.name = name
        self.role = role
        self.dept = dept
        self.salary = salary    

class Engineer(Employee):
    def __init__(self, name, dept, salary):
        super().__init__(name, "Engineer", dept, salary)

    def calculate_bonus(self):
        return self.salary * 0.1            
E1 = Engineer("Alice", "Software", 80000)
print("Name:", E1.name) 
print("Role:", E1.role)
print("Department:", E1.dept)   
print("Salary:", E1.salary)
print("Bonus:", E1.calculate_bonus())

# Practive Dunder Function
class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    # Dunder function to compare two orders based on amount
    # This will allow us to use the > operator to compare two Order objects
    # Acts as example of operator overloading in Pythonssss
    def __gt__(self,Ord2):
        return self.amount > Ord2.amount
    
O1 = Order(1, 170)
O2 = Order(2, 150)
print("Is O1 greater than O2?", O1 > O2)
       
