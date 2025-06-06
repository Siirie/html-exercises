import pyjokes
from random import sample
from pyweb import pydom

def get_smthing(event):
    pydom["div#jokes"].html = f"{pyjokes.get_joke()} 🥁"

def get_rally(event):
    pydom["div#rally"].html = "Rally data will be fetched here."

def get_pool(luokat: tuple):
    #luokat numero vastaa rally_kyltit_kopio.txt tiedoston jokaisen rivin alussa olevia numeroita
    pool = []
    try:
        for luokka in range(luokat):
            if luokka == 0:
                pool.extend(range(2, 4))  # 2-3
            elif luokka == 1:
                pool.extend(range(4, 40))  # 4-39
            elif luokka == 2:
                pool.extend(range(40, 65))  # 40-64
            elif luokka == 3:
                pool.extend(range(65, 91))  # 65-90
            elif luokka == 4:
                pool.extend(range(91, 113))  # 91-112
    except:
        for luokka in luokat:
            if luokka == 0:
                pool.extend(range(2, 4))  # 2-3
            elif luokka == 1:
                pool.extend(range(4, 40))  # 4-39
            elif luokka == 2:
                pool.extend(range(40, 65))  # 40-64
            elif luokka == 3:
                pool.extend(range(65, 91))  # 65-90
            elif luokka == 4:
                pool.extend(range(91, 113))  # 91-112
    else:
        print("erroria pukkaa")
    return pool

def choose_exe(event): #tulostaa tuloksen (nro, nimi)
    luokat = (1, 2)
    lkm= 3
    pool= get_pool(luokat)
    possibilities =[
(118, "NORMAALIKÄYNTIÄ"),
(205, "ISTU, SEISO"),
(103, "ISTU, KIERRÄ KOIRA")]
    
    """
    #luokat numero vastaa rally_kyltit_kopio.txt tiedoston jokaisen rivin alussa olevia numeroita
    with open('salat\rally_kyltit_kopio.txt', 'r', encoding='utf-8') as kyltitfile:
        for row in kyltitfile:
            parts= row.split(';') #parts[0] on järjestysnumero
            #print(parts[0], parts[1], parts[2], parts[3], parts[4])
            #seuravaksi pistäisi lisätä rivit, jotka alkavat tietyillä nmeroilla possibilities listaan
            if int(parts[0]) in pool:
                possibilities.append(row.strip())
    """
    
    choosen_exes=[]
    if len(possibilities) >= lkm:
        choosen_exes= sample(possibilities, lkm)
    else:
        choosen_exes=possibilities

    for exes in choosen_exes:
        
        parts= exes #.split(';') #parts[0] on järjestysnumero
        pydom["div#rally2"].html = f"{parts}"