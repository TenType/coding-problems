##x = input()
##if str(x)[::-1] == str(x):
##    print("yes")
##else:
##    print("no")

x = input()
x.replace(" ", "")
l = 0
r = len(x) - 1
output = 'yes'
while l < r:
	if x[l] != x[r]:
		output = 'no'
		break
	else:
		l += 1
		r -= 1
print(output)
