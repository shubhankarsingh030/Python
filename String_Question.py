# Question  - 1 - Print String in reverse, its length ,in upper case, lower case, & copy it to another string
# a = "shuBHankar"
# print(a.upper())
# print(a.lower())
# b =a
# print(a)
# print(len(a))
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
# print(a[::-1])
# b = "Singh"
# c = a+ b
# print(c) 


# Question - 2 - Lower case Letter should come first in another string

# a = "HellO LEts Do Lower case CaSE"
# b = ''
# for i in a:
#     if i.islower():
#         b = b + i
# for i in a:
#     if i.isupper():
#         b = b + i
# print(b)

# Question - 3 - Count All the letter, digit and special symbols
# str = "P@#yn26at^&i5ve"
# chr = 0
# dig = 0
# spchr = 0
# for i in str:
#     if i.isdigit():
#         dig = dig + 1   
#     elif i.isalpha():
#         chr = chr + 1
#     else:
#         spchr = spchr + 1

# print(f"your coutinh are \nnumber = {dig}\ncharacters = {chr}\nspcial character = {spchr}")

# Question - 4 - count all the vowel from the string

# def VowelCounter(x):
#     vowel = 0
#     const = 0
#     for i in x:
#         if i in "aeiouAEIOU":
#             vowel = vowel +1
#         elif i == " ":
#             continue
#         else:
#             const = const + 1
#     return f"Your Total Vowel are {vowel} and consonants are {const}" 
# a = " My Name Is Shubhakar Singh And lets Find All the vowels In this Sentence"
# b = "This is the second String Which Will Be Confined To Find Vowel and Consonant"
# print(VowelCounter(a))
# print(VowelCounter(b))

# Question -5 - check the string is pallindrome or not

# a = "Shubhankar"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if  a == b:
#     print("pallindrome")
# else:
#     print("nhi ho paaya")
