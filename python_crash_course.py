# """
# A comprehensive learning resource covering fundamental Python concepts organized into 12 sections.
# Each section demonstrates core programming principles with practical examples.
# SECTIONS:
#     01_VARIABLES_AND_DATA_TYPES: Basic variable declaration and primitive data types (str, int, bool, float)
#     02_LISTS: List creation, indexing, slicing, and list comprehensions with filtering
#     03_TUPLES: Immutable sequences, tuple unpacking, and conversion to mutable types for modification
#     04_SETS: Set operations including intersection, symmetric difference, and set subtraction
#     05_DICTIONARIES: Key-value pair storage, dictionary methods, and nested data structures
#     06_CONDITIONALS_IF_ELIF_ELSE: Conditional branching with if, elif, else statements
#     07_LOOPS_FOR_AND_WHILE: Iteration using for loops and while loops with control flow statements
#     08_FUNCTIONS: Function definition, parameters, and return values
#     09_MODULES: Importing and using external modules (datetime)
#     10_CLASSES_AND_OBJECTS: Object-oriented programming including:
#         - Class and instance properties
#         - Constructor methods (__init__) and special methods (__str__)
#         - Inheritance: Child classes inheriting from parent classes
#         - Polymorphism: Method overriding in subclasses
#         - Encapsulation: Private variables and methods with name mangling (__double_underscore)
#         - Getter and setter methods for controlled access
#     11_STRING_FORMATTING: F-strings with format specifiers (decimal places, comma separators, alignment, case conversion)
#     12_FILE_HANDLING_BASICS: Safe file operations using context managers (with statement) for reading and writing text files
# Key Concepts:
#     - Data structures: variables, lists, tuples, sets, dictionaries
#     - Control flow: conditionals and loops
#     - Functions and code reusability
#     - Object-oriented programming: classes, inheritance, polymorphism, and encapsulation
#     - File I/O with proper resource management
#     - String manipulation and formatting
# Python Beginner Learning Organizer
# Custom section tags are used to separate learning topics.
# """

# # ==========================================================
# # [SECTION: 01_VARIABLES_AND_DATA_TYPES]
# # ==========================================================
# name = "Peter"
# age = 20
# is_student = True
# height = 1.75

# print("Name:", name)
# print("Age:", age)
# print("Student:", is_student)
# print("Height:", height)


# # ==========================================================
# # [SECTION: 02_LISTS]
# # ==========================================================
# names = ["adam", "bridget", "adamu", "kate", "supreme", "brooks", "sky"]
# numbers = [1, 2, 13, 297, 18, 300]

# print("Original names:", names)
# print("First name:", names[0])

# filtered_names = [n for n in names if "a" in n]
# print("Names containing 'a':", filtered_names)

# small_numbers = [f"{n} is less than 27" for n in numbers if n < 27]
# print("Filtered numbers:", small_numbers)


# # ==========================================================
# # [SECTION: 03_TUPLES]
# # ==========================================================
# fruits_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print("Tuple item slice [2:5]:", fruits_tuple[2:5])

# # Tuples are immutable, so convert to list to update.
# temp_list = list(fruits_tuple)
# temp_list[1] = "blackcurrant"
# fruits_tuple = tuple(temp_list)
# print("Updated tuple:", fruits_tuple)


# # ==========================================================
# # [SECTION: 04_SETS]
# # ==========================================================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# intersection_items = set1.intersection(set2)
# symmetric_diff_items = set1.symmetric_difference(set2)
# only_set1_items = set1 - set2

# print("Set intersection:", intersection_items)
# print("Set symmetric difference:", symmetric_diff_items)
# print("Only in set1:", only_set1_items)


# # ==========================================================
# # [SECTION: 05_DICTIONARIES]
# # ==========================================================
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "self_driving": True,
#     "electric": False,
#     "colors": ["red", "white", "blue"],
# }

# print("Car type:", type(car))
# print("Car brand:", car["brand"])
# print("Car keys:", list(car.keys()))

