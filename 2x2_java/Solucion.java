import java.util.Scanner;

public class Solucion {


    private int rotacionInicial;
    private int[] solucion;
    private Cubo cubo;
    private boolean manual;
    private boolean notacion;


    public Solucion(){

        rotacionInicial = 0;
        solucion = new int[15];
        cubo = new Cubo();
        manual = false;
        notacion = true;
    }


    public void setmanual(boolean manual){
        this.manual = manual;
    }

    public void setnotacion(boolean notacion) {
        this.notacion = notacion;
    }




    private int[] introducirPosicion(){

        boolean mezclaVálida = false;

        int[] posicion = new int[17];

        while(!mezclaVálida){
            System.out.println("Introduzca la posicion del cubo: ");

            for (int i = 1; i < 17; i++) {
                Scanner leer = new Scanner(System.in);
                posicion[i] = leer.nextInt();
            }
            mezclaVálida = mezclaVálida(posicion);
        }
        return posicion;
    }

    private static boolean mezclaVálida(int[] posicion){

        boolean check = true;

        for(int i = 1; i <= 8 && check; i++){
            for(int j = 1; j <= 8 && check; j++){
                if(posicion[i] == posicion[j] && i != j)
                    check = false;
                if(posicion[i] > 8 || posicion[i] <= 0)
                    check = false;
            }
        }

        int sumatorioOrientacion = 0;
        for(int i = 9; i <= 16; i++){
            sumatorioOrientacion += posicion[i];
            if(posicion[i] > 2 || posicion[i] < 0)
                check = false;
        }
        if((sumatorioOrientacion % 3) != 0)
            check = false;

        if(check)
            System.out.println("Mezcla válida. Buscando solucion...");
        else
            System.out.println("Mezcla no válida");

        return check;
    }


    public void buscarSolucionAntiguo(){       ///////////////////Llama desde main

        long tiempoInicial = System.currentTimeMillis();

        if(manual){
            int[] pos = introducirPosicion();
            cubo.setPosicionInicial(pos);
            tiempoInicial = System.currentTimeMillis();
        }
        else {
            cubo.imprimirScramble();
        }

        rotacionInicial = buscarRotacion();

        boolean resuelto = cubo.resuelto(rotacionInicial, solucion);

        if(resuelto){
        }
        else {
            while (!resuelto) {                                                 //El cerebro
                siguienteCancelando();

                resuelto = cubo.resuelto(rotacionInicial, solucion);

            }

            if (resuelto) {                                                     //imprime
                System.out.println("Solucion encontrada");
                imprimirSolucion(tiempoInicial, System.currentTimeMillis());

            }
        }
    }

    public void buscarSolucion(){       ///////////////////Llama desde main

        long tiempoInicial = System.currentTimeMillis();

        if(manual){
            int[] pos = introducirPosicion();
            cubo.setPosicionInicial(pos);
            tiempoInicial = System.currentTimeMillis();
        }
        else {
            cubo.imprimirScramble();
        }

        rotacionInicial = buscarRotacion();

        boolean resuelto = cubo.resuelto(rotacionInicial, solucion);
        boolean s1 = cubo.S1(rotacionInicial, solucion);
        boolean encontradoS1 = false;//if en S1
                //Comprobaciones solucion con una cifra más y todas iguales
                //else


        if(resuelto){
            System.out.println("El cubo ya está resuelto");
        }

        else {
            while (!resuelto) {                                                 //El cerebro


                if(s1 && !encontradoS1){     //Añade una cifra
                    encontradoS1 = true;
                    int i = 14;
                    while (solucion[i] == 0 && i > 0) {
                        i--;
                    }
                    solucion[i + 1] = 10;
                }


                siguienteCancelando();

                s1 = cubo.S1(rotacionInicial, solucion);
                resuelto = cubo.resuelto(rotacionInicial, solucion);
            }

            if (resuelto) {
                System.out.println("Solucion encontrada");
                imprimirSolucion(tiempoInicial, System.currentTimeMillis());
            }
        }
    }

    public void imprimirArray(int[] array){
        for(int i = 0; i < array.length; i++)
            System.out.print(array[i] + " ");
    }

    private int buscarRotacion() {

        rotacionInicial = 0;
        boolean check = false;
        check = cubo.comprobarRotacion(rotacionInicial);

        while (!check) {

            rotacionInicial++;

            check = cubo.comprobarRotacion(rotacionInicial);
        }
        return rotacionInicial;
    }

    private int[] siguienteCancelando(){

        boolean repetido = true;
        while(repetido) {

                                                        //Se podría probar búsqueda binaria
            int i = 14;
            while (solucion[i] == 0 && i > 0) {
                i--;
            }
            int ultimo = i;

            if (solucion[i] == 39) {
                solucion[i] = 11;
                i--;

                while (i >= 0 && solucion[i] == 39) {
                    solucion[i] = 11;
                    i--;
                }

                if (i == -1)
                    solucion[ultimo + 1] = 11;
                else {
                    solucion[i]++;
                    if ((solucion[i] % 10) % 3 == 1)
                        solucion[i] += 10;
                }
            } else {
                solucion[i]++;
                if ((solucion[i] % 10) % 3 == 1)
                    solucion[i] += 10;
            }
            repetido = repetido(ultimo);
        }
        return solucion;
    }

