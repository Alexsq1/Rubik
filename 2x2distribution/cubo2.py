import copy

p = 0
o = 1


def solved(pos):
    return pos == [[1,2,3,4,5,6,7,8], [0,0,0,0,0,0,0,0]]


def adjacent(pre):
    l = []
    pos = (pre)
    l.append(R(pos))
    l.append(Rp(pos))
    l.append(R2(pos))

    l.append(U(pos))
    l.append(Up(pos))
    l.append(U2(pos))

    l.append(F(pos))
    l.append(Fp(pos))
    l.append(F2(pos))

    return l

def executeMoves(pos, cad):

    cad = cad + " "
    fullMove = False

    for i in range(len(cad)):

        m = cad[i]
        if fullMove or m == " ":
            fullMove = False
            continue

        m = m + cad[i + 1]
        fullMove = True

        if m == "R ":
            pos.R(pos)
        elif m == "R'":
            pos.Rp(pos)

        elif m == "R2":
            pos.R2(pos)

        elif m == "U ":
            pos.U(pos)

        elif m == "U'":
            pos.Up(pos)

        elif m == "U2":
            pos.U2(pos)

        elif m == "F ":
            pos.F(pos)

        elif m == "F'":
            pos.Fp(pos)

        elif m == "F2":
            pos.F2(pos)

        elif m == "L ":
            pos.L(pos)

        elif m == "L'":
            pos.Lp(pos)

        elif m == "L2":
            pos.L2(pos)

        elif m == "B ":
            pos.B(pos)

        elif m == "B'":
            pos.Bp(pos)

        elif m == "B2":
            pos.B2(pos)

        elif m == "D ":
            pos.D(pos)

        elif m == "D'":
            pos.Dp(pos)

        elif m == "D2":
            pos.D2(pos)

        elif m == "x ":
            pos.x(pos)

        elif m == "x'":
            pos.xp(pos)

        elif m == "x2":
            pos.x2(pos)

        elif m == "y ":
            pos.y(pos)

        elif m == "y'":
            pos.yp(pos)

        elif m == "y2":
            pos.y2(pos)

        elif m == "z ":
            pos.z(pos)

        elif m == "z'":
            pos.zp(pos)

        elif m == "z2":
            pos.z2(pos)

        else:
            print("cadena no válida, mov:", m)


def R(pre):

    pos = copy.deepcopy(pre)

    pos[p][2], pos[p][3], pos[p][4], pos[p][5] = pos[p][3], pos[p][4], pos[p][5], pos[p][2]
    pos[o][2], pos[o][3], pos[o][4], pos[o][5] = pos[o][3], pos[o][4], pos[o][5], pos[o][2]

    pos[o][2] = (pos[o][2] + 1) % 3
    pos[o][3] = (pos[o][3] + 2) % 3
    pos[o][4] = (pos[o][4] + 1) % 3
    pos[o][5] = (pos[o][5] + 2) % 3

    return pos


def Rp(pre):

    pos = copy.deepcopy(pre)

    pos[p][2], pos[p][3], pos[p][4], pos[p][5] = pos[p][5], pos[p][2], pos[p][3], pos[p][4]
    pos[o][2], pos[o][3], pos[o][4], pos[o][5] = pos[o][5], pos[o][2], pos[o][3], pos[o][4]

    pos[o][2] = (pos[o][2] + 1) % 3
    pos[o][3] = (pos[o][3] + 2) % 3
    pos[o][4] = (pos[o][4] + 1) % 3
    pos[o][5] = (pos[o][5] + 2) % 3

    return pos
def R2(pre):

    pos = copy.deepcopy(pre)

    pos[p][2], pos[p][3], pos[p][4], pos[p][5] = pos[p][4], pos[p][5], pos[p][2], pos[p][3]
    pos[o][2], pos[o][3], pos[o][4], pos[o][5] = pos[o][4], pos[o][5], pos[o][2], pos[o][3]

    return pos
def U(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][2], pos[p][3] = pos[p][3], pos[p][0], pos[p][1], pos[p][2]
    pos[o][0], pos[o][1], pos[o][2], pos[o][3] = pos[o][3], pos[o][0], pos[o][1], pos[o][2]


    return pos
def Up(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][2], pos[p][3] = pos[p][1], pos[p][2], pos[p][3], pos[p][0]
    pos[o][0], pos[o][1], pos[o][2], pos[o][3] = pos[o][1], pos[o][2], pos[o][3], pos[o][0]

    return pos
def U2(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][2], pos[p][3] = pos[p][2], pos[p][3], pos[p][0], pos[p][1]
    pos[o][0], pos[o][1], pos[o][2], pos[o][3] = pos[o][2], pos[o][3], pos[o][0], pos[o][1]

    return pos
def F(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][3], pos[p][4], pos[p][7] = pos[p][7], pos[p][0], pos[p][3], pos[p][4]
    pos[o][0], pos[o][3], pos[o][4], pos[o][7] = pos[o][7], pos[o][0], pos[o][3], pos[o][4]

    pos[o][0] = (pos[o][0] + 2) % 3
    pos[o][3] = (pos[o][3] + 1) % 3
    pos[o][4] = (pos[o][4] + 2) % 3
    pos[o][7] = (pos[o][7] + 1) % 3

    return pos
def Fp(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][3], pos[p][4], pos[p][7] = pos[p][3], pos[p][4], pos[p][7], pos[p][0]
    pos[o][0], pos[o][3], pos[o][4], pos[o][7] = pos[o][3], pos[o][4], pos[o][7], pos[o][0]

    pos[o][0] = (pos[o][0] + 2) % 3
    pos[o][3] = (pos[o][3] + 1) % 3
    pos[o][4] = (pos[o][4] + 2) % 3
    pos[o][7] = (pos[o][7] + 1) % 3

    return pos
