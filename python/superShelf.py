n, b = map(int, input().split())
cows = []
high = 1000001
low = 0
for i in range(0, n):
	cows.append(int(input()))

def dfs(check, tower):
	# if tower is closest to book
	global high
	if (tower >= b and tower < high):
		high = tower - b

	# out of bounds
	if (check >= n):
		return

	dfs(check+1, tower)
	dfs(check+1, tower+cows[check])

dfs(0, 0)

print(high)
