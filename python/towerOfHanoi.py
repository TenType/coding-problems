x = int(input())
a = [1]
for i in range(1, x):
	a.append(2 * a[i-1] + 1)
print(a[-1])
