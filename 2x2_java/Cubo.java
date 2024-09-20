public class Cubo {

    private int[] posicion;
    private int[] posicionMezcla;
    private int[][] S1 = {{1, 2, 5, 6, 3, 4, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0}, {1, 2, 4, 5, 6, 3, 7, 8, 0, 0, 1, 2, 1, 2, 0, 0}, {1, 2, 6, 3, 4, 5, 7, 8, 0, 0, 1, 2, 1, 2, 0, 0},
            {3, 4, 1, 2, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0}, {4, 1, 2, 3, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0}, {2, 3, 4, 1, 5, 6, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0},
            {5, 2, 3, 8, 1, 6, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0}, {8, 2, 3, 1, 4, 6, 7, 5, 2, 0, 0, 1, 2, 0, 0, 1}, {4, 2, 3, 5, 8, 6, 7, 1, 2, 0, 0, 1, 2, 0, 0, 1}};

    private String scramble = "F' U2 R U F2 R2 U R' F L2 F' B ";

    //Constructor

    public Cubo(){
        posicion = new int[17];
        posicionMezcla = new int[17];
        posicion[0] = 0;
        posicion[1] = 1;
        posicion[2] = 2;
        posicion[3] = 3;
        posicion[4] = 4;
        posicion[5] = 5;
        posicion[6] = 6;
        posicion[7] = 7;
        posicion[8] = 8;

        posicion[9] = 0;
        posicion[10] = 0;
        posicion[11] = 0;
        posicion[12] = 0;
        posicion[13] = 0;
        posicion[14] = 0;
        posicion[15] = 0;
        posicion[16] = 0;
        ejecutarMezcla();

    }
    public int[] getPosicion(){
        return posicion;
    }
    public void setPosicionInicial(int[] posicion){
        setPosicion(posicion);
    }

    public void imprimirPosicion(){

        for (int i = 1; i < 9; i++)
            System.out.print(posicion[i] + " ");
        System.out.println("");
        for (int i = 9; i < 17; i++)
            System.out.print(posicion[i] + " ");
        System.out.println("\n");
    }

    public void imprimirPosicionMezcla(){

        for (int i = 1; i < 9; i++)
            System.out.print(posicionMezcla[i] + " ");
        System.out.println("");
        for (int i = 9; i < 17; i++)
            System.out.print(posicionMezcla[i] + " ");
        System.out.println("\n");
    }
    private void setPosicion(int[] posicion){
        for(int i = 0; i < 17; i++)
            this.posicion[i] = posicion [i];

        for(int i = 0; i < 17; i++)
            posicionMezcla[i] = posicion[i];
    }

    public int[] getPosicionMezcla(){
        return posicionMezcla;
    }


    private void ejecutarMezcla(){

        scramble += " ";

        for(int i = 0; i < scramble.length(); i++){

            switch (scramble.charAt(i)){

                case 'R':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            R();
                            break;
                        case 39:
                            Rprima();
                            break;
                        case '2':
                            R2();
                            break;
                    }
                    break;
                case 'U':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            U();
                            break;
                        case 39:
                            Uprima();
                            break;
                        case '2':
                            U2();
                            break;
                    }
                    break;
                case 'F':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            F();
                            break;
                        case 39:
                            Fprima();
                            break;
                        case '2':
                            F2();
                            break;
                    }
                    break;
                case 'L':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            L();
                            break;
                        case 39:
                            Lprima();
                            break;
                        case '2':
                            L2();
                            break;
                    }
                    break;
                case 'D':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            D();
                            break;
                        case 39:
                            Dprima();
                            break;
                        case '2':
                            D2();
                            break;
                    }
                    break;
                case 'B':
                    switch (scramble.charAt(i + 1)){
                        case ' ':
                            B();
                            break;
                        case 39:
                            Bprima();
                            break;
                        case '2':
                            B2();
                            break;
                    }
                    break;
                default:
                    break;
            }
        }

        for(int i = 0; i < 17; i++)
            posicionMezcla[i] = posicion[i];
    }


    public boolean comprobarRotacion(int rotacionInicial){


        for(int i = 0; i < posicion.length; i++)
            posicion[i] = posicionMezcla[i];

        while (rotacionInicial > 0){
            switch (rotacionInicial % 10) {

                case 0:
                    break;
                case 1:
                    x2();
                    break;
                case 2:
                    x();
                    break;
                case 3:
                    xprima();
                    break;
                case 4:
                    y2();
                    break;
                case 5:
                    y();
                    break;
                case 6:
                    yprima();
                    break;
                case 7:
                    z2();
                    break;
                case 8:
                    z();
                    break;
                case 9:
                    zprima();
                    break;
            }
            rotacionInicial /= 10;
        }
        return posicion[7] == 7 && posicion[15] == 0;
    }

    public boolean resuelto(int rotacionInicial, int[] solucion) {

        for(int i = 0; i < 17; i++)
            posicion[i] = posicionMezcla[i];

        ejecutarMovimientos(rotacionInicial, solucion);

        boolean check = true;
        int i = 1;

        while (check == true && i < 8){
            if (posicion[i] != i)
                check = false;
            i++;
        }
        i++;
        while (check == true && i < 16){
            if (posicion[i] != 0)
                check = false;
            i++;
        }
        return check;
    }

    public boolean S1(int rotacionInicial, int[] solucion){


        for(int i = 0; i < 17; i++)
            posicion[i] = posicionMezcla[i];

        ejecutarMovimientos(rotacionInicial, solucion);

        boolean check = false;

        for(int i = 0; !check && i < 9; i++){
            check = true;
            for(int j = 0; check && j < 15; j++){
                check = (posicion[j + 1] == S1[i][j]);
            }
        }
        return check;
    }


    public void ejecutarMovimientos(int rotacionInicial, int[] solucion) {

        while (rotacionInicial > 0) {

            switch (rotacionInicial % 10) {
                case 0:
                    break;
                case 1:
                    x2();
                    break;
                case 2:
                    x();
                    break;
                case 3:
                    xprima();
                    break;
                case 4:
                    y2();
                    break;
                case 5:
                    y();
                    break;
                case 6:
                    yprima();
                    break;
                case 7:
                    z2();
                    break;
                case 8:
                    z();
                    break;
                case 9:
                    zprima();
                    break;
            }
            rotacionInicial /= 10;
        }

        for (int i = 0; i < 14; i++) {
            switch (solucion[i] % 10) {

                case 0:
                    break;
                case 1:
                    R2();
                    break;
                case 2:
                    R();
                    break;
                case 3:
                    Rprima();
                    break;
                case 4:
                    U2();
                    break;
                case 5:
                    U();
                    break;
                case 6:
                    Uprima();
                    break;
                case 7:
                    F2();
                    break;
                case 8:
                    F();
                    break;
                case 9:
                    Fprima();
                    break;
            }
        }
    }


    public void imprimirScramble(){
        System.out.println("La mezcla es: " + scramble);
    }


    private void R() {

        int aux = posicion[3];
        posicion[3] = posicion[4];
        posicion[4] = posicion[5];
        posicion[5] = posicion[6];
        posicion[6] = aux;

        aux = posicion[11];
        posicion[11] = posicion[12];
        posicion[12] = posicion[13];
        posicion[13] = posicion[14];
        posicion[14] = aux;

        posicion[11] += 1;
        posicion[12] += 2;
        posicion[13] += 1;
        posicion[14] += 2;

        orientacionModulo();
    }

    private void Rprima() {

        int aux = posicion[3];
        posicion[3] = posicion[6];
        posicion[6] = posicion[5];
        posicion[5] = posicion[4];
        posicion[4] = aux;

        aux = posicion[11];
        posicion[11] = posicion[14];
        posicion[14] = posicion[13];
        posicion[13] = posicion[12];
        posicion[12] = aux;

        posicion[11] += 1;
        posicion[12] += 2;
        posicion[13] += 1;
        posicion[14] += 2;

        orientacionModulo();
    }

    private void R2() {

        int aux = posicion[3];
        posicion[3] = posicion[5];
        posicion[5] = aux;

        aux = posicion[4];
        posicion[4] = posicion[6];
        posicion[6] = aux;

        aux = posicion[11];
        posicion[11] = posicion[13];
        posicion[13] = aux;

        aux = posicion[12];
        posicion[12] = posicion[14];
        posicion[14] = aux;
    }

    private void U() {

        int aux = posicion[1];
        posicion[1] = posicion[4];
        posicion[4] = posicion[3];
        posicion[3] = posicion[2];
        posicion[2] = aux;

        aux = posicion[9];
        posicion[9] = posicion[12];
        posicion[12] = posicion[11];
        posicion[11] = posicion[10];
        posicion[10] = aux;
    }

    private void Uprima() {

        int aux = posicion[1];
        posicion[1] = posicion[2];
        posicion[2] = posicion[3];
        posicion[3] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[10];
        posicion[10] = posicion[11];
        posicion[11] = posicion[12];
        posicion[12] = aux;
    }

    private void U2() {

        int aux = posicion[1];
        posicion[1] = posicion[3];
        posicion[3] = aux;

        aux = posicion[2];
        posicion[2] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[11];
        posicion[11] = aux;

        aux = posicion[10];
        posicion[10] = posicion[12];
        posicion[12] = aux;
    }

    private void F() {

        int aux = posicion[1];
        posicion[1] = posicion[8];
        posicion[8] = posicion[5];
        posicion[5] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[16];
        posicion[16] = posicion[13];
        posicion[13] = posicion[12];
        posicion[12] = aux;

        posicion[9] += 2;
        posicion[12] += 1;
        posicion[13] += 2;
        posicion[16] += 1;

        orientacionModulo();
    }

    private void Fprima() {

        int aux = posicion[1];
        posicion[1] = posicion[4];
        posicion[4] = posicion[5];
        posicion[5] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[12];
        posicion[12] = posicion[13];
        posicion[13] = posicion[16];
        posicion[16] = aux;

        posicion[9] += 2;
        posicion[12] += 1;
        posicion[13] += 2;
        posicion[16] += 1;

        orientacionModulo();
    }

    private void F2() {

        int aux = posicion[1];
        posicion[1] = posicion[5];
        posicion[5] = aux;

        aux = posicion[4];
        posicion[4] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[13];
        posicion[13] = aux;

        aux = posicion[12];
        posicion[12] = posicion[16];
        posicion[16] = aux;
    }

    private void L() {

        int aux = posicion[1];
        posicion[1] = posicion[2];
        posicion[2] = posicion[7];
        posicion[7] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[10];
        posicion[10] = posicion[15];
        posicion[15] = posicion[16];
        posicion[16] = aux;

        posicion[9] += 1;
        posicion[10] += 2;
        posicion[15] += 1;
        posicion[16] += 2;

        orientacionModulo();
    }

    private void Lprima() {

        int aux = posicion[1];
        posicion[1] = posicion[8];
        posicion[8] = posicion[7];
        posicion[7] = posicion[2];
        posicion[2] = aux;

        aux = posicion[9];
        posicion[9] = posicion[16];
        posicion[16] = posicion[15];
        posicion[15] = posicion[10];
        posicion[10] = aux;

        posicion[9] += 1;
        posicion[10] += 2;
        posicion[15] += 1;
        posicion[16] += 2;

        orientacionModulo();
    }

    private void L2() {

        int aux = posicion[1];
        posicion[1] = posicion[7];
        posicion[7] = aux;

        aux = posicion[2];
        posicion[2] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[15];
        posicion[15] = aux;

        aux = posicion[10];
        posicion[10] = posicion[16];
        posicion[16] = aux;
    }

    private void D() {

        int aux = posicion[5];
        posicion[5] = posicion[8];
        posicion[8] = posicion[7];
        posicion[7] = posicion[6];
        posicion[6] = aux;

        aux = posicion[13];
        posicion[13] = posicion[16];
        posicion[16] = posicion[15];
        posicion[15] = posicion[14];
        posicion[14] = aux;
    }

    private void Dprima() {

        int aux = posicion[5];
        posicion[5] = posicion[6];
        posicion[6] = posicion[7];
        posicion[7] = posicion[8];
        posicion[8] = aux;

        aux = posicion[13];
        posicion[13] = posicion[14];
        posicion[14] = posicion[15];
        posicion[15] = posicion[16];
        posicion[16] = aux;
    }

    private void D2() {

        int aux = posicion[5];
        posicion[5] = posicion[7];
        posicion[7] = aux;

        aux = posicion[6];
        posicion[6] = posicion[8];
        posicion[8] = aux;

        aux = posicion[13];
        posicion[13] = posicion[15];
        posicion[15] = aux;

        aux = posicion[14];
        posicion[14] = posicion[16];
        posicion[16] = aux;
    }

    private void B() {

        int aux = posicion[2];
        posicion[2] = posicion[3];
        posicion[3] = posicion[6];
        posicion[6] = posicion[7];
        posicion[7] = aux;

        aux = posicion[10];
        posicion[10] = posicion[11];
        posicion[11] = posicion[14];
        posicion[14] = posicion[15];
        posicion[15] = aux;

        posicion[10] += 1;
        posicion[11] += 2;
        posicion[14] += 1;
        posicion[15] += 2;

        orientacionModulo();
    }

    private void Bprima() {

        int aux = posicion[2];
        posicion[2] = posicion[7];
        posicion[7] = posicion[6];
        posicion[6] = posicion[3];
        posicion[3] = aux;

        aux = posicion[10];
        posicion[10] = posicion[15];
        posicion[15] = posicion[14];
        posicion[14] = posicion[11];
        posicion[11] = aux;

        posicion[10] += 1;
        posicion[11] += 2;
        posicion[14] += 1;
        posicion[15] += 2;

        orientacionModulo();
    }

    private void B2() {

        int aux = posicion[2];
        posicion[2] = posicion[6];
        posicion[6] = aux;

        aux = posicion[3];
        posicion[3] = posicion[7];
        posicion[7] = aux;

        aux = posicion[10];
        posicion[10] = posicion[14];
        posicion[14] = aux;

        aux = posicion[11];
        posicion[11] = posicion[15];
        posicion[15] = aux;
    }

    private void x() {

        int aux = posicion[3];
        posicion[3] = posicion[4];
        posicion[4] = posicion[5];
        posicion[5] = posicion[6];
        posicion[6] = aux;

        aux = posicion[11];
        posicion[11] = posicion[12];
        posicion[12] = posicion[13];
        posicion[13] = posicion[14];
        posicion[14] = aux;

        posicion[11] += 1;
        posicion[12] += 2;
        posicion[13] += 1;
        posicion[14] += 2;

        aux = posicion[1];
        posicion[1] = posicion[8];
        posicion[8] = posicion[7];
        posicion[7] = posicion[2];
        posicion[2] = aux;

        aux = posicion[9];
        posicion[9] = posicion[16];
        posicion[16] = posicion[15];
        posicion[15] = posicion[10];
        posicion[10] = aux;

        posicion[9] += 1;
        posicion[10] += 2;
        posicion[15] += 1;
        posicion[16] += 2;

        orientacionModulo();
    }

    private void xprima() {

        int aux = posicion[3];
        posicion[3] = posicion[6];
        posicion[6] = posicion[5];
        posicion[5] = posicion[4];
        posicion[4] = aux;

        aux = posicion[11];
        posicion[11] = posicion[14];
        posicion[14] = posicion[13];
        posicion[13] = posicion[12];
        posicion[12] = aux;

        posicion[11] += 1;
        posicion[12] += 2;
        posicion[13] += 1;
        posicion[14] += 2;

        aux = posicion[1];
        posicion[1] = posicion[2];
        posicion[2] = posicion[7];
        posicion[7] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[10];
        posicion[10] = posicion[15];
        posicion[15] = posicion[16];
        posicion[16] = aux;

        posicion[9] += 1;
        posicion[10] += 2;
        posicion[15] += 1;
        posicion[16] += 2;

        orientacionModulo();
    }

    private void x2() {

        int aux = posicion[3];
        posicion[3] = posicion[5];
        posicion[5] = aux;

        aux = posicion[4];
        posicion[4] = posicion[6];
        posicion[6] = aux;

        aux = posicion[11];
        posicion[11] = posicion[13];
        posicion[13] = aux;

        aux = posicion[12];
        posicion[12] = posicion[14];
        posicion[14] = aux;

        aux = posicion[1];
        posicion[1] = posicion[7];
        posicion[7] = aux;

        aux = posicion[2];
        posicion[2] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[15];
        posicion[15] = aux;

        aux = posicion[10];
        posicion[10] = posicion[16];
        posicion[16] = aux;
    }

    private void y() {

        int aux = posicion[1];
        posicion[1] = posicion[4];
        posicion[4] = posicion[3];
        posicion[3] = posicion[2];
        posicion[2] = aux;

        aux = posicion[9];
        posicion[9] = posicion[12];
        posicion[12] = posicion[11];
        posicion[11] = posicion[10];
        posicion[10] = aux;

        aux = posicion[5];
        posicion[5] = posicion[6];
        posicion[6] = posicion[7];
        posicion[7] = posicion[8];
        posicion[8] = aux;

        aux = posicion[13];
        posicion[13] = posicion[14];
        posicion[14] = posicion[15];
        posicion[15] = posicion[16];
        posicion[16] = aux;
    }

    private void yprima() {

        int aux = posicion[1];
        posicion[1] = posicion[2];
        posicion[2] = posicion[3];
        posicion[3] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[10];
        posicion[10] = posicion[11];
        posicion[11] = posicion[12];
        posicion[12] = aux;

        aux = posicion[5];
        posicion[5] = posicion[8];
        posicion[8] = posicion[7];
        posicion[7] = posicion[6];
        posicion[6] = aux;

        aux = posicion[13];
        posicion[13] = posicion[16];
        posicion[16] = posicion[15];
        posicion[15] = posicion[14];
        posicion[14] = aux;
    }

    private void y2() {

        int aux = posicion[1];
        posicion[1] = posicion[3];
        posicion[3] = aux;

        aux = posicion[2];
        posicion[2] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[11];
        posicion[11] = aux;

        aux = posicion[10];
        posicion[10] = posicion[12];
        posicion[12] = aux;

        aux = posicion[5];
        posicion[5] = posicion[7];
        posicion[7] = aux;

        aux = posicion[6];
        posicion[6] = posicion[8];
        posicion[8] = aux;

        aux = posicion[13];
        posicion[13] = posicion[15];
        posicion[15] = aux;

        aux = posicion[14];
        posicion[14] = posicion[16];
        posicion[16] = aux;
    }

    private void z() {

        int aux = posicion[1];
        posicion[1] = posicion[8];
        posicion[8] = posicion[5];
        posicion[5] = posicion[4];
        posicion[4] = aux;

        aux = posicion[9];
        posicion[9] = posicion[16];
        posicion[16] = posicion[13];
        posicion[13] = posicion[12];
        posicion[12] = aux;

        posicion[9] += 2;
        posicion[12] += 1;
        posicion[13] += 2;
        posicion[16] += 1;

        aux = posicion[2];
        posicion[2] = posicion[7];
        posicion[7] = posicion[6];
        posicion[6] = posicion[3];
        posicion[3] = aux;

        aux = posicion[10];
        posicion[10] = posicion[15];
        posicion[15] = posicion[14];
        posicion[14] = posicion[11];
        posicion[11] = aux;

        posicion[10] += 1;
        posicion[11] += 2;
        posicion[14] += 1;
        posicion[15] += 2;

        orientacionModulo();
    }

    private void zprima() {

        int aux = posicion[1];
        posicion[1] = posicion[4];
        posicion[4] = posicion[5];
        posicion[5] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[12];
        posicion[12] = posicion[13];
        posicion[13] = posicion[16];
        posicion[16] = aux;

        posicion[9] += 2;
        posicion[12] += 1;
        posicion[13] += 2;
        posicion[16] += 1;

        aux = posicion[2];
        posicion[2] = posicion[3];
        posicion[3] = posicion[6];
        posicion[6] = posicion[7];
        posicion[7] = aux;

        aux = posicion[10];
        posicion[10] = posicion[11];
        posicion[11] = posicion[14];
        posicion[14] = posicion[15];
        posicion[15] = aux;

        posicion[10] += 1;
        posicion[11] += 2;
        posicion[14] += 1;
        posicion[15] += 2;

        orientacionModulo();
    }

    private void z2() {

        int aux = posicion[1];
        posicion[1] = posicion[5];
        posicion[5] = aux;

        aux = posicion[4];
        posicion[4] = posicion[8];
        posicion[8] = aux;

        aux = posicion[9];
        posicion[9] = posicion[13];
        posicion[13] = aux;

        aux = posicion[12];
        posicion[12] = posicion[16];
        posicion[16] = aux;

        aux = posicion[2];
        posicion[2] = posicion[6];
        posicion[6] = aux;

        aux = posicion[3];
        posicion[3] = posicion[7];
        posicion[7] = aux;

        aux = posicion[10];
        posicion[10] = posicion[14];
        posicion[14] = aux;

        aux = posicion[11];
        posicion[11] = posicion[15];
        posicion[15] = aux;
    }

    private void orientacionModulo() {

        for (int i = 9; i < 17; i++) {
            posicion[i] %= 3;
        }
    }
}