# car["year"] = 1996
# car.update({"is_classic": car["year"] < 1990})
# print("Updated car dictionary:", car)


# # ==========================================================
# # [SECTION: 06_CONDITIONALS_IF_ELIF_ELSE]
# # ==========================================================
# gender = "female"

# if gender == "female":
#     print("Congratulations, you are eligible to attend the event")
# elif gender == "male":
#     print("This is a female only event")
# else:
#     print("Invalid gender")


# # ==========================================================
# # [SECTION: 07_LOOPS_FOR_AND_WHILE]
# # ==========================================================
# print("For loop over names:")
# for item in names:
#     print("-", item)

# print("While loop with continue:")
# i = 0
# while i < 10:
#     i += 1
#     if i == 4 or i == 7:
#         continue
#     print(i)


# # ==========================================================
# # [SECTION: 08_FUNCTIONS]
# # ==========================================================
# def add_two(number):
#     return number + 2


# print("add_two(5):", add_two(5))


# # ==========================================================
# # [SECTION: 09_MODULES]
# # ==========================================================
# import datetime
# from datetime import date

# today1 = datetime.date.today()
# today2 = date.today()

# print("Today's date from datetime:", today1)
# print("Today's date from date:", today2)


# # ==========================================================
# # [SECTION: 10_CLASSES_AND_OBJECTS]
# # ==========================================================
# class Project:
#     def __init__(self, name):
#         self.project_name = name
#         self.detail = ""

# # The __str__ method is a special method that defines how an object is represented as a string. When you print an object or convert it to a string, this method is called to determine the string representation of the object.
#     def __str__(self): 
#         return self.detail

#     def detailer(self, year, capacity, category):
#         self.detail = (
#             f"{self.project_name} was developed in {year}, with capacity {capacity}. "
#             f"It is categorized as {category}."
#         )


# switcher = Project("switch controller")
# switcher.detailer(2026, "1kW", "Embedded system")
# print("Project detail:", switcher.detail)
# print(switcher)

# # ===========================================================================
# # Class Property vs Object/Instnace Property
# # ===========================================================================
# # Modifying class property will affect all instances, while modifying instance property will only affect that specific instance.
# class Person:
#     org_name = "Futlink"  # Class property shared by all instances
#     # constructor method to initialize name and age attributes
#     def __init__ (self, name, age):
#         self.name = name # Instance property unique to each object
#         self.age = age # Instance property unique to each object

#     def greet (self):
#         print(f"Hello, my name is {self.name}")

# p1 = Person("John", 36)
# p1.greet()
# print("Person's name:", p1.name)
# print("Person's age:", p1.age)

# p1.age = 37
# print("Updated person's age:", p1.age)
# print("Organization name (class property):", Person.org_name)

# # ===========================================================================
# # Inheritance
# # ===========================================================================
# # The BoardOfDirectors class inherits from the Person class, allowing it to use the properties and methods of Person while also adding its own unique properties and methods. Note that naming a method in the child class the same as a method in the parent class (like introduce) will override the parent method when called on an instance of the child class.

# class BoardOfDirectors(Person):
#     def __init__ (self, name, age, position):
#         super().__init__(name, age) # Call the constructor of the parent class (Person)
#         self.position = position # Additional property for BoardOfDirectors
#     def introduce(self):
#         print(f"Hello, I am {self.name}, the {self.position} of the {Person.org_name} company.")

# director = BoardOfDirectors("Moses", 45, "CEO")

# # ===========================================================================
# # Polymorphism (multiple forms)
# # ===========================================================================
# # polymorphism allows objects of different classes to be treated as objects of a common superclass. 
# class Employee(Person):
#     def __init__ (self, name, age, department):
#         super().__init__(name, age) # Call the constructor of the parent class (Person)
#         self.department = department # Additional property for Employee
#     def introduce(self):
#         print(f"Hello, I am {self.name}, working in the {self.department} department of {Person.org_name}.")

# employee = Employee("Alice", 30, "Engineering")

