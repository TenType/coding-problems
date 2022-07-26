n = int(input())
f = [0, 1, 2, 4]
if n <= 0:
	print(0)
elif n < 3:
	print(f[n])
else:
	for i in range(3, n):
		f.append(f[i - 2] + f[i - 1] + f[i])
	print(f[-1] % 998244353)
	print(f)
