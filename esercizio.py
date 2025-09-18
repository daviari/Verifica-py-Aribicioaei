tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    somma = 0
    media = 0
    conteggio = 0 
    
    for _,_,puntiSquadra,PuntiOspite in tupla_partite:
        somma=puntiSquadra+PuntiOspite+somma
        conteggio+=1
        print(conteggio)
    media=round(somma/conteggio,2)
    return media

def media_gol_squadra(tupla_partite,squadra_scelta):
    somma = 0 
    media = 0
    conteggio = 0
    
    for squadraCasa,squadraOspite,puntiSquadra,puntiOspite in tupla_partite:
        if(squadra_scelta.lower()==squadraCasa.lower()):
            print(f"partita tra {squadraCasa} e {squadraOspite}, la squadra {squadraCasa} ha fatto {puntiSquadra} goal ")
            somma+=puntiSquadra
            conteggio +=1
        elif (squadra_scelta.lower()==squadraOspite.lower()):
            print(f"partita tra {squadraCasa} e {squadraOspite}, la squadra {squadraOspite} ha fatto {puntiOspite} goal")
            somma+=puntiOspite
            conteggio +=1
    media=round(somma/conteggio,2)
    return media 
                
            
def partita_con_piu_gol(tupla_partite):
    
    somma_Max = 0 
    lista = []
    nome1 = ""
    nome2 = ""
    for squadraCasa,squadraOspite,puntiSquadra,PuntiOspite in tupla_partite:
        somma = 0 
        somma=puntiSquadra+PuntiOspite
        if(somma>somma_Max):
            somma_Max= somma
            nome1=squadraCasa
            nome2=squadraOspite
    lista.append(nome1)
    lista.append(nome2)
    lista.append(somma_Max)

    return lista
    
        
def percentuale_vittoria_squadra(tupla_partite,squadra_scelta):
    conteggio_vinte = 0
    conteggio = 0 
    percentuale = 0 
    for squadraCasa,squadraOspite,puntiSquadra,PuntiOspite in tupla_partite:
        if (squadra_scelta.lower()==squadraCasa.lower()):
            conteggio += 1
            if(puntiSquadra>PuntiOspite):
                conteggio_vinte += 1
        elif(squadra_scelta.lower()==squadraOspite.lower()):
                conteggio+=1 
                if(PuntiOspite>puntiSquadra):
                    conteggio_vinte +=1
    if conteggio == 0:
        print("ERRORE")
    else:
        percentule=(conteggio_vinte/conteggio)*100
        print(f"la percentuale delle vitotrie della {squadra_scelta} è {percentule}%")
    
               



while True:
    print("")
    print("MENU:")
    print("1.Media dei goal totali")
    print("2.Media goal della squadra scelta")
    print("3.Partita fatta con più goal")
    print("4.Percentuale della vittoria")
    print("0. Per concludere il ciclo")
    print("")
    scelta=int(input("Scegli quale funzione vuoi eseguire: "))
    if scelta == 0: 
        print("Ciclo terminato")
        break
    elif scelta == 1: 
        media = media_gol_partite(tupla_partite)
        if media == 0:
            print("ERRORE")
        else:
            print(f"La media dei goal di tutte le partite è {media}")
        
    elif scelta == 2: 
        squadra_scelta=str(input("Scegli una squadra:"))
        media=media_gol_squadra(tupla_partite,squadra_scelta)
        if media == 0:
            print("ERRORE")
        else:
            print(f"La squadra {squadra_scelta} ha fatto in media {media} goal ")
        
    elif scelta == 3: 
        lista= partita_con_piu_gol(tupla_partite)
        print(lista)

    elif scelta == 4:
        squadra_scelta = str(input("inserisci nome squadra: "))
        percentuale_vittoria_squadra(tupla_partite,squadra_scelta)
    else:
        print("ERRORE")
        
    