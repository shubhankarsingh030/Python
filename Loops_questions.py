# Queston  - 1 Print Natural Number
# n = int(input("Enter your number"))
# for i in range(1,n+1):
#     print(i)

# Question - 2 - Reverse for loop

# n = int(input("enter your number"))
# for i in range(n,0,-1):
#     print(i)

# Question - 3 - Take number as input and print its table

#n = int(input("Enter your number for it's table"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# n = int(input("enter your number for the table"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# Question - 4 - sum up to n terms
# n = int(input("enter your number for the sum"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# Question - 5 - factorial of the number
# n = int(input("enter your number for facotrial"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)

#  Question - 6 - print all the factor of number
# n = int(input("Enter your number for the Factors"))
# print("All the Factors of your Number are",end= "--")
# for i in range(1,n+1):
#     if n%i ==0:
#         print(i,end= " ")

# Question -7 - accept the number and check it is perfect or not

# n = int(input("Enter your Number"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("Its a perfect number")
# else:
#     print("its not a perfect number")

# Question - 8 - check for the number is prime or not

# n = int(input("enter your number"))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("Its a prime number")
# else:
#     print("Its not a prime number")

# Question - 9 - saperate each digit in number and print in new line

# n = int(input("enter your number"))
# while n > 0:
#     print(n%10)
#     n = n//10

# Question 10 - accept a number and check it is pallindromic or not

# n = int(input("enter your number"))
# copy = n
# rev = 0
# while n > 0:
#     z = (n%10)
#     rev = rev * 10 +z
#     n = n//10
# if copy == rev:
#     print("its a pollindromic number")
# else:
#     ("its not a pollindromic number")