# for x in (director, employee):
#     x.introduce() # This will call the introduce method of the respective class (BoardOfDirectors or Employee) due to polymorphism. in other words the introduce method is a polymorphic method that behaves differently based on the type of object (director or employee) that is calling it.

# # ===========================================================================
# # Encapsulation (Private variables and methods) -- conventionally creating private variables and methods using a single underscore (_) (unprotected) or double underscore (__) (protected).
# # ===========================================================================
# class BankAccount:
#     account_manager = "Futlink Bank" # Class property shared by all instances
#     account_type = "Savings" # Class property shared by all instances

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance # Private variable (name mangling)

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Withdrawal amount must be positive and less than or equal to the balance.")
#     #custom getter method to access the private balance variable with authorization check
#     def get_balance(self, owner):
#         if self.owner == owner:
#             return self.__balance
#         else:
#             print("Unauthorized access to balance.")
#             return None
        
#     def set_balance(self, owner, new_balance):
#         if owner == BankAccount.account_manager: # Only allow the account manager to set the balance
#             self.__balance = new_balance
#             print(f"Balance updated to {new_balance}.")
#         else:
#             print("Unauthorized access to set balance.")
        
# account = BankAccount("John", 1000)
# account.deposit(500)
# account.withdraw(200)
# print("Current balance (authorized):", account.get_balance("John"))
# print("Current balance (unauthorized):", account.get_balance("Alice"))
# account.set_balance("Alice", 2000) # Unauthorized attempt to set balance
# account.set_balance("Futlink Bank", 2000) # Authorized attempt to set balance
# print("Current balance (authorized):", account.get_balance("John"))



# # ==========================================================
# # [SECTION: 11_STRING_FORMATTING]
# # ==========================================================
# price = 5900000

# print(f"Price (3 decimal places): {59:.3f}")
# print(f"Price with comma: {price:,}")
# print(f"Price with underscore: {price:_}")
# print(f"Centered number: {price:^20}")

# student_name = "john"
# print(f"Uppercase: {student_name.upper()}")
# print(f"Capitalized: {student_name.capitalize()}")


# # ==========================================================
# # [SECTION: 12_FILE_HANDLING_BASICS]
# # ==========================================================
# # This section demonstrates safe file write and read in beginner form.
# sample_filename = "exampleFile.txt"

# exampleFile = open(sample_filename, "w")

# exampleFile.write("Hello from Python file handling!\n have a nice day!")

# exampleFile.close()

# # # the "with" statement is used to ensure that the file is properly closed after its suite finishes, even if an exception is raised. This is a best practice for file handling in Python to prevent resource leaks and ensure data integrity.
# # with open(sample_filename, "w", encoding="utf-8") as file:
# #     file.write("Hello from Python file handling!\n have a nice day! 🙂")

# with open(sample_filename, "r", encoding="utf-8") as file:
#     content = file.read().strip()

# print("File content:", content)

# # This is a more concise way to read and print each line from the file without storing the entire content in memory at once.
# with open("exampleFile.txt") as f:
#   for x in f:
#     print(x)

# # There are 4 modes for the open method;
# # 1. "r" - Read mode (default): Opens a file for reading. If the file does not exist, it raises a FileNotFoundError.
# # 2. "w" - Write mode: Opens a file for writing. If the file already exists, it truncates the file to zero length (deletes its content). If the file does not exist, it creates a new file.
# # 3. "a" - Append mode: Opens a file for appending. If the file already exists, it allows you to add new content to the end of the file without deleting the existing content. If the file does not exist, it creates a new file.
# # 4. "x" - Exclusive creation mode: Opens a file for exclusive creation. If the file already exists, it raises a FileExistsError. If the file does not exist, it creates a new file.

# # The encoding parameter in the open function specifies the encoding used to read or write the file. Common encodings include "utf-8" (which supports a wide range of characters, including emojis), "ascii" (which supports only basic English characters), and "latin-1" (which supports Western European characters). Specifying the correct encoding is important to ensure that the file is read or written correctly, especially when dealing with non-ASCII characters. Default encoding may vary based on the system and locale settings, so it's often a good practice to explicitly specify the encoding when working with files to avoid potential issues with character representation.


