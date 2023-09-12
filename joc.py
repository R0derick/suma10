ALTURA=0
AMPLADA=0
SUMA=0
UTILITZADA=""
tauler=[]

def existeix_mov(alt, ampl, suma, util, taul):
    global ALTURA, AMPLADA, SUMA, UTILITZADA, tauler
    ALTURA=alt
    AMPLADA=ampl
    SUMA=suma
    UTILITZADA=util
    tauler=taul
    
    for i in range(ALTURA):
        for j in range(AMPLADA):
            if tauler[i][j]!=UTILITZADA:
                veines_ok=[[i,j],]
                valor_acum=tauler[i][j]
                es_suma_ok, valor_acum=tractar_veines(i, j, veines_ok, valor_acum)
                if es_suma_ok:
                    #print ("Caselles que sumen",str(valor_acum),":",veines_ok)
                    return True
    return False
      
def obtenir_veines(i, j, veines_ok, valor_acum):
    '''
    i-1,j-1   i-1,j   i-1,j+1
    i,j-1       i,j     i,j+1
    i+1,j-1   i+1,j   i+1,j+1
    '''
    veines=[]

    if i==0:
        if j==0:
            veines.extend([\
                          [i,j+1],\
                          [i+1,j], [i+1,j+1]])
        elif j==AMPLADA-1:
            veines.extend([\
                          [i,j-1],\
                          [i+1,j-1], [i+1,j]])        
        else:
            veines.extend([\
                          [i,j-1], [i,j+1],\
                          [i+1,j-1], [i+1,j], [i+1,j+1]])
    elif i==ALTURA-1:
        '''
        i-1,j-1   i-1,j   i-1,j+1
        i,j-1       i,j     i,j+1
        i+1,j-1   i+1,j   i+1,j+1
        '''
        if j==0:
            veines.extend([[i-1,j], [i-1,j+1],\
                          [i,j+1]\
                          ])
            
        elif j==AMPLADA-1:
            veines.extend([[i-1,j-1], [i-1,j],\
                           [i,j-1]\
                           ])        
        else:
            veines.extend([[i-1,j-1], [i-1,j], [i-1,j+1],\
                           [i,j-1], [i,j+1]\
                           ])
    elif j==0:
        veines.extend([[i-1,j], [i-1,j+1],\
                       [i,j+1],\
                       [i+1,j], [i+1,j+1]])
    elif j==AMPLADA-1:
        veines.extend([[i-1,j-1], [i-1,j],\
                       [i,j-1],\
                       [i+1,j-1], [i+1,j]])      
    else:
        veines.extend([[i-1,j-1], [i-1,j], [i-1,j+1],\
                       [i,j-1], [i,j+1],\
                       [i+1,j-1], [i+1,j], [i+1,j+1]])
    
    #print("Llista de veines abans de filtratge: ", veines)
    
    #Filtrar caselles veïnes. Per evitar bucles treure de les veines
    #les que són ok (tractades anteriorment)
    veines_res=[]
    if len(veines_ok)>0:
        try:
            for pos in range(len(veines)):
                valor_casella=tauler[veines[pos][0]][veines[pos][1]]
                if valor_casella==UTILITZADA:
                    #Descartar veina
                    continue
                elif valor_casella + valor_acum > SUMA:
                    #Descartar veina
                    continue
                else:
                    descartar=False
                    for veina_ok in veines_ok:
                        if veina_ok[0]==veines[pos][0] and veina_ok[1]==veines[pos][1]:
                            #Veina ja tractada, descartar
                            descartar=True
                    if not descartar:
                        #Afegeixo la veina actual
                        veines_res.extend([[veines[pos][0],veines[pos][1]]])        
        except(IndexError):
            #Error: IndexError: list index out of range
            print("Avisa el professor que hi ha hagut un IndexError a obtenir_veines().")
        except(TypeError):
            #ERROR: 'int' object is not subscriptable
            print("Avisa el professor que hi ha hagut un TypeError a obtenir_veines().")
    
    return veines_res

def tractar_veines(i, j, veines_ok, valor_acum):
    veines=obtenir_veines(i, j, veines_ok, valor_acum)
    
    if len(veines)==0:
        return False, 0
    else:
        for pos in range(len(veines)):
            try:
                valor_veina=tauler[veines[pos][0]][veines[pos][1]]
                if valor_veina + valor_acum == SUMA:
                    #print("Trobat. Valors:",valor_veina,"i",valor_acum)
                    veines_ok.extend([[veines[pos][0],veines[pos][1]]])
                    return True, valor_veina + valor_acum
                elif valor_veina + valor_acum < SUMA:
                    #Afegeixo la veina actual
                    veines_ok.extend([[veines[pos][0],veines[pos][1]]])
                    #Crida recursiva
                    return tractar_veines(veines[pos][0], veines[pos][1], veines_ok, valor_veina+valor_acum)
                else: #?? No hauria de passar
                    return False, valor_veina + valor_acum
            except(TypeError):
                #ERROR: unsupported operand type(s) for +: 'int' and 'str'
                print("Avisa el professor que hi ha hagut un TypeError a tractar_veines().")
