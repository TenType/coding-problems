n = int(input())
cows = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
milk = [0, 0, 0, 0, 0, 0, 0]
for i in range(0, n):
	a, b = map(str, input().split())
	milk[cows.index(a)] += int(b)

minimum = 1000000
maximum = 0
for x in range(0, 7):
	if milk[x] < minimum:
		minimum = milk[x]
	if milk[x] > maximum:
		maximum = milk[x]

counter = 0
for y in range(1, maximum+1):
	if minimum + y in milk:
		for z in range(0, 7):
			if minimum + y == milk[z]:
				counter += 1
		break

if counter == 1:
	print(cows[milk.index(minimum + y)])
else:
	print('Tie')
