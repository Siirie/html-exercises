from random import sample
#luokat 0-4, lkm 1-30. Tiedot tulee html formista
#data josta valitaan on /salat/rally_kyltit.csv
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

def choose_exe(luokat: tuple, lkm: int): #tulostaa tuloksen (nro, nimi)
    pool= get_pool(luokat)
    possibilities =[]
    #luokat numero vastaa rally_kyltit_kopio.txt tiedoston jokaisen rivin alussa olevia numeroita
    with open('salat/rally_kyltit_kopio.txt', 'r', encoding='utf-8') as kyltitfile:
        for row in kyltitfile:
            parts= row.split(';') #parts[0] on järjestysnumero
            #print(parts[0], parts[1], parts[2], parts[3], parts[4])
            #seuravaksi pistäisi lisätä rivit, jotka alkavat tietyillä nmeroilla possibilities listaan
            if int(parts[0]) in pool:
                possibilities.append(row.strip())
    
    
    choosen_exes=[]
    if len(possibilities) >= lkm:
        choosen_exes= sample(possibilities, lkm)
    else:
        choosen_exes=possibilities

    for exes in choosen_exes:
        
        parts= exes.split(';') #parts[0] on järjestysnumero
        print(parts[1], parts[2])    
    #0 = 2, 3
    # 1 = 4-39
    #2 = 40-64
    #3 = 65-90
    #4 = 91-112


if __name__ == "__main__":
    # Test the function with example inputs
    #luokat = (0, 1)
    lkm = 5
    #   print(choose_exe((0, 1), 3))  
    #choose_exe((0, 1), 1) #Kutsutaan siis vain choose_exe(luokat, lkm) 
    choose_exe((4, 1, 2), 10) 

    