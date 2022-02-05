from functools import lru_cache

n = int(input())

@lru_cache(maxsize=None)
def circle(points):
	if points < 2:
		return 1

	result = circle(points-1)
	for i in range(0, points-1):
		result = result + circle(i) * circle(points-2-i)

	return result % 12345

print(circle(n) % 12345)
