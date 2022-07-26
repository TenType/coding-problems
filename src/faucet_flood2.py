import sys
sys.setrecursionlimit(20000)

n = int(input())
f = []
checked = []
result = 0

s1 = 0
s2 = 0

def split(word):
	return [char for char in word]

for i in range(0, n):
	text = split(str(input()))
	f.append(text)
	if '*' in text:
		s1 = i
		s2 = text.index('*')
		
	checked.append([])
	for o in range(0, len(f[i])):
		checked[i].append(False)

def flood(x, y):
	if x < 0 or y < 0 or x > n-1 or y > n-1:
		return
	if f[y][x] == '-' or checked[y][x]:
		return

	global result
	result += 1
	checked[y][x] = True
	# print(x, y)
	
	flood(x-1, y)
	flood(x+1, y)
	flood(x, y+1)
	flood(x, y-1)
	flood(x-1, y+1)
	flood(x-1, y-1)
	flood(x+1, y+1)
	flood(x+1, y-1)

print(s1, s2)
flood(s1, s2)
print(result)
