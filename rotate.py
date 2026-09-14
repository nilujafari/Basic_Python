x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 4
n1 = x[-r:]
n2 = x[:-r]
result = n1 + n2
print(n1 , n2)
print(result)




# Second Method
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 4
for i in range(r):
        rev_x = x.pop()
        x.insert(0, rev_x)
print(x)
