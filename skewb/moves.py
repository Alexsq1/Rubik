# Hard coded moves to perform on the cube.
# Position is passed in and returned with the stickers in the order they should be after the turn.

def R(pos):
	return (pos[0] + pos[1] + pos[5] +
			pos[2] + pos[4] + pos[3] +
			pos[6] + pos[7] + pos[12] + pos[9] +
			pos[10] + pos[11] + pos[25] + pos[13] +
			pos[14] + pos[27] + pos[28] + pos[29] +
			pos[17] + pos[19] + pos[15] + pos[16] +
			pos[22] + pos[23] + pos[24] + pos[8] +
			pos[26] + pos[20] + pos[21] + pos[18] )

def Rp(pos):
	return (pos[0] + pos[1] + pos[3] +
			pos[5] + pos[4] + pos[2] +
			pos[6] + pos[7] + pos[25] + pos[9] +
			pos[10] + pos[11] + pos[8] + pos[13] +
			pos[14] + pos[20] + pos[21] + pos[18] +
			pos[29] + pos[19] + pos[27] + pos[28] +
			pos[22] + pos[23] + pos[24] + pos[12] +
			pos[26] + pos[15] + pos[16] + pos[17] )

def L(pos):
	return (pos[0] + pos[4] + pos[2] +
			pos[3] + pos[5] + pos[1] +
			pos[20] + pos[7] + pos[8] + pos[9] +
			pos[25] + pos[11] + pos[23] + pos[24] +
			pos[14] + pos[15] + pos[16] + pos[6] +
			pos[18] + pos[19] + pos[17] + pos[21] +
			pos[22] + pos[29] + pos[26] + pos[27] +
			pos[13] + pos[10] + pos[28] + pos[12] )


def Lp(pos):
	return (pos[0] + pos[5] + pos[2] +
			pos[3] + pos[1] + pos[4] +
			pos[17] + pos[7] + pos[8] + pos[9] +
			pos[27] + pos[11] + pos[29] + pos[26] +
			pos[14] + pos[15] + pos[16] + pos[20] +
			pos[18] + pos[19] + pos[6] + pos[21] +
			pos[22] + pos[12] + pos[13] + pos[10] +
			pos[24] + pos[25] + pos[28] + pos[23] )


def B(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[5] + pos[3] + pos[4] +
			pos[6] + pos[16] + pos[8] + pos[9] +
			pos[10] + pos[11] + pos[12] + pos[7] +
			pos[14] + pos[15] + pos[13] + pos[17] +
			pos[18] + pos[28] + pos[29] + pos[26] +
			pos[21] + pos[23] + pos[19] + pos[20] +
			pos[22] + pos[27] + pos[24] + pos[25] )


def Bp(pos):
	return (pos[0] + pos[1] + pos[2] +
			pos[4] + pos[5] + pos[3] +
			pos[6] + pos[13] + pos[8] + pos[9] +
			pos[10] + pos[11] + pos[12] + pos[16] +
			pos[14] + pos[15] + pos[7] + pos[17] +
			pos[18] + pos[24] + pos[25] + pos[22] +
			pos[26] + pos[23] + pos[28] + pos[29] +
			pos[21] + pos[27] + pos[19] + pos[20] )

def U(pos):
	return (pos[3] + pos[1] + pos[2] +
			pos[4] + pos[0] + pos[5] +
			pos[18] + pos[19] + pos[20] + pos[9] +
			pos[15] + pos[11] + pos[12] + pos[13] +
			pos[14] + pos[29] + pos[16] + pos[17] +
			pos[25] + pos[22] + pos[23] + pos[21] +
			pos[7] + pos[8] + pos[24] + pos[6] +
			pos[26] + pos[27] + pos[28] + pos[10] )


def Up(pos):
	return (pos[4] + pos[1] + pos[2] +
			pos[0] + pos[3] + pos[5] +
			pos[25] + pos[22] + pos[23] + pos[9] +
			pos[29] + pos[11] + pos[12] + pos[13] +
			pos[14] + pos[10] + pos[16] + pos[17] +
			pos[6] + pos[7] + pos[8] + pos[21] +
			pos[19] + pos[20] + pos[24] + pos[18] +
			pos[26] + pos[27] + pos[28] + pos[15] )
