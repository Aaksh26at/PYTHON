# *
# **
# ***
# ****
# *****


# size = 5

# for i in range(1, size + 1):
#     for j in range(1, size + 1):
#         print(f"{i * j}\t", end='')
#     print()


# rows = 5

# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end='')
#     print()


# rows = 6

# for i in range(1,rows+1):
#        for j in range(i-1):
#               print("*",end="")
#        print()




# for letter in 'AB':
#     for number in '12':
#         print(letter + number, end=" ")
# print()


# for i in range(1, 4):
#     total = 0
#     for j in range(1, i+1):
#         total += j
#         print(total, end=" ")
# print()


# for i in range(1, 5):
#     for j in range(1, 5):
#         if (i + j) % 2 == 0:
#             print(f"({i}, {j})", end=" ")
# print()


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()



# for i in range(1, 6):
#     print(f"Factors of {i}: ", end="")
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print(j, end=" ")
#     print()



for i in range(2,10):
       is_prime = True
       for j in range(2,i):
              if i%j==0:
                     is_prime = False
                     break
       if is_prime:
              print(i,end = " ")
print()



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for i in matrix:
    for j in i:
        total += j
print("Total sum:", total)



# for i in range(3):
#     for j in range(3):
#         print(f"({i}, {j})")



# strings = ["hello", "world", "python"]
# vowels = "aeiou"
# for string in strings:
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     print(f"'{string}' has {count} vowels")



# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()

# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("W", end=" ")
#         else:
#             print("B", end=" ")
#     print()


# for i in range(1, 6):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j
#     print(f"Factorial of {i} is {factorial}")



# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# summed_list = []
# for i in range(len(list1)):
#     summed_list.append(list1[i] + list2[i])
# print(summed_list)


# string = "hello"
# frequency = {}
# for char in string:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
# print(frequency)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common = []
# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)


# size = 3
# matrix = []
# for i in range(size):
#     row = []
#     for j in range(size):
#         if i == j:
#             row.append(1)
#         else:
#             row.append(0)
#     matrix.append(row)
# for row in matrix:
#     print(row)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b = numbers[::-1]
# for i in b:
#     print(b)


# num = int(input("Enter a number here: "))

# if num<=1:
#        print("1 is neither prime nor even number")
# if num>=1:
#        for i in range(2,num):
#               if num%i==0:
#                print("it is not a prime number")
#                break
#        else:
#               print("it is a prime number")


# num2 = int(input("Ente a number here: "))
# fact = 1

# for i in range(1,num2+1):
#        fact = fact*i
# print(f"The factorial of {num2} is: {fact}")
       



# list1 = []

# for i in range(1,7):
#        list1.append(i**2)
# print(list1)


# n=5

# for i in range(n):
#        for j in range(n):
#         print("*",end='')
# print()


# n=6

# for i in range(n):
#  for j in range(i+1):
#   print("*",end='')
# print()




# for i in range(2, 10):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         print(i, end=" ")
# print()


# list1 = [1, 2, 3]
# # list2 = [4, 5, 6]
# # summed_list = []
# # for i in range(len(list1)):
# #     summed_list.append(list1[i] + list2[i])
# # print(summed_list)



# num2 = int(input("Enter a number here: "))
# num3 = int(input("Enter another number here: "))

# for i in range(num2,num3+1):
#   if i>1:
#     for j in range(2,i):
#       if i%j==0:
#         break
#     else:
#       print(i)



# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = []
# for i in range(len(matrix[0])):
#     transpose_row = []
#     for j in range(len(matrix)):
#         transpose_row.append(matrix[j][i])
#     transpose.append(transpose_row)
# print(transpose)
    
    
# for i in range(5):
#     print(i)

# j = 0
# while j < 5:
#     print(j)
#     j += 1



# list1 = [1,2,4,6]
# list2 = [1,2,7,6]

# common = []

# for i in list1:
#   if i in list2:
#     common.append(i)
# print(common)

# matrix1 = [[2, 4, 6], 
#            [8, 10, 12], 
#            [14, 16, 18]]
# matrix2 = [[1, 3, 5], 
#            [7, 9, 11], 
#            [13, 15, 17]]
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]

# for r in result:
#     print(r)




# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# upper_triangular = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if i <= j:
#             upper_triangular[i][j] = matrix[i][j]

# for u in upper_triangular:
#     print(u)




# num2 = int(input("Enter a number here: "))
# num3 = int(input("Enter another number here: "))

# for i in range(num2,num3+1):
#        if num2%i==0:




list1 = [1, 1, 2, 2, 4, 6, 7, 7, 8]
list2 = []
for i in list1:
    if i in list2:
        list2.append(i)
print(list2)
              





