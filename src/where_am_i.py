n = int(input())
f = [char for char in str(input())]
# print(f)

def combocheck(check):
	for i in range(k, len(f)):
		last = k*2
		# print(last)
		while last < len(f) + 1:
			target = ""
			# print(last-k, last)
			for j in range(last-k, last):
				target += f[j]
			# print(check, target)
			if target == check:
				# print(k, "was not the number")
				return False
			last += 1
	return True

k = 1
while k < len(f):
	check = ""
	for m in range(0, k):
		check += f[m]
	# print(check)
	if combocheck(check):
		# print(k)
		break
	else:
		k += 1

print(k)
			
