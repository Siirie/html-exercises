
""""
#kirjoita ohjelma, joka lisää jokaisen rivin alkuun järjestysnumeron alkaen 1
with open('salat/rally_kyltit_kopio.txt', 'r') as file:
    lines = file.readlines()
with open('salat/rally_kyltit_kopio.txt', 'w') as file:
    for i, line in enumerate(lines, start=1):
        file.write(f"{i};{line}")  # Add the line number at the beginning of each line
"""

with open('salat/rally_kyltit_kopio.txt', 'r') as file:
    for row in file:
        # Process each row in the file
        parts= row.split(';')
        print(parts[0], parts[1], parts[2], parts[3], parts[4]) 
        #0 = kyltin järjestysnro, #1 = kyltin nro 2 nimi 3 suorituspaikkau 4 kuvaus
