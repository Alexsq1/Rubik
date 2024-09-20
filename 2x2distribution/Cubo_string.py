import copy


class Cubo:
    solved_state = 'WWWWGGOOBBRRGGOBRRYYY'

    def __init__(self, pos):

        if pos == '':
            self.pos = self.solved_state
        else:
            self.pos = pos

    def solved(self):
        return self.pos == self.solved_state

    def executeMoves(self, cad):

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
                self.R()
            elif m == "R'":
                self.Rp()

            elif m == "R2":
                self.R2()

            elif m == "U ":
                self.U()

            elif m == "U'":
                self.Up()

            elif m == "U2":
                self.U2()

            elif m == "F ":
                self.F()

            elif m == "F'":
                self.Fp()

            elif m == "F2":
                self.F2()

            elif m == "L ":
                self.L()

            elif m == "L'":
                self.Lp()

            elif m == "L2":
                self.L2()

            elif m == "B ":
                self.B()

            elif m == "B'":
                self.Bp()

            elif m == "B2":
                self.B2()

            elif m == "D ":
                self.D()

            elif m == "D'":
                self.Dp()

            elif m == "D2":
                self.D2()

            elif m == "x ":
                self.x()

            elif m == "x'":
                self.xp()

            elif m == "x2":
                self.x2()

            elif m == "y ":
                self.y()

            elif m == "y'":
                self.yp()

            elif m == "y2":
                self.y2()

            elif m == "z ":
                self.z()

            elif m == "z'":
                self.zp()

            elif m == "z2":
                self.z2()

            else:
                print("cadena no válida, mov:", m)

    def adjacent(self):

        l = []

        for i in range(9):
            nl = copy.deepcopy(self)
            l.append(nl)

        # s = set()

        l[0].R()
        l[1].Rp()
        l[2].R2()

        l[3].U()
        l[4].Up()
        l[5].U2()

        l[6].F()
        l[7].Fp()
        l[8].F2()

        #        for i in l:
        #           s.add(i)
        return l

    def R(self):
        nueva = (self.pos[12] + self.pos[1] + self.pos[2] +
                 self.pos[4] + self.pos[18] + self.pos[5] +
                 self.pos[6] + self.pos[7] + self.pos[8] +
                 self.pos[0] + self.pos[11] + self.pos[17] +
                 self.pos[20] + self.pos[13] + self.pos[14] +
                 self.pos[3] + self.pos[10] + self.pos[16] +
                 self.pos[15] + self.pos[19] + self.pos[9])

        self.pos = nueva

    def Rp(self):
        nueva = (self.pos[9] + self.pos[1] + self.pos[2] +
                 self.pos[15] + self.pos[3] + self.pos[5] +
                 self.pos[6] + self.pos[7] + self.pos[8] +
                 self.pos[20] + self.pos[16] + self.pos[10] +
                 self.pos[0] + self.pos[13] + self.pos[14] +
                 self.pos[18] + self.pos[17] + self.pos[11] +
                 self.pos[4] + self.pos[19] + self.pos[12])
        self.pos = nueva

    def R2(self):
        nueva = (self.pos[20] + self.pos[1] + self.pos[2] +
                 self.pos[18] + self.pos[15] + self.pos[5] +
                 self.pos[6] + self.pos[7] + self.pos[8] +
                 self.pos[12] + self.pos[17] + self.pos[16] +
                 self.pos[9] + self.pos[13] + self.pos[14] +
                 self.pos[4] + self.pos[11] + self.pos[10] +
                 self.pos[3] + self.pos[19] + self.pos[0])
        self.pos = nueva

    def U(self):
        nueva = (self.pos[3] + self.pos[0] + self.pos[1] +
                 self.pos[2] + self.pos[10] + self.pos[11] +
                 self.pos[4] + self.pos[5] + self.pos[6] +
                 self.pos[7] + self.pos[8] + self.pos[9] +
                 self.pos[12] + self.pos[13] + self.pos[14] +
                 self.pos[15] + self.pos[16] + self.pos[17] +
                 self.pos[18] + self.pos[19] + self.pos[20])

        self.pos = nueva

    def Up(self):
        nueva = (self.pos[1] + self.pos[2] + self.pos[3] +
                 self.pos[0] + self.pos[6] + self.pos[7] +
                 self.pos[8] + self.pos[9] + self.pos[10] +
                 self.pos[11] + self.pos[4] + self.pos[5] +
                 self.pos[12] + self.pos[13] + self.pos[14] +
                 self.pos[15] + self.pos[16] + self.pos[17] +
                 self.pos[18] + self.pos[19] + self.pos[20])

        self.pos = nueva

    def U2(self):
        nueva = (self.pos[2] + self.pos[3] + self.pos[0] +
                 self.pos[1] + self.pos[8] + self.pos[9] +
                 self.pos[10] + self.pos[11] + self.pos[4] +
                 self.pos[5] + self.pos[6] + self.pos[7] +
                 self.pos[12] + self.pos[13] + self.pos[14] +
                 self.pos[15] + self.pos[16] + self.pos[17] +
                 self.pos[18] + self.pos[19] + self.pos[20])

        self.pos = nueva

    def F(self):

        nueva = (self.pos[6] + self.pos[14] + self.pos[2] +
                 self.pos[3] + self.pos[5] + self.pos[13] +
                 self.pos[19] + self.pos[7] + self.pos[8] +
                 self.pos[9] + self.pos[10] + self.pos[1] +
                 self.pos[4] + self.pos[12] + self.pos[18] +
                 self.pos[15] + self.pos[16] + self.pos[0] +
                 self.pos[11] + self.pos[17] + self.pos[20])

        self.pos = nueva

    def Fp(self):
        nueva = (self.pos[17] + self.pos[11] + self.pos[2] +
                 self.pos[3] + self.pos[12] + self.pos[4] +
                 self.pos[0] + self.pos[7] + self.pos[8] +
                 self.pos[9] + self.pos[10] + self.pos[18] +
                 self.pos[13] + self.pos[5] + self.pos[1] +
                 self.pos[15] + self.pos[16] + self.pos[19] +
                 self.pos[14] + self.pos[6] + self.pos[20])

        self.pos = nueva

    def F2(self):
        nueva = (self.pos[19] + self.pos[18] + self.pos[2] +
                 self.pos[3] + self.pos[13] + self.pos[12] +
                 self.pos[17] + self.pos[7] + self.pos[8] +
                 self.pos[9] + self.pos[10] + self.pos[14] +
                 self.pos[5] + self.pos[4] + self.pos[11] +
                 self.pos[15] + self.pos[16] + self.pos[6] +
                 self.pos[1] + self.pos[0] + self.pos[20])

        self.pos = nueva

    def L(self):
        p = self.CP
        o = self.CO
        self.pos[p][0], self.pos[p][1], self.pos[p][6], self.pos[p][7] = self.pos[p][1], self.pos[p][6], self.pos[p][7], \
            self.pos[p][0]
        self.pos[o][0], self.pos[o][1], self.pos[o][6], self.pos[o][7] = self.pos[o][1], self.pos[o][6], self.pos[o][7], \
            self.pos[o][0]

        self.pos[o][0] = (self.pos[o][0] + 1) % 3
        self.pos[o][1] = (self.pos[o][1] + 2) % 3
        self.pos[o][6] = (self.pos[o][6] + 1) % 3
        self.pos[o][7] = (self.pos[o][7] + 2) % 3

    def Lp(self):
        p = self.CP
        o = self.CO
        self.pos[p][0], self.pos[p][1], self.pos[p][6], self.pos[p][7] = self.pos[p][7], self.pos[p][0], self.pos[p][1], \
            self.pos[p][6]
        self.pos[o][0], self.pos[o][1], self.pos[o][6], self.pos[o][7] = self.pos[o][7], self.pos[o][0], self.pos[o][1], \
            self.pos[o][6]

        self.pos[o][0] = (self.pos[o][0] + 1) % 3
        self.pos[o][1] = (self.pos[o][1] + 2) % 3
        self.pos[o][6] = (self.pos[o][6] + 1) % 3
        self.pos[o][7] = (self.pos[o][7] + 2) % 3

    def L2(self):
        p = self.CP
        o = self.CO

        self.pos[p][0], self.pos[p][1], self.pos[p][6], self.pos[p][7] = self.pos[p][6], self.pos[p][7], self.pos[p][0], \
            self.pos[p][1]
        self.pos[o][0], self.pos[o][1], self.pos[o][6], self.pos[o][7] = self.pos[o][6], self.pos[o][7], self.pos[o][0], \
            self.pos[o][1]

    def D(self):
        p = self.CP
        o = self.CO

        self.pos[p][4], self.pos[p][5], self.pos[p][6], self.pos[p][7] = self.pos[p][7], self.pos[p][4], self.pos[p][5], \
            self.pos[p][6]
        self.pos[o][4], self.pos[o][5], self.pos[o][6], self.pos[o][7] = self.pos[o][7], self.pos[o][4], self.pos[o][5], \
            self.pos[o][6]

    def Dp(self):
        p = self.CP
        o = self.CO

        self.pos[p][4], self.pos[p][5], self.pos[p][6], self.pos[p][7] = self.pos[p][5], self.pos[p][6], self.pos[p][7], \
            self.pos[p][4]
        self.pos[o][4], self.pos[o][5], self.pos[o][6], self.pos[o][7] = self.pos[o][5], self.pos[o][6], self.pos[o][7], \
            self.pos[o][4]

    def D2(self):
        p = self.CP
        o = self.CO

        self.pos[p][4], self.pos[p][5], self.pos[p][6], self.pos[p][7] = self.pos[p][6], self.pos[p][7], self.pos[p][4], \
            self.pos[p][5]
        self.pos[o][4], self.pos[o][5], self.pos[o][6], self.pos[o][7] = self.pos[o][6], self.pos[o][7], self.pos[o][4], \
            self.pos[o][5]

    def B(self):
        p = self.CP
        o = self.CO

        self.pos[p][1], self.pos[p][2], self.pos[p][5], self.pos[p][6] = self.pos[p][2], self.pos[p][5], self.pos[p][6], \
            self.pos[p][1]
        self.pos[o][1], self.pos[o][2], self.pos[o][5], self.pos[o][6] = self.pos[o][2], self.pos[o][5], self.pos[o][6], \
            self.pos[o][1]

        self.pos[o][1] = (self.pos[o][1] + 1) % 3
        self.pos[o][2] = (self.pos[o][2] + 2) % 3
        self.pos[o][5] = (self.pos[o][5] + 1) % 3
        self.pos[o][6] = (self.pos[o][6] + 2) % 3

    def Bp(self):
        p = self.CP
        o = self.CO

        self.pos[p][1], self.pos[p][2], self.pos[p][5], self.pos[p][6] = self.pos[p][6], self.pos[p][1], self.pos[p][2], \
            self.pos[p][5]
        self.pos[o][1], self.pos[o][2], self.pos[o][5], self.pos[o][6] = self.pos[o][6], self.pos[o][1], self.pos[o][2], \
            self.pos[o][5]

        self.pos[o][1] = (self.pos[o][1] + 1) % 3
        self.pos[o][2] = (self.pos[o][2] + 2) % 3
        self.pos[o][5] = (self.pos[o][5] + 1) % 3
        self.pos[o][6] = (self.pos[o][6] + 2) % 3

    def B2(self):
        p = self.CP
        o = self.CO

        self.pos[p][1], self.pos[p][2], self.pos[p][5], self.pos[p][6] = self.pos[p][5], self.pos[p][6], self.pos[p][1], \
            self.pos[p][2]
        self.pos[o][1], self.pos[o][2], self.pos[o][5], self.pos[o][6] = self.pos[o][5], self.pos[o][6], self.pos[o][1], \
            self.pos[o][2]

    def x(self):
        self.R()
        self.Lp()

    def xp(self):
        self.Rp()
        self.L()

    def x2(self):
        self.R2()
        self.L2()

    def y(self):
        self.U()
        self.Dp()

    def yp(self):
        self.Up()
        self.D()

    def y2(self):
        self.U2()
        self.D2()

    def z(self):
        self.F()
        self.Bp()

    def zp(self):
        self.Fp()
        self.B()

    def z2(self):
        self.F2()
        self.B2()


