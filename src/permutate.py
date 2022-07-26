n = int(input())
f = []

### 1: convert n into 1, 2... n
### 2: permutate list of converted number
###    - keep permutating and swapping until there is only 1 number
###    - combine each digit array into a string then add it to another array
### 3: bubble sort array
### 4: print all from array

def swap(x, l, r):
	temp = x[l]
	x[l] = x[r]
	x[r] = temp

def permutate(x, l):
	
	if l == n - 1:
		# convert list into one string
		
		result = ""
		for m in range(0, n):
			result += x[m] + ' '
			 
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

# bubble sort
for z in range(1, len(f)):

	q = 1
	while q != len(f):
		if f[q-1] > f[q]:
			temp = f[q]
			f[q] = f[q-1]
			f[q-1] = temp
			
		q += int(1)

# print all
for e in range(0, len(f)):
	print(f[e])
			
