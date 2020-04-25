my_var = [1,2,3,4,5,5]

temp = sum(my_var)

if temp%2 != 0:
    print(False)

for i in range(len(my_var)):
     if sum(my_var[:i]) == sum(my_var[i:]):
          print(my_var[:i],my_var[i:])
          
