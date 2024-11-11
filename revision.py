# c = int(input("Enter the number: "))

# f = (c*9/5)+32


# print(f)



# num1 = int(input("Enter the number: "))
# num2 = int(input("Ente the second number: "))

# temp = num1
# num1 = num2 
# num2 = temp

# print(num1)
# print(num2)


# MY CODE OF REVESRE A NUMBER

# num3 = int(input("Ente the number to reverse: "))
# original_num = num3

# reversed_num = 0

# while num3>0:
       
#  reversed_num = num3%10
 
#  print(reversed_num,end="")
 
#  num3 = num3//10
 
# if original_num == reversed_num:
#        print("The number is palindrome")
# else:
#        print("The number is not palindrome")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Input a four-digit number
# number = int(input("Enter a four-digit number: "))

# # Store the original number for comparison
# original_number = number

# # Reverse the number
# reversed_number = 0
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10

# # Display the reversed number
# print("The reversed number is:", reversed_number)

# # Check if the original number is the same as the reversed number
# if original_number == reversed_number:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")




# import math

# # Function to calculate Euclidean distance
# def euclidean_distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# # Input coordinates of the first point
# x1 = float(input("Enter the x-coordinate of the first point: "))
# y1 = float(input("Enter the y-coordinate of the first point: "))

# # Input coordinates of the second point
# x2 = float(input("Enter the x-coordinate of the second point: "))
# y2 = float(input("Enter the y-coordinate of the second point: "))

# # Calculate the Euclidean distance
# distance = euclidean_distance(x1, y1, x2, y2)

# # Display the result
# print("The Euclidean distance between the two points is:", distance)


# angle1 = int(input("Enter the angle: "))
# angle2 = int(input("Enter the second angle: "))
# angle3 = int(input("Enter the third angle: "))

# sum = angle1+angle2+angle3

# if sum>180:
#     print(f"The three angle sum is more than 180 degree so it cannot form a triangle")
# else:
#     print(f"The three angles can form the triangle")


# print("hello world")


# num = int(input("Enter the number: "))

# fact = 1

# if num<0:
#        print("The number which is negative has no factorial")
# elif(num==0):
#        print("The factorial of 0 is 1")
# else:
#        for i in range(1,num+1):
#               fact = fact*i

# print(f"The factorail of the number is {fact}")




# def fact(num1):
#        if num1==0:
#               return 1
#        else:
#               return ((num1)*fact(num1-1))


# num1 = int(input("Enter the number: "))

# print(fact(num1))


# a = 0
# b = 1
# print(a,b,end=" ")

# for i in range(8):
#        c = a+b
#        print(c,end=" ")
#        a,b=b,c


# Create a dictionary with information about a book (title, author, year). Add a new key for the genre

# dict1 = {
#        "title" : "book",
#        "author" : "akshat",
#        "year" : 2004
# }

# dict1["price"] = 560
# print(dict1)

# Retrieve the value associated with a key from a dictionary of countries and capitals.

# title = dict1["title"]
# print(title)

# Update an existing value in a dictionary. Given a dictionary of student grades, update a specific student's grade.

# dict1["year"] = 2005
# print(dict1)


# Loop through a dictionary of usernames and emails to print each username and email.

# dict2 = {
#        "aakshat" : "35456",
#        "payal" : "ert4"
# }

# for user_name,email in dict2.items():
#        print(f"The username is {user_name} and the email is {email}")

# Check if a key exists in a dictionary of employee names and departments and print a message based on the result.

# employees = {
#     "Alice": "Finance",
#     "Bob": "Engineering",
#     "Charlie": "Marketing",
#     "David": "HR"
# }

# employee_name = "aakshat"

# if employee_name in employees:
#        print(f"The {employee_name} exist")
# else:
#        print(f"The  Employee name: {employee_name} does not exist")


# Get all keys from a dictionary of city names and their populations.

# city = {
#        "names" : "jaipue",
#        "populations" : 345666
# }


# for key in city:
#        print(f"{key}")


# # First dictionary with basic book information
# book_info_1 = {
#     "title": "To Kill a Mockingbird",
#     "author": "Harper Lee",
#     "year": 1960
# }

# # Second dictionary with additional information about the book
# book_info_2 = {
#     "publisher": "J.B. Lippincott & Co.",
#     "pages": 281,
#     "language": "English"
# }

# # Merging the dictionaries
# # Method 1: Using update() - modifies book_info_1 in place
# book_info_1.update(book_info_2)

# print(book_info_1)


# fruits = ["banana","apple","guava","orange"]
# colors = ["yellow","red","green","orange"]

# fruit_colors = dict(zip(fruits,colors))

# print(fruit_colors)





# Count occurrences: Write a function that counts the occurrences of each letter in a given string and stores the counts in a dictionary.


# def occrrences(count):
#        char_count = {}
#        for char in count:
#         if char in char_count:
#                char_count[char]+=1
#         else:
#                char_count[count] = 1
#        return char_count
# count = input("Enter the string: ")

# print(occrrences(count))


# def count_letter_occurrences(text):
#     # Initialize an empty dictionary to store letter counts
#     letter_counts = {}
    
