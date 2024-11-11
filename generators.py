# # ----------------------------------- 08-07-2024 ------------------------------------
# # print("hello world")


# # GENERATORS IN PYTHON

# # def myFunc():
# #   yield "Hello"
# #   yield 51
# #   yield "Good Bye"

# # x = myFunc()

# # for z in x:
# #   print(z)
  
# def play(n):
#    l5 = []
#    for i in n:
#           if i%2==0:
#            l5.append(i)
#    return l5
# n = [4,6,8,10,3,9]
# print(play(n))
 

# def fact2(n):
#  fact = 1
#  for i in range(1,n+1):
#   fact*=i
#   print(fact)
# fact2(6)

# def swapPositions(lis, pos1, pos2):
#     for i, x in enumerate(lis):
#         if i == pos1:
#             elem1 = x
#         if i == pos2:
#             elem2 = x
#     lis[pos1] = elem2
#     lis[pos2] = elem1
#     return lis
 
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
# print(swapPositions(List, pos1-1, pos2-1))


# def reverse_list(list):
#        new_list = list[::-1]
#        return new_list
# list = [1,2,3,5,6,7,8,9]
# print(reverse_list(list))


# def negative(n):
#        for i in n:
#         if n<0:
#               return "negative number cannot print"
# n = [1,-2,3,5,6,8,-7]
# print(negative(n))



# ------------------------------ 09-07-2024 --------------------


# l1 = [10,20,30,40,50]
# l2 = [2,3,4,'a',5]

# result = []

# for i in l2:
#       for j in l1:
#         if type(i)!=str:
#          result.append(i*j)
        
# print(result)


l4 = [1, 2, 3, 4, (5, 6, 7, 8), {8, 9, 10}, {"value1": "bat", "value2": "bowl"}]
l5 = []
l6 = []
l7 = []
l8 = [] 

for item in l4:
    if type(item) == int:
        l5.append(item)
    elif type(item) == tuple:
        l6.append(item)
    elif type(item) == set:
        l7.append(item)
    elif type(item) == dict:
        l8.append(item)

print(l4)
print(l5)
print(l6)
print(l7)
print(l8)


class bike():
    print("hw")

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
