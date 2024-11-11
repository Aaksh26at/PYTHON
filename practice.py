# Side = float(input("Enter your square side: "))

# print("area of Square: ", Side*Side)

# float1 = float(input("Enter first number"))
# float2 = float(input("Enter your second number"))

# print2 = ((float1+float2)/2)
# print(print2)

# num1 = int(input("Enter your number: "))

# if(num1%7==0):
#        print("The number is the multiple of 7:",num1)
# else:
#        print("The number is not a multiple of 7")

# l1 = [2,5,8,7,9,10]
# l2 = []

# for i in l1:
#   if i%2==0:
#     l2.append(i)
# print(l2)

# THIS IS THE MAIN LIST
# l3 = [3,4,6,7,8,9,8,3,4,2]
# # THIS IS AN EMPTY LIST
# l4 = []

# # THIS LOOP WILL ITERATE THROUGH THE LIST
# for i in l3:
# # THIS CONDITION WILL CHECK THE ELEMENTS IF THE ELEMENTS IS ALREADY PRESENT IT WILL NOT APPEND THE ELEMENT TO THE LIST L4
#  if i not in l4:
# # THIS LINE WILL APPEND THE ELEMENTS TO THE LIST WHICH IS NOT PRESENT TO THE LIST
#   l4.append(i)
# # NOW PRINT THE LIST
# print(l4)

# l6 = [2,3,4,5]
# sum = 0
# for i in l6:
#  sum+=i
# print(sum)


# l7 = [1,4,5,6,7,8,10]
# greater = 0
# for i in l7:
#   if i>greater:
#    greater = i
# print(greater)

# l8 = [1,2,3,4,6,7,8,9]
# counttocount = 2
# count = 0
# for i in l8:
#  if counttocount==i:
#   count = count+1
# print(count)

# Define the list to be reversed
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Initialize an empty list to store the reversed elements
# reversed_list = []

# # Loop through the original list in reverse order
# for i in range(len(original_list) - 1, -1, -1):
#     reversed_list.append(original_list[i])

# # Print the reversed list
# print("Original list:", original_list)
# print("Reversed list:", reversed_list)

# Write a Python program that calculates the sum of all even numbers from 1 to 100.

# sum = 0
# for i in range(1,101):
#   if i%2==0:
#     sum+=i
# print(sum)


# Print all prime numbers between 1 and 50
# for num in range(1, 51):
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)


# Write a Python program to calculate the factorial of a given number using a loop.

def call_fact(n):
 fact = 1
 for i in range(1,n+1):
  fact*=i
 print(fact)
call_fact(6)

# num = int(input("Enter your first number: "))

# fact = 1
# for i in range(1,num+1):
#   fact*=i
  
# print(fact)

# a = 0
# b = 1

# num = int(input("Enter the number to obtain fibonacci series"))

# if num==1:
#   print(a)
# else:
#   print(a)
#   print(b)
#   for i in range(1,num+1):
#     c = a+b
#     a = b
#     b = c
#     print(c) 
 

# def fibonacci(n):
#  if n<=0:
#     return "enter the positive integer"
#  elif n==1:
#    return [0]
#  elif n ==2:
#    return [0,1]
#  else:
#    fib_series = fibonacci(n-1)
#    fib_series.append(fib_series[-1] + fib_series[-2])
#    return fib_series
 
#  n = 10  # Number of terms in the Fibonacci series
#  print(n)


# GROCERY SHOPPING PROJECT

# DEFINE THE MENU OF RESTURANT

# menu = {
#   'pizza' : 40,
#   'Pasta' : 50,
#   'Burger': 60,
#   'salad' : 70,
#   'coffee': 80,
# }
# # GREET
# print("Welcome to PYTHON Resturant")
# print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80 ")

# order_total = 0

# item_1 = input("Enter the name of item you want to order = ")
# if item_1 in menu:
#   order_total += menu[item_1]
#   print("Your item {item_1} has been added to your order")
# else:
#   print("ordered item {item_1} is not avaiable yet")

# another_order = input("Do you want to add another item? (yes/no)")
# if another_order == "yes":
#   item_2 = input("Enter the name of second item =")
#   if item_2 in menu:
#     order_total += menu[item_2]
#     print(f"Item {item_2} has been added to order")
#   else:
#     print(f"Ordered item {item_2} is not avaiable!")

# print(F"The total amount of items to pay is {order_total}")




# def print_values(n):
#    if n<0:
#           return
#    print(n)  
#    print_values(n-1)
   
# print_values(10)

# -------------------------- 05-07-2024 --------------------------------------------
# def first(n):
#        if n==0:
#               return "HELLO WORLD"
#        else:
#               return "Nothing"
       
# print(first(0))


# a = 0
# b = 1

# num = int(input("ENTER THE NUMBER YOU WANT TO PRINT FIBONACCI SERIES: "))

# if num==1 or num==0:
#        print(1)
# else:
#        print(a)
#        print(b)
       
#        for i in range(1,num+1):
#               c = a+b
#               a = b
#               b = c
#               print(c)

# --------------------------07-07-2024------------------------------------------

# matrix = []

# for i in range(5):
#        matrix.append([])
#        for j in range(5):
#               matrix[i].append(j)
# print(matrix)


# matrix1 = [[j for j in range(5)] for i in range(5)]

# print(matrix1)



# matrix2 = [[1,2,3,4],[5,6,7,8,19],[20,23,24,26]]

# odd_numbers = []

# for row in matrix2:
#        for element in row:
#               if element%2 != 0 :
#                      odd_numbers.append(element)
# print(odd_numbers)



# matrix3 = [[1,2,3,4,5],[6],[7,8,9]]

# matrix4 = []

# for sublist in matrix3:
#        for val in sublist:
#               matrix4.append(val)
# print(matrix4)



#  TOTAL SUM OF A NESTED LIST


# def sum (nested_list):
#        total_sum = 0
#        for sublist in nested_list:
#               for item in sublist:
#                      total_sum+=item
#        return total_sum
       
# nested_list = [
#        [1,2,3,4],
#        [5,6,7,8],
#        [7,8,9,0]
# ]

# print(sum(nested_list))



# def maximun(nested_list):
#        maximun_number = int()
#        for sublist in nested_list:
#               for items in sublist:
#                      if items>maximun_number:
#                             maximun_number = items
#        return maximun_number
# nested_list = [
#        [1,2,3,4],
#        [5,6,7,8],
# ]

# print(maximun(nested_list))



# def even_numbers(nested_list):
#        l3 = []
#        for i in nested_list:
#               for j in i:
#                      if i%2==0:
#                             l3.append(i)
#               return even_numbers

# nested_list =  [
#        [1,3,5,6],
#        [3,6,8,9,10]
# ]
# print(even_numbers(nested_list))


# ----------------------  08-07-2024  ------------------------------------------------




# def even_numbers(nested_list):
#        l3 = []
#        for i in nested_list:
#               for j in i:
#                if j%2==0:
#                      l3.extend(j)
#        return even_numbers
# nested_list = [1,3,4,6,7,89]

# print(even_numbers(nested_list))









       

                       
                       




























