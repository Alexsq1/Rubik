import time

import Cubo_string

def distribucion():

    ini = Cubo_string.solved_state()

    #Crear lista de conjuntos. Guardan CADENAS (hashables)
    states = [{ini}, set()]

    #Cargar S0 y S1. Son "irregulares", el resto son uniformes
    for i in Cubo_string.adj_static(ini):
        states[-1].add(i)

    i = 1
    print("Capa", "0", ": ", "1", " estado")

    #Mientras el nuevo no esté vacío
    while states[-1]:

        #Añadir conjunto nuevo. Iterar sobre conjunto más nuevo
        states.append(set())
        for opt in states[-2]:

            #Iterar sobre los adyacentes (los nuevos que se están generando)
            for adj in Cubo_string.adj_static(opt):

                #Si no está en los conjuntos posibles:
                if not(adj in states[-1] or adj in states[-2] or adj in states[-3]):

                    #Añadir a nuestro conjunto la posición
                    states[-1].add(adj)


        print("Capa ", i, ": ", len(states[-2]), "estados")
        i += 1

def generar_combinaciones():

#Código que imprime todas las combinaciones por capas

    t_inicial = time.time()



    ini = Cubo_string.solved_state()

    #Crear lista de conjuntos. Guardan CADENAS (hashables)
    states = [{ini}, set()]

    mezclas = [{""}, set()]

    estado_a_mezcla = {}
    estado_a_mezcla[ini] = ""

    #Cargar S0 y S1. Son "irregulares", el resto son uniformes
    i = 0
    for adj in Cubo_string.adj_static(ini):

        states[-1].add(adj)
        recup_mezcla = estado_a_mezcla[ini]
        mezcla_act = recup_mezcla + Cubo_string.mov_por_numero(i)

        mezclas[-1].add(mezcla_act)
        estado_a_mezcla[adj] = mezcla_act

        i += 1

    print("Capa", "0", ": ", "1", " estado")

    capa = 1



    #Mientras el nuevo no esté vacío
    while states[-1]:

        #Añadir conjunto nuevo. Iterar sobre conjunto más nuevo
        states.append(set())
        mezclas.append(set())

        for opt in states[-2]:

            i = 0

            #Iterar sobre los adyacentes (los nuevos que se están generando)
            for adj in Cubo_string.adj_static(opt):

                #Si quisieras probar con la misma capa: saltar -> empeora 5 segundos

                # if estado_a_mezcla[opt][-3] == Cubo_string.mov_por_numero(i)[-3]:
                #     i += 1
                #     continue


                #Si no está en los conjuntos posibles:
                if not(adj in states[-1] or adj in states[-2] or adj in states[-3]):

                    #Añadir a nuestro conjunto la posición
                    states[-1].add(adj)

                    recup_mezcla = estado_a_mezcla[opt]
                    mezcla_act = recup_mezcla + Cubo_string.mov_por_numero(i)

                    mezclas[-1].add(mezcla_act)
                    estado_a_mezcla[adj] = mezcla_act

                i += 1


        print("\nCapa ", capa, ": ", len(states[-2]), "estados")

        for m in mezclas[-2]:
            print(m)

        capa += 1
