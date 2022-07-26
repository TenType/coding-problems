import math

n = int(input())
list_n = list(map(int, input().split()))
averages = []
list_new = list_n

# find all averages
for i in range(0, n):
	list_temp = list_n[i]
	list_new.pop(i)
	# print(list_new)
	
	total = 0
	for x in range(0, len(list_new)):
		total = total + list_new[x]
	# print(total)

	total_10 = total * 10
	total_10 = math.floor(total_10 / len(list_new))
	total = total_10 / 10
	# print(total)
	averages.append(total)
	list_new.insert(i, list_temp)

# find greatest answer
answer = averages[0]
for o in range(1, len(averages)):
	if averages[o] > answer:
		answer = averages[o]

print(answer)
