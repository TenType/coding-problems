##n, p = map(int, input().split())
##f = []
##for i in range(0, n+1):
##    if i < p:
##        f.append(0)
##    elif i == p:
##        f.append(p*2)
##    else:
##        # print(i)
##        # print(f)
##        f.append(f[i-1] + i)
### print(f)
##print(f[-1])

##n, p = map(int, input().split())
##f = [p*2]
##for i in range(p+1, n+1):
##    # print(f[-1] + i)
##    f.append(f[-1] + i)
##print(f[-1])

n = int(input())
f = [2]
for i in range(2, n+1):
	f.append(f[-1] + i)
print(f[-1])
