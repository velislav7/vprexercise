# EX.1

# list1=[]
# list2=[]

# while True:
#     numbers = int(input("Въведете числа "))
#     if numbers == 0:
#         break
#     if numbers % 3 == 0 and numbers % 2 == 0:
#         list1.append(numbers)
#     if numbers % 7 ==0 and numbers % 2 != 0:
#         list2.append(numbers)

# sum_list1 = sum(list1[2::2])
# print ("Сумата на четните елементи в първата листа е равна на ", sum_list1)

# sortedlist2 = sorted(list2, reverse=True)
# product_list2 = list2[0] * list2[-1]
# print ("Произвведението на най-голямото и най-малкото число е равно на ", product_list2)

# EX.2
# class Product:
#     def __init__(self, manufacturer, product_code, price_per1, amount):
#         self.manufacturer = manufacturer
#         self.product_code = product_code
#         self.price_per1 = price_per1
#         self.amount = amount

# all_products = {
#     "4a": Product("Xiaomi", "4a", 50, 0),
#     "4c": Product("Xiaomi", "4c", 60, 0),
#     "ac1200": Product("TP-Link", "ac1200", 30, 0),
#     "ac1900": Product("TP-Link", "ac1900", 40, 0),
# }

# class ShoppingCart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product, amount):
#         product.amount = amount
#         self.products.append((product, amount))        

# cart = ShoppingCart()

# buy_options = input("Hello! Would you like to buy a new product? YES/NO ").lower()
# if buy_options == "yes":
#     while True:
#         product_code = input(f"Here is our selection.\n Xiaomi 4a \n Xiaomi 4c \n TP-Link ac1200 \n TP-Link ac1900 \nBy writing the product code you are choosing to add it to your basket. ").lower()
#         if product_code in all_products:
#             quantity = int(input("What quantity do you want "))
#             if quantity > 0:
#                 cart.add_product(all_products[product_code], quantity)
#             else:
#                 print("Invalid quantity. Quantity must be greater than 0.")
#         else:
#             print("Invalid product code. Try again")

#         continue_option = input("Would you like to add another product? YES/NO ").lower()
#         if continue_option != "yes":
#             break

#     total_price = sum(product[0].price_per1 * product[1] for product in cart.products)
#     total_price_with_vat = total_price * 1.2
#     delivery_cost = 5
#     final_price = total_price_with_vat + delivery_cost

#     print("Thank you for shopping with us! Your order: ")
#     for product, amount in cart.products:
#         print(f"{product.manufacturer} - {product.product_code} - Quantity: {amount} - Price: {product.price_per1}")

#     print(f"Total Price: {final_price}")

# else:
#     print("Thank you! See you next time.")

# EX.3 Create a program that allows the user to manage student information.

# class Student:
#     def __init__(self, name, student_id, grades):
#         self.name = name
#         self.student_id = student_id
#         self.grades = grades
#         self.calculate_grades()

#     def add_grade(self, grade):
#         self.grades.append(grade)
#         self.calculate_grades()
    
#     def calculate_grades(self):
#         self.average_grade = round(sum(self.grades) / len(self.grades), 2)
    

# def create_student():
#     name = str(input("Whats is the student name: "))
#     student_id = int(input("What is his/her id: "))
#     all_grades = [int(grade) for grade in input("Type the grades separated by spaces: ").split()]    
    
#     if all(grade >= 2 for grade in all_grades):
#         student = Student(name, student_id, all_grades)
#         print(f"Student created successfully: Name - {student.name}, ID - {student.student_id}, Average Grades - {student.average_grade}")
#     else:
#         print("All grades must be >= 2")

# while True:
#     add_student = input("Do you like to add a student yes/no: ")

#     if add_student == "yes":
#         create_student()
#     else:
#         print("Have a good day")
#         break

# EX.4 program for managing a library catalog

# class Book:
#     def __init__(self, title, author, isbn, copies_available):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.copies_available = copies_available

#     # Borrowing the book
#     def checkin(self):
#         if self.copies_available >= 0:
#             print(f"Book '{self.title}' checked out")
#             self.copies_available -= 1
#         else:
#             print("The book is not available")
    
#     # Returning the book
#     def checkout(self):
#         print(f"Book {self.title} is returned")
#         self.copies_available += 1

#     def display_info(self):
#         print(self.title)
#         print(self.author)
#         print(self.isbn)
#         print(self.copies_available)

# library_catalog = {}

# print("Welcome to the Python book library. \n You can check in or check out a book which you want or you ca add a new book in the library.")   

# # Allow the user to add books
# while True:
#     options = input("1. For adding a new book type 'add' \n2. For a checkin of a book type 'checkin' \n3. For a checkout of a book type 'checkout' \n4. If you are ready type 'exit' \n").lower() 
#     if options =="add":
#         title = input("Enter a book Title: ")
#         author = input("Enter an Author Name: ")
#         isbn = input("Enter a isbn: ")
#         copies_available = int(input("Enter the available copies of the book: "))

#         new_book = Book(title, author, isbn, copies_available)
#         library_catalog[isbn] = new_book

#     elif options =="checkin":
#         isbn = input("Type the ISBN of the book which you want, that will be checked for availability: ").lower()
#         if isbn in library_catalog:
#             library_catalog[isbn].checkin()
#         else:
#             print("Your book is not available")

#     elif options =="checkout":
#         isbn = input("Type the ISBN of the book which you want to return: ").lower()
#         if isbn in library_catalog:
#             library_catalog[isbn].checkout()
#         else:
#             print("Your book is not available")

#     elif options =="exit":
#         print("Library Catalog")
#         for isbn, book in library_catalog.items():
#             book.display_info()
#         break
#     else:
#         print("Invalid option. Please try again.")

# EX.5 Implement a program using a while loop that continuously prompts the user for input. 
#      If the entered number is positive, add it to list1. If the entered number is negative, add its absolute value to list2. 
#      Terminate the loop when the user enters 0.

# positive nums
list1 = []
# negative nums
list2 = []

while True:
    number = int(input("Enter a number different from 0. To exit the program type 0: "))
    if number > 0:
        list1.append(number)
    elif number < 0:
        list2.append(number)
    elif number == 0:
        print(f"Here are the positive numbers: {list1} \n Here are the negative numbers: {list2}")
        break
    else:
        print("Please enter a valid number!")
