n = int(input())

def solve_hanoi(disks, stick1, stick2, stick3):
	if disks <= 1:
		print('Move disk ' + str(disks) +  ' from rod ' + stick1 + ' to rod ' + stick3)
		return

	solve_hanoi(disks - 1, stick1, stick3, stick2)
	print('Move disk ' + str(disks) + ' from rod '+ stick1 + ' to rod ' + stick3)
	# solve_hanoi(1, stick1, stick2, stick3)
	solve_hanoi(disks - 1, stick2, stick1, stick3)
	# print(stick2 + '->' + stick3)

solve_hanoi(n, 'A', 'C', 'B')