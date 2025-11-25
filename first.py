#-----------------  OOP in Python -----------------

# class Student:
#     name = ""
#     age = 0
#     Class = ""
#     def info(self):
#         print(f'Hello {self.name} you are {self.age} year ols anf you study in{self.Class}')
        
#     def __init__(self,name,age,Class):
#         self.name = name
#         self.age = age
#         self.Class = Class
    
# ashish = Student("Ahishs",20,"MCA")
# ashish.info()




# ---------------- Single Level Inheritance in Python -----------------

# class Animal:
#     species = ""
#     color = ""
#     legs = 0

#     def info(self):
#         print(f'This is a {self.color} {self.species} with {self.legs} legs.')

#     def __init__(self,species,color,legs):
#         self.species = species
#         self.color = color
#         self.legs = legs
        
# class Dog(Animal):
#     def bark(self):
#         print("Woof Woof!")
        
        
# husky = Dog("Dog","White",4)
# print("Printing info of husky dog:")
# husky.info()

# print("Husky barking sound:")
# husky.bark()

# graphical representation of inheritance

#       ----------
#       | Animal |
#       ----------
#          |
#        -------
#        | Dog |
#        -------



# ---------------- Multi Level Inheritance in Python -----------------
# class Person:
#     name = ""
#     age = 0
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def person(self):
#         print("I am a Person")
#     def info(self):
#         print(f'Name: {self.name}, Age: {self.age}')
        
# class Employee(Person):
#     employee_id = 0
#     def employee(self):
#         print("I am an Employee")
#     def __init__(self,name,age,employee_id):
#         super().__init__(name,age)
#         self.employee_id = employee_id
        
# class Manager(Employee):
#     department = ""
    
#     def __init__(self,name,age,employee_id,department):
#         super().__init__(name,age,employee_id)
#         self.department = department
    
#     def position(self):
#         print("I am a Manager")
        
#     def manager_info(self):
#         self.info()
#         print(f'Employee ID: {self.employee_id}, Department: {self.department}')
        
# ashish = Manager("Ashish",20,101,"IT")

# ashish.person()

# ashish.employee()

# ashish.position()

# ashish.manager_info()

# ghraphical representation of inheritance


#       -----------
#       | Person  |
#       -----------
#           |
#        -----------
#        | Employee |
#        -----------
#            |
#        -----------
#        | Manager  |
#        -----------


# ---------------- Multiple Inheritance in Python -----------------
# class Father:
#     def skills(self):
#         print("Gardening, Programming")
#     def father_info(self):
#         print("I am Father")
        
# class Mother:
#     def skills(self):
#         print("Cooking, Art")
#     def mother_info(self):
#         print("I am Mother")
        
# class Child(Father,Mother):
#     def child_info(self):
#         print("I am Child")
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print("Sports, Music")
        
        
# ashish = Child()
# ashish.father_info()
# ashish.mother_info()
# ashish.child_info()
# ashish.skills()


# graphical representation of inheritance

#        -----------       -----------
#        | Father  |       | Mother  |
#        -----------       -----------
#            |                |
#            |                |
#            --------|---------
#                    |
#                 ---------
#                 | Child |
#                 ---------
#       

# ---------------- Hierarchical Inheritance in Python -----------------

# class Company:
#     name = ""
#     location = ""
#     established_year = 0
#     def __init__(self,name,location,established_year):
#         self.name = name
#         self.location = location
#         self.established_year = established_year
        
#     def company_info(self):
#         print(f'Company Name: {self.name}, Location: {self.location}, Established Year: {self.established_year}')
        
# class HP(Company):
#     products = []
#     def hp_info(self):
#         print("This is HP Company")
        
#     def __init__(self,name,location,established_year,products):
#         super().__init__(name,location,established_year)
#         self.products = products
#     def describe_products(self):
#         print(f'HP Products: {", ".join(self.products)}')
# class Dell(Company):
#     products = []
#     def dell_info(self):
#         print("This is Dell Company")
        
#     def __init__(self,name,location,established_year,products):
#         super().__init__(name,location,established_year)
#         self.products = products
        
#     def describe_products(self):
#         print(f'Dell Products: {", ".join(self.products)}')
        
        
        
# hp = HP("HP","USA",1939,["Laptops","Printers"])
# dell = Dell("Dell","USA",1984,["Laptops","Desktops"])

# hp.company_info()
# hp.hp_info()
# hp.describe_products()

# dell.company_info()
# dell.dell_info()
# dell.describe_products()

# graphical representation of inheritance
#        -----------
#        | Company |
#        -----------
#          /     \
#         /       \
#       -------  -------
#       | HP  |  | Dell |
#       -------  -------

#  ---------------- Antother exaple -----------------
class Grandfather:
    skills = ["Fishing", "Gardening"]

    def __init__(self, name, place_of_birth, **kwargs):
        self.name = name
        self.place_of_birth = place_of_birth

    def info(self):
        print(f'Grandfather Name: {self.name}, Place of Birth: {self.place_of_birth}')
        print(f'Skills: {", ".join(self.skills)}')


class Father(Grandfather):
    skills = ["Programming", "Cooking"]

    def __init__(self, father_age, **kwargs):
        super().__init__(**kwargs)
        self.father_age = father_age

    def info(self):
        super().info()
        print(f'Father Age: {self.father_age}')
        print(f'Skills: {", ".join(self.skills)}')


class Mother(Grandfather):
    skills = ["Art", "Crafting"]

    def __init__(self, mother_age, **kwargs):
        super().__init__(**kwargs)
        self.mother_age = mother_age

    def info(self):
        super().info()
        print(f'Mother Age: {self.mother_age}')
        print(f'Skills: {", ".join(self.skills)}')


class Child(Father, Mother):
    skills = ["Sports", "Dancing"]

    def __init__(self, name, place_of_birth, father_age, mother_age):
        super().__init__(
            name=name,
            place_of_birth=place_of_birth,
            father_age=father_age,
            mother_age=mother_age
        )

    def child_info(self):
        print("I am Child")

    def info(self):
        super().info()
        print(f'Child Skills: {", ".join(self.skills)}')


ashish = Child("Robert", "New York", 50, 48)
ashish.child_info()
ashish.info()

# graphical representation of inheritance
#        --------------
#        | Grandfather |
#        --------------
#          /        \
#         /          \
#       -------    -------
#      | Father |  | Mother |
#       -------    -------
#          \        /
#           \      /
#            ---------
#            | Child |
#           ---------


# method Overloading

class Method:
    def add(name = None):
        if name == None:
            print("Hello")
        else:
            print(f'Hello {name}')
            

m1 = Method()
# m1.add()
# m1.add("Ashish")


# operator Overloading
class Oprat:
    def __init__(self,a):
        self.a = a
        
    def __add__(self,other):
        return self.a + other.a
op1 = Oprat(5)
op2 = Oprat(10)

print(op1 + op2)  # Output: 15