def F2(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][3], pos[p][4], pos[p][7] = pos[p][4], pos[p][7], pos[p][0], pos[p][3]
    pos[o][0], pos[o][3], pos[o][4], pos[o][7] = pos[o][4], pos[o][7], pos[o][0], pos[o][3],

    return pos
def L(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][6], pos[p][7] = pos[p][1], pos[p][6], pos[p][7], pos[p][0]
    pos[o][0], pos[o][1], pos[o][6], pos[o][7] = pos[o][1], pos[o][6], pos[o][7], pos[o][0]

    pos[o][0] = (pos[o][0] + 1) % 3
    pos[o][1] = (pos[o][1] + 2) % 3
    pos[o][6] = (pos[o][6] + 1) % 3
    pos[o][7] = (pos[o][7] + 2) % 3

    return pos
def Lp(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][6], pos[p][7] = pos[p][7], pos[p][0], pos[p][1], pos[p][6]
    pos[o][0], pos[o][1], pos[o][6], pos[o][7] = pos[o][7], pos[o][0], pos[o][1], pos[o][6]

    pos[o][0] = (pos[o][0] + 1) % 3
    pos[o][1] = (pos[o][1] + 2) % 3
    pos[o][6] = (pos[o][6] + 1) % 3
    pos[o][7] = (pos[o][7] + 2) % 3

    return pos
def L2(pre):

    pos = copy.deepcopy(pre)

    pos[p][0], pos[p][1], pos[p][6], pos[p][7] = pos[p][6], pos[p][7], pos[p][0], pos[p][1]
    pos[o][0], pos[o][1], pos[o][6], pos[o][7] = pos[o][6], pos[o][7], pos[o][0], pos[o][1]

    return pos
def D(pre):

    pos = copy.deepcopy(pre)

    pos[p][4], pos[p][5], pos[p][6], pos[p][7] = pos[p][7], pos[p][4], pos[p][5], pos[p][6]
    pos[o][4], pos[o][5], pos[o][6], pos[o][7] = pos[o][7], pos[o][4], pos[o][5], pos[o][6]

    return pos
def Dp(pre):

    pos = copy.deepcopy(pre)

    pos[p][4], pos[p][5], pos[p][6], pos[p][7] = pos[p][5], pos[p][6], pos[p][7], pos[p][4]
    pos[o][4], pos[o][5], pos[o][6], pos[o][7] = pos[o][5], pos[o][6], pos[o][7], pos[o][4]

    return pos

def D2(pre):

    pos = copy.deepcopy(pre)

    pos[p][4], pos[p][5], pos[p][6], pos[p][7] = pos[p][6], pos[p][7], pos[p][4], pos[p][5]
    pos[o][4], pos[o][5], pos[o][6], pos[o][7] = pos[o][6], pos[o][7], pos[o][4], pos[o][5]

    return pos

def B(pre):

    pos = copy.deepcopy(pre)

    pos[p][1], pos[p][2], pos[p][5], pos[p][6] = pos[p][2], pos[p][5], pos[p][6], pos[p][1]
    pos[o][1], pos[o][2], pos[o][5], pos[o][6] = pos[o][2], pos[o][5], pos[o][6], pos[o][1]

    pos[o][1] = (pos[o][1] + 1) % 3
    pos[o][2] = (pos[o][2] + 2) % 3
    pos[o][5] = (pos[o][5] + 1) % 3
    pos[o][6] = (pos[o][6] + 2) % 3

    return pos
def Bp(pre):

    pos = copy.deepcopy(pre)

    pos[p][1], pos[p][2], pos[p][5], pos[p][6] = pos[p][6], pos[p][1], pos[p][2], pos[p][5]
    pos[o][1], pos[o][2], pos[o][5], pos[o][6] = pos[o][6], pos[o][1], pos[o][2], pos[o][5]

    pos[o][1] = (pos[o][1] + 1) % 3
    pos[o][2] = (pos[o][2] + 2) % 3
    pos[o][5] = (pos[o][5] + 1) % 3
    pos[o][6] = (pos[o][6] + 2) % 3

    return pos
def B2(pre):

    pos = copy.deepcopy(pre)

    pos[p][1], pos[p][2], pos[p][5], pos[p][6] = pos[p][5], pos[p][6], pos[p][1], pos[p][2]
    pos[o][1], pos[o][2], pos[o][5], pos[o][6] = pos[o][5], pos[o][6], pos[o][1], pos[o][2]

    return pos
def x(pre):

    pos = copy.deepcopy(pre)

    pos.R(pos)
    pos.Lp(pos)

    return pos
def xp(pre):

    pos = copy.deepcopy(pre)

    pos.Rp(pos)
    pos.L(pos)

    return pos
def x2(pre):

    pos = copy.deepcopy(pre)

    pos.R2(pos)
    pos.L2(pos)

    return pos

def y(pre):

    pos = copy.deepcopy(pre)

    pos.U(pos)
    pos.Dp(pos)

    return pos
def yp(pre):

    pos = copy.deepcopy(pre)

    pos.Up(pos)
    pos.D(pos)

    return pos
def y2(pre):

    pos = copy.deepcopy(pre)

    pos.U2(pos)
    pos.D2(pos)

    return pos
def z(pre):

    pos = copy.deepcopy(pre)

    pos.F(pos)
    pos.Bp(pos)

    return pos
def zp(pre):

    pos = copy.deepcopy(pre)

    pos.Fp(pos)
    pos.B(pos)

    return pos
def z2(pre):

    pos = copy.deepcopy(pre)

    pos.F2(pos)
    pos.B2(pos)

    return pos