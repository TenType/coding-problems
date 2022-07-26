n, m, x, y = map(int, input().split())
horse_position = [[x,y],[x-1,y-2], [x-1, y+2], [x+1, y-2], [x+1, y+2], [x-2, y-1], [x-2, y+1], [x+2, y-1], [x+2, y+1]]

from functools import lru_cache
@lru_cache(maxsize=None)
def chess(pos_x, pos_y):
	if [pos_x, pos_y] in horse_position:
		return 0

	if pos_x == 0:
		if [0, pos_y] in horse_position:
			return 0
		for i in range(1, pos_y+1):
			if [0, i] in horse_position:
				return 0
		return 1

	if pos_y == 0:
		if [pos_x, 0] in horse_position:
			return 0
		for i in range(1, pos_x+1):
			if [i, 0] in horse_position:
				return 0
		return 1

	return chess(pos_x - 1, pos_y) + chess(pos_x, pos_y - 1)

print(chess(n, m))

'''
if pos_x == 0 or pos_y == 0:
		if pos_x == 0:
			check = pos_x
			opposite = pos_y
		elif pos_y == 0:
			check = pos_y
			opposite = pos_x
			
		if [0, opposite] in horse_position:
			return 0
		for i in range(0, check):
			if [i, opposite] in horse_position:
				return 0
		return 1
'''
	
