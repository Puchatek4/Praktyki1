# print('Hello world')
# name = input("What is your name: ")
# country = input("Where are you from: ")
# fav = input("What is your favourite things: ")
# print("Hello, ")
# print("My name is", name)
# print("I'm from", country)
# print("My favourite thing is", fav)


# x = int(input("number X: "))
# y = int(input("number Y: "))
# if y == 0 :
#     y = int(input("number Y: "))
# else: 
#     print("X / Y =", x / y)
#     print("X + Y =", x + y)
#     print("X - Y =", x - y)
#     print("X * Y =", x * y)

# number = int(input("enter number: "))
# if number %2 == 0 :
#     print("even number")
# else:
#     print("Odd number")

# number = int(input("enter number: "))

# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero") 

# login = input("Enter login: ")
# password = input("Enter password: ")
# accept_login = "login"
# accept_password = "password"

# if login == accept_login and password == accept_password:
#     print("Great")
# else:
#     print("Bad login or password try again")

# age = int(input("How old are you: "))
# if age >= 16:
#     paid = input("Do you paid for course? (yes/no): ")
#     if paid == "yes":
#         score = int(input("What a score do you get? (0 -> 100): "))
#         if score > 80:
#             print("You get access to the high level")
#         elif score > 50:
#             print("You get access to the intermediate level")
#         else: 
#             print("You must pass an egzam with minimum 51 score")
#     else:
#         print("You must paid for a course")
# else:
#     print("You are to young")

# for i in range(5):
#     print("hello")
# i = 0
# while i <= 5:
#     print("hello")
#     i = i + 1

# for i in range(2, 20, 2):
#     print(i)

# for i in range(1, 5):
#     print("*" * i)

# balance = 1000
# while True:

#     print("balance:", balance)
#     action = int(input("DO you want deposit or withdraw your money? (deposit -> 0 || withdraw -> 1 ): " ))
#     if action == 0:
#         liczba = int(input("how much money do you deposit: "))
#         balance = balance + liczba
#         print(balance)
#     elif action == 1:
#         liczba = int(input("how much money do you withdraw: "))
#         balance = balance - liczba
#         if balance < 0:
#             print("You cant withdraw money. Go to work!!!") 
#             balance = balance + liczba
#         else:
#             print("transaction accepted")
            

# balance = 1000
# while True:
#     def checkbalance():
#         print("Your balance:", balance)

#     def deposite():
#         global balance
#         liczba = int(input("how much money do you deposit: "))
#         balance = balance + liczba
        
#     def withdraw():
#         global balance
#         liczba = int(input("how much money do you withdraw: "))
#         balance = balance - liczba
#         if balance < 0:
#             print("You cant withdraw money. Go to work!!!") 
#             balance = balance + liczba
#         else:
#             print("transaction accepted")


# # if action == 1:
#     #     checkbalance()
#     # elif action == 2:
#     #     deposite()
#     # elif action == 3: 
#     #     withdraw()
#     # elif action == 4:
#     #     break

#     action = int(input(" check balance -> 1 \n deposite money -> 2 \n withdraw money -> 3 \n exit -> 4 \n your choice: "))
#     match action:
#         case 1:
#             checkbalance()
#         case 2:
#             deposite()
#         case 3:
#             withdraw()
#         case 4:
#             break
#         case _:
#             print("not correct")


# fruits = ["mandarynka", "jabko", "pomidor", "banan", "kokos"]
# fruits.append("kiwi")
# fruits.insert(1, "truskawka")
# fruits[3] = 'borowka'
# del fruits[-1]
# print(fruits)
# print(fruits[0], fruits[-1])
students = []
how_many = int(input("How may students: "))
for i in range(how_many):
    name = input("Firstname:")
    lastname = input("Lastname:")
    age = int(input("Age:"))
    test = int(input("Test resoults: "))
    
    students.append([name, lastname, age])
    print("Aktualna lista:")
    print(students)

def student_list():
    global students
    print("student list: ")
    for i in students:
        print("--", i[0], i[2])
student_list()

 







# def search():
#     search_name = input("Search name: ")