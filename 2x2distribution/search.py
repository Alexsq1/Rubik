# Generates every 2x2 position, categorized by depth.

import moves_default
import time

# Position structure (see readMe for details)
solved_position = 'WWWWGGOOBBRRGGOBRRYYY'

# Takes a position and returns a list of all the positions that arise from performing every move
def get_moves(pos):
	return [moves_default.F(pos), moves_default.Fp(pos), moves_default.F2(pos),
			moves_default.R(pos), moves_default.Rp(pos), moves_default.R2(pos),
			moves_default.U(pos), moves_default.Up(pos), moves_default.U2(pos)]

# Solves the problem
def solve():

	start_time = time.time()
	letters = ["F ", "F'", "F2", "R ", "R'", "R2", "U ", "U'", "U2"]
	d_aux = dict()
	for i in range(len(get_moves(solved_position))):
		d_aux[get_moves(solved_position)[i]] = letters[i]
	dist = [{solved_position: ""}, d_aux]
	print('Depth 0: 1 positions:')
	print('\nDepth 1: ' + str(len(dist[-1])) + ' positions:')
	for i in dist[-1].values():
		print(i)

	while dist[-1]:
		dist.append(dict())
		for pos in dist[-2].keys():
			for i in range(len(get_moves(pos))):
				if get_moves(pos)[i] not in dist[-2].keys() and get_moves(pos)[i] not in dist[-3].keys():
					dist[-1][get_moves(pos)[i]] = dist[-2][pos] + " " + letters[i]
		l = dist[-1].values()
		print('\nDepth ' + str(len(dist) - 1) + ': ' + str(len(dist[-1])) + ' positions:')
		for i in l:
			print(i)

	print('2x2 Depth is ' + str(len(dist) - 2) + ', solved in ' + str(round(time.time() - start_time, 2)) + ' seconds')

solve()