#####################################################################
# Fuera de la clase: métodos estáticos

def solved(pos):
    return pos == 'WWWWGGOOBBRRGGOBRRYYY'


def solved_state():
    return 'WWWWGGOOBBRRGGOBRRYYY'


def F(pos):
    return (pos[6] + pos[14] + pos[2] +
            pos[3] + pos[5] + pos[13] +
            pos[19] + pos[7] + pos[8] +
            pos[9] + pos[10] + pos[1] +
            pos[4] + pos[12] + pos[18] +
            pos[15] + pos[16] + pos[0] +
            pos[11] + pos[17] + pos[20])


# Front Quarter Turn Counterclockwise
def Fp(pos):
    return (pos[17] + pos[11] + pos[2] +
            pos[3] + pos[12] + pos[4] +
            pos[0] + pos[7] + pos[8] +
            pos[9] + pos[10] + pos[18] +
            pos[13] + pos[5] + pos[1] +
            pos[15] + pos[16] + pos[19] +
            pos[14] + pos[6] + pos[20])


# Front Half Turn
def F2(pos):
    return (pos[19] + pos[18] + pos[2] +
            pos[3] + pos[13] + pos[12] +
            pos[17] + pos[7] + pos[8] +
            pos[9] + pos[10] + pos[14] +
            pos[5] + pos[4] + pos[11] +
            pos[15] + pos[16] + pos[6] +
            pos[1] + pos[0] + pos[20])


