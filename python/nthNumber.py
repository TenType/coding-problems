n = int(input())
f = [0, 1, 1]

for i in range(3, n):
	f.append(f[i-3] + 2 * f[i-2] + f[i-1])

if n <= 1:
	print(0)
else:
	print(f[-1])
