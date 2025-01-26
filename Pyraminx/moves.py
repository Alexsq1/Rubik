# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.

def R(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[5] + pos[3] + pos[4] +
			pos[6] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[11] +
			pos[12] + pos[13] +
			pos[14] + pos[15] +
			pos[18] + pos[19] +
			pos[21] + pos[20] +
			pos[17] + pos[16] +
			pos[22] + pos[23])


'''	
return (pos[0] + pos[1] + pos[2] +
			pos[3] + pos[4] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[11] +
			pos[12] + pos[13] +
			pos[14] + pos[15] +
			pos[16] + pos[17] +
			pos[18] + pos[19] +
			pos[20] + pos[21] +
			pos[22] + pos[23] )
			
			'''


def Rp(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[4] + pos[5] + pos[3] +
			pos[6] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[11] +
			pos[12] + pos[13] +
			pos[14] + pos[15] +
			pos[21] + pos[20] +
			pos[16] + pos[17] +
			pos[19] + pos[18] +
			pos[22] + pos[23] )


def L(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[3] + pos[4] + pos[5] +
			pos[8] + pos[6] + pos[7] +
			pos[9] + pos[10] + pos[11] +
			pos[22] + pos[23] +
			pos[14] + pos[15] +
			pos[16] + pos[17] +
			pos[13] + pos[12] +
			pos[20] + pos[21] +
			pos[19] + pos[18])


def Lp(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[3] + pos[4] + pos[5] +
			pos[7] + pos[8] + pos[6] +
			pos[9] + pos[10] + pos[11] +
			pos[19] + pos[18] +
			pos[14] + pos[15] +
			pos[16] + pos[17] +
			pos[23] + pos[22] +
			pos[20] + pos[21] +
			pos[12] + pos[13])

def B(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[3] + pos[4] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[11] + pos[9] + pos[10] +
			pos[12] + pos[13] +
			pos[20] + pos[21] +
			pos[16] + pos[17] +
			pos[18] + pos[19] +
			pos[23] + pos[22] +
			pos[15] + pos[14])


def Bp(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[3] + pos[4] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[10] + pos[11] + pos[9] +
			pos[12] + pos[13] +
			pos[23] + pos[22] +
			pos[16] + pos[17] +
			pos[18] + pos[19] +
			pos[14] + pos[15] +
			pos[21] + pos[20])


def U(pos):
	return (pos[2] + pos[0] + pos[1] +
			pos[3] + pos[4] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[11] +
			pos[16] + pos[17] +
			pos[12] + pos[13] +
			pos[14] + pos[15] +
			pos[18] + pos[19] +
			pos[20] + pos[21] +
			pos[22] + pos[23])


def Up(pos):
	return (pos[1] + pos[2] + pos[0] +
			pos[3] + pos[4] + pos[5] +
			pos[6] + pos[7] + pos[8] +
			pos[9] + pos[10] + pos[11] +
			pos[14] + pos[15] +
			pos[16] + pos[17] +
			pos[12] + pos[13] +
			pos[18] + pos[19] +
			pos[20] + pos[21] +
			pos[22] + pos[23])
