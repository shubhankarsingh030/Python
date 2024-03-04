# Question -1 - Accept list element and reprint it.
# l =[]
# count = int(input("Tell how many number you want"))
# for i in range(count):
#     z = int(input("tell your nummber and press enter"))
#     l.append(z)
# print(l)


# Question 2- Print list element in reverse order

# a = [1,2,3,4,4,5,6,6,7]
# b = []

# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)

# Question 3 - Print positive and negetive element of List in seperate lists

# a = [1,-1,-5,6,-6,7,8,2,-7,0]
# pos = []
# neg = []
# zero = []
# for i in a:
#     if i > 0:
#         pos.append(i)
#     elif i < 0:
#         neg.append(i)
#     else:
#         zero.append(i)
# print(f"your positive element are {pos} \nand your negetive element{neg} \nand your number is zero {zero} ")

# Question- 4 - Find the greatest element and print its index too

# a = [45,56,22,12,11,452,95,700,2,5155]
# max = 0
# min = 0
# index = 0
# for i in range (len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"Your Maximum number is {max} at index {index}")

# Question 5 - Find the second Greatest Number and print its index too

# a = [1,3,56,33,67,1,0,56,345,100,400,412,410]
# max = 0
# max2 = 0
# index = 0
# index2 = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i
        
# print(max,max2)

# Question 6 - Check if list is sorted or not(using Function)

# def SortedorNot(x):
#     for i in range(len(x)-1):
#         if x[i] <= x[i+1]:
#             continue
#         else:
#             return("your list is not sorted")
            
#     else:
#         return("your list is sorted")
# a = [2,3,4,5,1,12,3,34,56,7,84,11,10]
# b = [1,2,3,4,5,6,7,8,9,10]
# print(SortedorNot(a))
# print(SortedorNot(b))

# Question 7 - Pallindromic List (Using Function)
# a = [1,2,2,2,2,2,1]
# c = [2,3,5,6,8,4,7,7,4,3]
# b = []

# def PallindromorNot(x):
#     for i in range(len(x)-1,-1,-1):
#         b.append(x[i])
#     if x == b:
#         return("Pallindrome")
#     else:
#         return("Not Pallindrom")
# print(PallindromorNot(a))
# print(PallindromorNot(c))

# Question 8 - How many separate element are there in list excluding the repeatation 

# a = [1,2,3,4,22,3,4,5,6,7,8,6,32,23,23,32,32,23]
# b = set(a)
# print(len(a))
