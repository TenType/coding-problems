n = int(input())
f = [0, 0, 1]
if n < 3:
	print(0)
elif n == 3:
	print(1)
else:
	for i in range(3, n):
		result = f[i-1]
		for j in range(0, i-2):
			result = result + f[i-1-j] * f[2+j]
			# print(f[i-1-j] * f[2+j])
		f.append(result)
		# print(f)
	# print(f)
	print(f[-1])
# n = 10, expected 1430
