tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 260)),
        ("marzo", ("gas", 130)),
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 260)),
        ("marzo", ("gas", 130)),
    ]),
    ("Roma", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 260)),
        ("marzo", ("gas", 130)),
    ]),
)

def analizza_consumi_energetici (tupla_consumi_energetici,scelta_nome,scelta_tipo):
    somma = 0 
    media = 0 
    conteggio = 0 
    max_Consumo = 0 
    max_Mese = 0 
    for nome,*inventario in tupla_consumi_energetici:
        for mese,prodotto in inventario:
            tipo,consumo= prodotto
            if scelta_nome.lower()== nome.lower() and scelta_tipo.lower() == tipo.lower() :
                somma+=consumo
                conteggio+=1
                if(consumo>max_Consumo):
                    max_Consumo = consumo
                    max_Mese = mese 
    media=round(somma/conteggio,2)
    print(f"la media della risorsa è {media}. Il massimo consumo è di {max_Consumo} avvenuto nel mese di {max_Mese}")           



scelta_nome=str(input("Scegli il nome della città "))
scelta_tipo=str(input("Scegli tra (gas o elettrico): "))
analizza_consumi_energetici (tupla_consumi_energetici,scelta_nome,scelta_tipo)

