
# # def count1(input_string):
# #     vowels = "aeiouAEIOU"  # List of vowels
# #     count = 0  # Initialize vowel count

# #     # Iterate over each character in the string
# #     for char in input_string:
# #         if char in vowels:
# #             count += 1  # Increment count if character is a vowel

# #     return count

# # # Example usage
# # input_string = "Hello, World!"
# # vowel_count = count1(input_string)
# # print(f"The number of vowels in '{input_string}' is {vowel_count}.")


# # Create a Python program that generates a multiplication table for a given number using a for loop

# # THIS LINE TO TAKE INPUT FROM THE USER TO PRINT THE TABLE
# # number1 = int(input("Enter a number to print table: "))
# # count1 = 1

# # while count1 < 11:
# #     print(number1 * count1)
# #     count1 += 1


# # Write a Python program to reverse a list using a for loop.

# # list1 = [1,3,4,5,6]
# # list2 = []

# # for i in range(len(list1)-1,-1,-1):
# #   list2.append(list1[i])

# # print(list2)


# # Write a Python program to find the common elements between two lists using a for loop.

# list3 = [1,3,4,5]
# list4 = [1,3,6,7]
# common_elements = []

# # Loop through each element in list1
# for i in list3:
# # Check if the current element is also in list2
#   if i in list4:
# # If it is, add it to the common_elements list
#     common_elements.append(i)
# # PRINT THE COMMON ELEMENTS 
# print(common_elements)


# # Write a Python program to remove duplicates from a list using a for loop.

# list5 = [1,3,5,6]
# list6 = [1,3,5,7]
# remove_duplicates = []

# # Loop through each element in list5
# for i in list5:
# #Check if the current element is not in list6
#   if i not in list6:
# # If it is not then append the element
#     remove_duplicates.append(i)
# print(remove_duplicates)


# # Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.

# sum = 0
# for i in range(1,51):
#   if i%2!=0:
#     sum+=i

# print(sum)


# # Create a Python program that counts the number of words in a sentence using a for loop.
# words_count = 0
# str2 = "aakshat"
# for i in str2:
#   words_count+=1
# print(words_count)

# # Write a Python program that checks if a given year is a leap year using a for loop.

# leap_year = int(input("Enter a year to search for leap year: "))

# if leap_year/4==0:
#   print("This year is a leap year ")
# else:
#   print("This year is not a leap year")
  



elements = [1,2,3,4,5]

for i in elements:
       if i == 3:
              elements.remove(3)
       else:
              print(i)