# Right Quarter Turn Clockwise
def R(pos):
    return (pos[12] + pos[1] + pos[2] +
            pos[4] + pos[18] + pos[5] +
            pos[6] + pos[7] + pos[8] +
            pos[0] + pos[11] + pos[17] +
            pos[20] + pos[13] + pos[14] +
            pos[3] + pos[10] + pos[16] +
            pos[15] + pos[19] + pos[9])


# Right Quarter Turn Counterclockwise
def Rp(pos):
    return (pos[9] + pos[1] + pos[2] +
            pos[15] + pos[3] + pos[5] +
            pos[6] + pos[7] + pos[8] +
            pos[20] + pos[16] + pos[10] +
            pos[0] + pos[13] + pos[14] +
            pos[18] + pos[17] + pos[11] +
            pos[4] + pos[19] + pos[12])


# Right Half Turn
def R2(pos):
    return (pos[20] + pos[1] + pos[2] +
            pos[18] + pos[15] + pos[5] +
            pos[6] + pos[7] + pos[8] +
            pos[12] + pos[17] + pos[16] +
            pos[9] + pos[13] + pos[14] +
            pos[4] + pos[11] + pos[10] +
            pos[3] + pos[19] + pos[0])


# Up Quarter Turn Clockwise
def U(pos):
    return (pos[3] + pos[0] + pos[1] +
            pos[2] + pos[10] + pos[11] +
            pos[4] + pos[5] + pos[6] +
            pos[7] + pos[8] + pos[9] +
            pos[12] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[18] + pos[19] + pos[20])


# Up Quarter Turn Counterclockwise
def Up(pos):
    return (pos[1] + pos[2] + pos[3] +
            pos[0] + pos[6] + pos[7] +
            pos[8] + pos[9] + pos[10] +
            pos[11] + pos[4] + pos[5] +
            pos[12] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[18] + pos[19] + pos[20])


# Up Half Turn
def U2(pos):
    return (pos[2] + pos[3] + pos[0] +
            pos[1] + pos[8] + pos[9] +
            pos[10] + pos[11] + pos[4] +
            pos[5] + pos[6] + pos[7] +
            pos[12] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[18] + pos[19] + pos[20])


def adj_static(pos):
    return [R2(pos), R(pos), Rp(pos),
            U2(pos), U(pos), Up(pos),
            F2(pos), F(pos), Fp(pos)]

def mov_por_numero(i):
    if i == 0:
        return "R2 "
    if i == 1:
        return "R  "
    if i == 2:
        return "R' "
    if i == 3:
        return "U2 "
    if i == 4:
        return "U  "
    if i == 5:
        return "U' "
    if i == 6:
        return "F2 "
    if i == 7:
        return "F  "
    if i == 8:
        return "F' "
