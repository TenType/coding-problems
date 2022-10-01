n = int(input())
nums = []

for _ in range(n):
    [direction, num] = input().split(' ')
    nums.append([int(num), direction])

nums.sort()

min_liars = n
for i in range(n):
    liars = 0

    # check to the left
    for j in range(i):
        if nums[j][1] == 'L':
            liars += 1

    # check to the right
    for j in range(i, n):
        if nums[j][1] == 'G':
            liars += 1

    min_liars = min(min_liars, liars)

print(min_liars)
