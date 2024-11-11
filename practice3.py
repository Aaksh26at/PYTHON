
# square_numbers = []

# for i in range(1,11):
#        square_numbers.append(i**2)
# print(square_numbers)



# l1 = [2,3,4,5,7,8]
# l2 = [3,4,5,6,7]
# l3 =[]
# for i in l1:
#        for j in l2:
#               l3.append(i*j)

# print(l3)  

# l1 =  [1,4,5,6,8,9,0]

# print(l1[:])           

# Given a list nums, find the sum of all elements in the list.

# nums = [2,3,4,6,7,8]
# sum = 0

# for i in nums:
#        sum+=i
# print(sum)

# Write a function to find the maximum element in a list.

# def find_max(max):
#        max_element = max[0]
#        for element in max:
#               if element>max_element:
#                max_element = element
#        return max_element
# max = [3,4,7,8,9]
# print(find_max(max))
       
# Remove all duplicates from a list.

# data = [10, 20, 30, 10, 30]

# def remove_duplicates(data):
#     l2 = []
#     for i in data:
#         if i not in l2:
#             l2.append(i)
#     return l2  # return statement moved outside the loop

# print(remove_duplicates(data))  # print the result with the correct input


# Count the occurrences of an element in a list.

# element_to_count = 2
# count = 0

# l2 = [2,3,4,5,2,5,6,2]
# for i in l2:
#        if i == element_to_count:
#               count+=1
# print(count)
          

# num1 = (input("Enter a number to check if a given string is palindrome or not: "))

# rev = num1[::-1]

# if num1==rev:
#     print("string is palindrome")
# else:
#     print("it is not palindrome")



li2 = [1,3,6,7,[4,5,7],[6,7,8]]

n = len(li2)

for i in range(n):
    if type(li2[i]) is list:
        if len(li2[i])>1:
            m = len(li2[i])
            for j in range(m):
                print(i,j,li2[i][j])
    else:
        print(i,li2[i])
        

    
    
    

