import sys
sys.setrecursionlimit(20000)

n = int(input())
f = []

def swap(x, l, r):
	x2 = list(x)
	temp = x2[l]
	x2[l] = x2[r]
	x2[r] = temp
	print(x2)
	x = tuple(x2)
	print(x)

def permutate(x, l):
	
	if l == n - 1:
		# convert list into one string

		for j in range(0, len(x)):
			if int(x[j]) == j+1:
				return
		
		result = ""
		for m in range(0, n):
			result += x[m]
			 
		f.append(result)
		return

	
	for i in range(l, n):
		swap(x, l, i)
		
		permutate(x, l+1)

		swap(x, l, i)


# convert n into 1, 2... n
y = ""
for o in range(1, n+1):
	y += str(o)
		
permutate(list(y), 0)
print(len(f))
