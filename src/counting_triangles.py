n = int(input())
f = [0, 1]
f2 = [0, 1]

for i in range(2, n+1):
	total = 0
	for o in range(0, i):
		total += i-o

	total2 = 0
	x = 1
	while True:
		total2 += i-x
		if i-x <= 1:
			break
		x += 2


##    if (i-value <= 1):
##        f2.append(f2[-1])
##    else:
##        f2.append(f2[i-1] + i-value)
##        value += 2
##
##    print(f2)
##    print(value)

	f.append(f[i-1] + total + total2)
	
print(f[-1])
