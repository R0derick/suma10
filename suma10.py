import random   # Importar llibreria random per crear els números de la llista aleatoris.
import os       # Importar llibreria os per netejar la pantalla i deixar el codi més net.
import joc      # Importar joc per comprovar que no queden mes caslles disponibles al tauler.

def clear():                # Defineix funció per netejar la pantalla.
    if os.name == "nt":     # Si el sistema operatiu es Windows ejecuta "cls".
        os.system("cls")    # Windows.
    else:                   # Si el sistema operatiu es GNU/Linux ejecuta "clear".
        os.system("clear")  # Linux.

def parar():                # Funció per parar el joc i continuar pressionant el espai.
    stop = input('')

final_joc = True            # Inici del joc.
while final_joc:            # Metre el joc sigiu True.
    clear()                 # Ejecuta la funció per netejar la pantalla.
    print('************************************')
    print('Començant nova partida...')
    JUGADOR1= input('Introdueix el nom del jugador 1: ')    # Demana el nom dels jugadors a l'usuari.
    JUGADOR2= input('Introdueix el nom del jugador 2: ')
    print('************************************')

    ################# DEFINCIÓ VARIABLES I CONSTANTS #########
    DEFAMPLADA = 20  #Amplada a modificar.    MAX: 99
    DEFALTURA = 20   #Altura a modificar.     MAX: 99

    UTILITZADA = 'X'                        # Signe que substituira les caselles utilitzades.
    punts = [0, 0]  #JUGADOR1, JUGADOR2     # Punts de cada jugador.
    AMPLADA = range(1, DEFAMPLADA+1)        # Números del 1 fins a l'amplada definida.
    ALTURA = range(1, DEFALTURA+1)          # Números del 1 fins a l'altura definida.
    posibles_caselles = []                  # Caselles que estan a prop de la primear introduida i pot seleccionar l'usuari.
    ########################################################

    ########################## CREACIÓ LLISTES ############################
    llista = []     #Els valors del tauler es guardaran de la seguent forma: llista[Número_de_fila][Número_de_columna]                                                                         

    for element in range(DEFALTURA):                # Entra al bucle el nombre de cop que hi ha a DEFALTURA
        subllista = []                              # Crea una llista vuida
        for i in range(DEFAMPLADA):                 # Per cada element del 0 al número que hi ha a DEFAMPLADA-1
            subllista.append(random.randint(1, 9))  # Agrega un valor a la llista creada
        llista.append(subllista)                    # Agrega la llista creada al bucle a una llista de llistes.
    #########################################################################

    ######################### CREACIÓ TAULER #################################
    #Creació llistes amb nom llista+num del 1 fins al últim de la constant ALTURA
    def tauler():   #Funció sense parametres per crear el tauler i ordenar millor el programa
        print('')
        if DEFALTURA >= 10:
            print('', end='    ')
        else:
            print('', end='   ')

        for num in AMPLADA:
            if num >= 10:
                print(num, end=' ')
            else:
                print(num, end='  ')
        print('')

        if DEFALTURA >= 10:
            print('', end='   ')
        else:
            print('', end='  ')

        for num in AMPLADA:
            print('', end='---')
        print('')

        for numAlt in ALTURA:
            if DEFALTURA >= 10:
                if numAlt <= 9:
                    print(numAlt, ' |', end='')
                else:
                    print(numAlt, '|', end='')
            else:
                print(numAlt, '|', end='')

            for element in llista[numAlt-1]:
                print(element, end='  ')
            print('')

    ###############################################################             # Comença partida
    
    torn = JUGADOR1                 # Torn del jugaador actual
    moviments = True                # Mentre sigui True continuarà la partida, hi ha caselles que poden sumar 10.
    final_partida = True            # si final_partida es fals no entrara al seguent bucle i s'acabara el joc.
    while final_partida:

        if torn == JUGADOR1:                            # Si el torn es del JUGADOR1:
            print(f'És el torn de: {JUGADOR1}')
            print(f'Punts de {JUGADOR1}: {punts[0]}')
            print(f'Punts de {JUGADOR2}: {punts[1]}')
        else:                                           # Si el torn es del JUGADOR2:
            print(f'És el torn de: {JUGADOR2}')
            print(f'Punts de {JUGADOR1}: {punts[0]}')
            print(f'Punts de {JUGADOR2}: {punts[1]}')

        tauler()                                        # Ejecuta la funció que crea el tauler.
        print('')                                       # Escriu un enter.

        totes_posibles_caselles = []                    # Totes les caselles que estan al voltant de les caselles seleccionades, per tant, poden també ser seleccionades.
        caselles_utilitzades = 0                        # Contador per saber quantes caselles s'han utilitzat per sumar 10.
        SUMA = 0                                        # Guarda el valor de la suma de totes les caselles seleccionades de la partida actual.
        intent = 1                                      # Aquesta variable serveix per solucionar un error a l'hora de comprovar les caselles properes.
        utilitzades_temp = []                           # Caselles que no es poden utilitzar perque s'han utilitzat en el mateix torn.
        final_torn = True                               # Bolea que indica si el torn a acabat o continua.
        while final_torn:                               # Mentre final_torn sigui verdader.
            if moviments:                               # Si hi queden moviments.
                no_error = True                         # Variable per definir si hi ha errors.

                fila = int(input(f'Introdueix fila (1-{DEFALTURA}): '))                     # Demana a l'usuari quina fila vol seleccionar
                columna = int(input(f'Introdueix colu (1-{DEFALTURA}): '))                  # Demana a l'usuari quina columna vol seleccionar


                ############################ 1r PUNT #################################
                if fila < 1 or fila > DEFALTURA or columna < 1 or columna > DEFALTURA:      # Si la casella seleccionada esta fora del tauler:
                    print('ERROR: La casella esta fora del tauler, torna a intentar-ho.')   # Imprimeix l'error.
                ######################################################################      # Si no hi ha cap error, continua.
                else:                                                       
                ############################ 2n PUNT #################################
                    if llista[fila-1][columna-1] == UTILITZADA:                                                 # Si la casella guarda una "X" es que ja s'ha fet servir          
                        print("ERROR: La casella ja s'ha seleccionat anteriorment, torna a intentar-ho.")       # Imprimeix l'error
                ######################################################################
                    else:
                ############################ 3r PUNT #################################
                        if (fila, columna) in utilitzades_temp:                                                 # Si la casella s'ha utilitzat en aquest torn
                            print("ERROR: La casella ja s'ha utilitzat en aquest torn, torna a intentar-ho.")   # Imprimeix l'error
                ######################################################################
                        else:
                ############################ 4t PUNT #################################
                            if intent == 1:                                                                     # Si es la primear veguada
                                posibles_caselles = [(fila-1, columna-1),(fila-1, columna),(fila-1, columna+1),(fila, columna-1),(fila, columna+1),(fila+1, columna-1),(fila+1, columna),(fila+1, columna+1)]
                                totes_posibles_caselles = posibles_caselles.copy()  # Guarda a posibles_caselles les posibles caselles que es poden seleccionar despres de seleccionar la primera i en fa una copa a totes_posibles_caselles
                                intent = 2                                          # Guarda el 2 a intent perque no ejecuta el else.
                                                                                    # La primera casella que es seleccioni no ha d'estar a prop de cap, només ha de ser vàlida.
                            else:                                                  # Si no es primera vegada s'introdueix una casella
                                if (fila, columna) not in totes_posibles_caselles:  # Si la última casella introduida no esta a totes_posibles_caselles vol dir que s'ha introduit una casella fora de rang.
                                    print("ERROR: La casella no es veïna d'alguna de les caselles seleccionades, es perd el torn.")

                                    if torn == JUGADOR1:                            # Es perd el torn i el torn de jugador
                                        torn = JUGADOR2
                                    else:
                                        torn = JUGADOR1

                                    parar()                                         # Atura el programa perque es pugui veure l'error.
                                    no_error = False                                # Guarda a no_error = False perque no continui amb el programa i torni a començar el while
                                    final_torn = False                              # Guarda final_torn = False per tornar a començar un altre torn amb l'altre usuari
                                    clear()

                                posibles_caselles = [(fila-1, columna-1),(fila-1, columna),(fila-1, columna+1),(fila, columna-1),(fila, columna+1),(fila+1, columna-1),(fila+1, columna),(fila+1, columna+1)]
                                totes_posibles_caselles = totes_posibles_caselles + posibles_caselles.copy()    # Guarda les posibles caselles del última casella introduida
                ######################################################################                          # I les suma a totes les caselles introduides, aquesta llista es reinicia quan s'acaba el torn.
                            if no_error:                                                        # Si no hi ha hagut cap error
                                correcte = False                                                # Guarda False fins que el torn no s'hagui acabat sumant 10.
                                SUMA += llista[fila-1][columna-1]                               # Guarda a la variable SUMA el valor de SUMA + el valor de la casella actual.
                                caselles_utilitzades += 1                                       # Augmenta un valor les caselles_utilitzades per comptar quantes caselles s'han utilitzat per sumar 10.
                                if SUMA > 10:                                                   # Si la suma es superior a 10 es perd el torn.
                                    print('ERROR: La suma és superior a 10, es perd el torn.')  # Imprimeix l'error
                                    parar()                                                     # Es para el programa per poder veure l'error
                                    clear()                                                     # Borra la pantalla
                                    final_torn=False
                                    
                                    if torn == JUGADOR1:                                        # Es perd el torn i el torn de jugador
                                        torn = JUGADOR2
                                    else:
                                        torn = JUGADOR1

                                elif SUMA < 10:                                                 # Si la suma es menor a 10 la partida continua.
                                    print(f'Fins ara les caselles sumen {SUMA}.')               # Imprimeix el valor de la suma
                                else:                                                           # Si la SUMA = 10
                                    print(f'Molt bé, sumen {SUMA}. Es passa el torn')           # El torn ha finalitzat.
                                    print('************************************')
                                    correcte = True                                             # Canvia el valor de correcte a True perque es canvin les caselles a UTILITZADA i es sumin els punts.
                                utilitzades_temp.append((fila, columna))                        # Guarda la casella actual a utilitzades_temp que son les caselles que s'han utilitzat en aquest torn.

                                if correcte:                                                    # Si el torn ha acabat correctament.
                                    for casella in utilitzades_temp:                            # Per cada casella del torn actual
                                        llista[casella[0]-1][casella[1]-1] = UTILITZADA         # Substitueix el número que hi ha per UTILITZADA

                                    moviments = joc.existeix_mov(DEFALTURA, DEFAMPLADA, SUMA, UTILITZADA, llista)   # Comprova si queden moviments lliures.

                                    if caselles_utilitzades == 2:       # Si s'utilitzen 2 caselles els punts a sumar son 2
                                        punts_sumar = 2
                                    elif caselles_utilitzades == 3:     # Si s'utilitzen 3 caselles els punts a sumar son 4
                                        punts_sumar = 4
                                    elif caselles_utilitzades == 4:     # Si s'utilitzen 4 caselles els punts a sumar son 5
                                        punts_sumar = 5
                                    elif caselles_utilitzades == 5:     # Si s'utilitzen 5 caselles els punts a sumar son 7
                                        punts_sumar = 7
                                    else:                               # Si les caselles que s'han utilitzat son 6 o mes es suma la quantitat de les caselles + 3
                                        punts_sumar = caselles_utilitzades + 3
                                    
                                    if torn == JUGADOR1:                # Si el torn actual es del JUGADOR1
                                        punts[0] += punts_sumar         # Suma els punts del torn actual al contador
                                        torn = JUGADOR2                 # Canvia el torn de jugador
                                    else:                               # Si el torn actual es del JUGADOR2
                                        punts[1] += punts_sumar         # Suma els punts del torn actual al contador del JUGADOR2
                                        torn = JUGADOR1                 # Canvia el torn de jugador

                                    final_torn = False                  # Guarda false a final_torn perque s'ha acabat el torn correctament.
                                    parar()
                                    clear()
            else:                                                       # Si no queden moviments al tauler
                print('********* No hi ha més moviments. Partida finalitzada. **********')
                print(f'Punts de {JUGADOR1}: {punts[0]}')               # Imprimeix els punts del JUGADOR1
                print(f'Punts de {JUGADOR2}: {punts[1]}')               # Imprimeix els punts del JUGADOR2
                if punts[0] > punts[1]:                                 # Si els punts del JUGADOR1 són superiors al JUGADOR2, el guanyador es el JUGADOR1
                    print(f'El guanyador és: {JUGADOR1}')               # Imprimeix el guanyador
                elif punts[0] < punts[1]:                               # Si els punts del JUGADOR2 són superiors al JUGADOR1, el guanyador es el JUGADOR2
                    print(f'El guanyador és: {JUGADOR2}')               # Imprimeix el guanyador
                else:                                                   # Si els punts dels 2 jugadors són iguals
                    print('Empat.')                                     # Imprimeix el resultat

                tornar_jugar = input('\nVols tornar a jugar (s/n): ')   # Pregunta a l'usauri si vol tornar a jugar 
                if tornar_jugar == 'n':                                 # Si no vol jugar s'ha de sortir de tots els bucles i acabara el joc
                    final_joc = False
                    final_torn = False
                    final_partida = False
                else:                                                   # Si vol continuar jugant s'ha de sortir fins al primer bucle while que inicia la partida.
                    final_torn = False
                    final_partida = False
                    clear()
print('Sortint del joc...')