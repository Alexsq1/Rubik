# Generates every 2x2 position, categorized by depth.

import moves
import time

# Position structure (see readMe for details)
solved_position = 'WGRBOYWWWWGGGGRRRRBBBBOOOOYYYY'

# Takes a position and returns a list of all the positions that arise from performing every move
def get_moves(pos):
	return [moves.R(pos), moves.Rp(pos),
			moves.L(pos), moves.Lp(pos),
			moves.U(pos), moves.Up(pos),
			moves.B(pos), moves.Bp(pos)]

# Solves the problem
def solve():
	start_time = time.time()
	letters = ["R ", "R'", "L ", "L'", "U ", "U'", "B ", "B'"]
	capa1 = dict()
	for i in range(len(get_moves(solved_position))):
		capa1[get_moves(solved_position)[i]] = letters[i]
	dist = [{solved_position: ""}, capa1]
	print('Depth 0: 1 positions:')
	print('\nDepth 1: ' + str(len(dist[-1])) + ' positions:')
	for i in dist[-1].values():
		print(i)

	while dist[-1]:
		dist.append(dict())
		for pos in dist[-2].keys():
			adjacent_cases = get_moves(pos)
			for i in range(len(adjacent_cases)):
				if adjacent_cases[i] not in dist[-2].keys() and adjacent_cases[i] not in dist[-3].keys():
					dist[-1][adjacent_cases[i]] = dist[-2][pos] + " " + letters[i]

		print('\nDepth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions: ')
		for i in dist[-1].values():
			print(i)
	print('Skewb Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')

solve()
