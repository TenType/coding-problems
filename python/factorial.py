##f = []
##
##def factorial(n):
##    result = n
##    for i in range(1, n):
##        if(i in f):
##            result = i * f[f.index(i)] 
##        else:
##            result = i * result
##            f.append(result)
##    print(result)
##
##factorial(3)
##factorial(4)

##n = int(input())
##arr = [1] * (n + 1)
##for i in range(1, n + 1):
##    arr[i] = i * arr[i - 1]
##
##print(arr)

n = int(input())
f = []
result = 1
for i in range(1, n + 1):
	result = i * result
	f.append(result)
print(result)