#     # Convert text to lowercase for case-insensitivity
#     text = text.lower()
    
#     # Iterate through each character in the text
#     for char in text:
#         # Check if the character is a letter
#         if char.isalpha():
#             # Increment the count for each letter
#             if char in letter_counts:
#                 letter_counts[char] += 1
#             else:
#                 letter_counts[char] = 1
                
#     return letter_counts

# # Get input from the user
# text = input("Enter the string: ")

# # Print the letter occurrences
# print(count_letter_occurrences(text))


# square = {num: num**2 for num in range(1,11)}
# print(square)



# family = {
#        "aakshat" : "21",
#        "poorvi" : "25",
#        "payal" : "34"
# }

# new_family = {}

# for name,age in family.items():
#        if age in new_family:
#               new_family[age].append(name)
#        else:
#                new_family[age] = [name]
               

# print(new_family)      

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


# class hello:
#        def __init__(self,name,surname,father,mother):
#               self.name = name
#               self.surname = surname
#               self.father = father
#               self.mother = mother

# class byee(hello):
#        def __init__(self, name, surname, father, mother,child):
#               super().__init__(name, surname, father, mother)
#               self.child = child
              
# class bat():
#        def __init__(self,price,type,quality):
#               self.price = price
#               self.type = type
#               self.quality = quality

# class bowl(bat):
#       def __init__(self,price,type,quality,bowl_price):
#              super().__init__(price,type,quality)
#              self.bowl_price = bowl_price




# stu_record = [
#        {"stu_name" : "aakshat", "stu_roll_no" : 45, "stu_fathermobileno" : 4552, "stu_marks" : 70},
#          {"stu_name" : "satya", "stu_roll_no" : 56, "stu_fathermobileno" : 4598, "stu_marks" : 71},
#            {"stu_name" : "skasham", "stu_roll_no" : 10, "stu_fathermobileno" : 4655, "stu_marks" : 40},
#              {"stu_name" : "TUSHAR", "stu_roll_no" : 67, "stu_fathermobileno" : 4875, "stu_marks" : 50},
#                {"stu_name" : "dhruv", "stu_roll_no" : 12, "stu_fathermobileno" : 4559, "stu_marks" : 40}
# ]

# for record in stu_record:
#        if record["stu_marks"]<50:
#              print(f"The student {record['stu_name']} has failed and the father mobile number is {record['stu_fathermobileno']}")



# 10.	Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit


# cost_price = {
#   "book" : 45,
#   "book1" : 56,
#   "table" : 78,
#   "tennis" : 79
# }

# selling_price = {
#   "book" : 46,
#   "book1" : 54,
#   "book2" : 75,
#   "tennis" : 80
# }

# for price in cost_price:
#   for sp in selling_price:
#     if price>sp:
#       print("the book made profit")
#     else:
#       print("the book made loss")


# cost_price = {
#   "book": 45,
#   "book1": 56,
#   "table": 78,
#   "tennis": 79
# }

# selling_price = {
#   "book": 46,
#   "book1": 54,
#   "table": 75,
#   "tennis": 80
# }

# # Iterate over each item in cost_price
# for item in cost_price:
#     # Check if the item also exists in selling_price
#     if item in selling_price:
#         # Compare selling price and cost price for the item
#         if selling_price[item] > cost_price[item]:
#             print(f"{item} made a profit")
#         else:
#             print(f"{item} made a loss")
#     else:
#         print(f"{item} has no selling price data")


# 11.	Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

# p = int(input("Enter the principal amount: "))
# ROI = int(input("Enter the rate of interset: "))
# TP = int(input("The time peroid is this: "))

# SI = (p*ROI*TP)/100

# print(SI)

# 12.	Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

# v = 3.15*r**r*h

# r = int(input("enter the radius: "))
# h = int(input("Ente the height of the cyinder: "))

# v = 3.15*r*r*h

# print(v)

# cost_per_liter = 40
# price = v*cost_per_liter

# print(f"the price is :{price} ")


# 17.	Write a program that will take three digits from the user and add the square of each digit.

# num1 = int(input(""))
# num2 = int(input(""))
# num3 = int(input(""))

# square1 = num1**2
# square2 = num2**2
# square3 = num3**2

# total_sum = square1+square2+square3


# print(total_sum)


# num1 = int(input("enter the number here to check whethe it is armstrong or not: "))

# sum = 0
# temp = num1

# while temp >0:
#   digit = temp%10
#   cube = digit ** 4
#   sum = sum+cube
#   temp //= 10
  
# if sum==num1:
#   print("the number is an armstrong number: ")
# else:
#   print("the number is not an armstrong number")


# sum1 = 0

# num2 = int(input("ENTE THE NUMBER: "))

# for i in range(num2+1):
#   sum1+=i
  
# print(sum1)

# 25.	Write a program that can multiply 2 numbers provided by the user without using the * operator



# import math

# num3 = int(input("ENTEr the number: "))
# num4 = int(input("enter the second number: "))

# mul = 0

# for i in range(abs(num4)):
#   mul+=num3
  
# print(mul)

























