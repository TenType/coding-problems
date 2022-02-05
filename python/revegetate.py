n, m = map(int, input().split())
connected = []
seeds = []
for i in range(0, n):
	connected.append([])
	
for i in range(0, m):
	a, b = map(int, input().split())
	if (b not in connected[a-1]):
		connected[a-1].append(b)
	if (a not in connected[b-1]):
		connected[b-1].append(a)

print(connected)
		

# for each pasture
for i in range(0, n):

	# for each seed
	for j in range(1, 4):
		valid = True

		# for each other pasture
		for k in range(1, 4):
			if k == j:
				continue
			if k in connected[j]:
				valid = False
				break

		if valid:
			seeds.append(k)
			break

print(seeds)
			

	
