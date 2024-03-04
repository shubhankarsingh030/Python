# Question 1 - Merge two Python Dictionary

# a = {1:12,2:45,3:11,4:55}
# b = {5:77,6:66,7:55,8:44}

# c = a
# c.update(b)
# print(c)

# a.update(b)
# print(a)

# question 2 - sum all the values in dicstionary

# a = {1:12,2:45,3:11,4:55}
# sum = 0

# for i in a.values():
#     sum = sum + 1
# print(sum)

# Question 3 - count the frequency of each element in a list

# a = [1,2,3,2,2,3,4,5,56,6,5,4,3,3,3,4,5,6,78,8,99,8,76,]

# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1 
# print(dict)

# Question 4 - Comnine two dicstionary by adding two values for common keys

a = {1:12,2:45,3:11,4:55}
b = {4:77,6:66,7:55,8:44}

for i in b.keys():
    if i in a.keys():
        a[i] = a[i] + b [i]
    else:
        a[i] = b[i]
print(a)