# # ==========================================================
# # [SECTION: 13_EXCEPTION_HANDLING]
# # ==========================================================
# print("Exception handling examples:")

# try:
#     number = 10
#     result = number / 0
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division completed successfully.")
# finally:
#     print("This block runs no matter what.")

# try:
#     with open("missing_file.txt", "r", encoding="utf-8") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file was not found.")


# # ==========================================================
# # [SECTION: 14_LAMBDA_MAP_FILTER_AND_SORT_KEY]
# # ==========================================================
# numbers = [5, 2, 9, 1, 7, 4]
# names = ["adam", "bridget", "adamu", "kate", "supreme", "brooks", "sky"]

# #lambda function is synonymous to javascript arrow function. It only have one expression and does not require a return statement. 
# square = lambda value: value * value 
# print("Lambda square of 6:", square(6))

# # map
# mapped_numbers = list(map(lambda value: value * 2, numbers))
# filtered_numbers = list(filter(lambda value: value > 4, numbers))
# sorted_names = sorted(names, key=lambda value: len(value))

# print("Mapped numbers:", mapped_numbers)
# print("Filtered numbers:", filtered_numbers)
# print("Names sorted by length:", sorted_names)


# # ==========================================================
# # [SECTION: 15_RECURSION_AND_GENERATORS]
# # ==========================================================
# def factorial(value):
#     if value <= 1:
#         return 1
#     return value * factorial(value - 1)


# def count_up_to(limit):
#     current = 1
#     while current <= limit:
#         # yield is used to create a generator, which allows the function to return a value and pause its execution, resuming from the same point when the next value is requested. This is more memory efficient than returning a list of all values at once, especially for large limits.
#         yield current
#         current += 1


# print("Factorial of 5:", factorial(5))
# print("Generator values:")
# for item in count_up_to(5):
#     print(item)

# # yield is a temporary return statement. When the function is called again, it resumes execution right after the yield statement, allowing it to produce a sequence of values over time instead of computing them all at once and returning a list. This is particularly useful for generating large sequences or when the total number of values is not known in advance.

# def yield_example():
#     yield "First value"
#     count = 0
#     while count < 3:
#         yield f"Count is {count}"
#         count += 1

# for x in yield_example():
#     print(x)

#     # ===========================================================================
#     # CLASS PRACTICE
#     # ===========================================================================

# def hangman():
#     x = 2 + 5
#     y = 0
#     y += x
#     z = 0
#     if y > 0:
#         z = 2
#     else:
#         z = 1306
#     return z
# # print(hangman())

# from time import sleep

# def welcome():
#     print("Welcome to on BOARD!")
#     sleep(0.5)
#     print("Hi, Alloy, use this calculator app\n")

# def calc():
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     operation = input("Enter operation (-, *, +): ")

#     ans = None
#     if operation == "+":
#         ans = float(num1) + float(num2)
#     elif operation == "*":
#         ans = float(num1) * float(num2)
#     elif operation == "-":
#         ans = float(num1) - float(num2)
#     else:
#         ans = "invalid operation"
#     print(f"{ans}\n")

# def thankYou():
#     print("Thank you for using our app. Please come again!")

# welcome()
# sleep(0.6)
# calc()
# sleep(1)
# thankYou()

from time import sleep
# x = "\\ "
# y = " "
# z = 20
# i = 0
# for i in range(z):
#     y = y + x
#     sleep(0.5)
#     print(y)



def userDirection():
    print("Welcome")
    direction = input("Enter your direction (< , >): ")
    steps = input("Enter number of steps: ")
    y = "\\ "
    x = "/"
    reverse = int(steps)
    for i in range(int(steps)):
        if direction == ">":
            sleep(0.5)
            print(y)
            y = " " + y
        elif direction == "<":
            a = " " * (reverse - 1)
            sleep(0.5)
            print(a + x)
            reverse = reverse - 1
        else:
            print("Invalid direction. Please enter '<' or '>'.")
            break

userDirection()