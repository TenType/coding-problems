n = int(input())
cows = list(map(int, input().split()))

steps = n-1
for i in range(n-2, 0, -1):
	if cows[i+1] < cows[i]:
		steps = i+1
		break

print(steps)