    private boolean repetido(int ultimo){

        boolean check = false;
        int i = ultimo;

        while(i > 0 && check == false){
            if(solucion[i] / 10 == solucion[i - 1] / 10)
                check = true;
            i--;
        }
        return check;
    }

    public int contarMovimientos(){

        int numeroMovimientos = 0;

        for (int j = 0; j < 14; j++) {
            if (solucion[j] != 0) {
                numeroMovimientos++;
            }
        }
        return numeroMovimientos;
    }

    private void imprimirSolucion(long tiempoInicial, long tiempoFinal){

        if(notacion)
            imprimirSolucionConNotacion();
        else
            imprimirSolucionSinNotacion();
        long tiempoTotal = tiempoFinal - tiempoInicial;

        int[] tiempoDef = new int[3];
        for(int i = 0; i < 3; i++){
            tiempoDef[i] = (int) tiempoTotal % 10;
            tiempoTotal /= 10;
        }
        System.out.println("\nSolucion encontrada en " + tiempoTotal + "." + tiempoDef[2] + tiempoDef[1] + tiempoDef[0] + " segundos\n");
    }

    private void imprimirSolucionSinNotacion() {

        System.out.println("");
        System.out.println("Solucion sin notacion: \n");
        while (rotacionInicial > 0){
            switch (rotacionInicial % 10) {

                case 0:
                    break;
                case 1:
                    System.out.println("Sin girar ninguna capa, rote verticalmente el cubo 2 veces");
                    break;
                case 2:
                    System.out.println("Sin girar ninguna capa, coloque la capa inferior en el frente");
                    break;
                case 3:
                    System.out.println("Sin girar ninguna capa, coloque la capa superior en el frente");
                    break;
                case 4:
                    System.out.println("Sin girar ninguna capa, rote horizontalmente el cubo 2 veces");
                    break;
                case 5:
                    System.out.println("Sin girar ninguna capa, coloque la capa de la derecha en el frente");
                    break;
                case 6:
                    System.out.println("Sin girar ninguna capa, coloque la capa de la izquierda en el frente");
                    break;
                case 7:
                    System.out.println("Sin girar ninguna capa, mantenga la capa del frente y rote el cubo 2 veces");
                    break;
                case 8:
                    System.out.println("Sin girar ninguna capa, mantenga la capa del frente y rote el cubo en el sentido de las agujas del reloj");
                    break;
                case 9:
                    System.out.println("Sin girar ninguna capa, mantenga la capa del frente y rote el cubo en el sentido contrario a las agujas del reloj");
                    break;
            }
            rotacionInicial /= 10;
        }

        for (int i = 0; i < 15; i++) {
            switch (solucion[i] % 10) {

                case 0:
                    break;
                case 1:
                    System.out.println("Gire la capa de la derecha 2 veces");
                    break;
                case 2:
                    System.out.println("Gire la capa de la derecha hacia arriba");
                    break;
                case 3:
                    System.out.println("Gire la capa de la derecha hacia abajo");
                    break;
                case 4:
                    System.out.println("Gire la capa superior 2 veces");
                    break;
                case 5:
                    System.out.println("Gire la capa superior hacia la izquierda");
                    break;
                case 6:
                    System.out.println("Gire la capa superior hacia la derecha");
                    break;
                case 7:
                    System.out.println("Gire la capa frontal 2 veces");
                    break;
                case 8:
                    System.out.println("Gire la capa frontal en el sentido de las agujas del reloj");
                    break;
                case 9:
                    System.out.println("Gire la capa frontal en el sentido contrario a las agujas del reloj");
                    break;
            }
        }
    }

    private void imprimirSolucionConNotacion() {

        System.out.println("");
        System.out.println("Solucion con notacion: \n");
        while (rotacionInicial > 0){
            switch (rotacionInicial % 10) {

                case 0:
                    break;
                case 1:
                    System.out.print("x2 ");
                    break;
                case 2:
                    System.out.print("x ");
                    break;
                case 3:
                    System.out.print("x' ");
                    break;
                case 4:
                    System.out.print("y2 ");
                    break;
                case 5:
                    System.out.print("y ");
                    break;
                case 6:
                    System.out.print("y' ");
                    break;
                case 7:
                    System.out.print("z2 ");
                    break;
                case 8:
                    System.out.print("z ");
                    break;
                case 9:
                    System.out.print("z' ");
                    break;
            }
            rotacionInicial /= 10;
        }

        for (int i = 0; i < 15; i++) {
            switch (solucion[i] % 10) {

                case 0:
                    break;
                case 1:
                    System.out.print("R2 ");
                    break;
                case 2:
                    System.out.print("R ");
                    break;
                case 3:
                    System.out.print("R' ");
                    break;
                case 4:
                    System.out.print("U2 ");
                    break;
                case 5:
                    System.out.print("U ");
                    break;
                case 6:
                    System.out.print("U' ");
                    break;
                case 7:
                    System.out.print("F2 ");
                    break;
                case 8:
                    System.out.print("F ");
                    break;
                case 9:
                    System.out.print("F' ");
                    break;
            }
        }
    }
}