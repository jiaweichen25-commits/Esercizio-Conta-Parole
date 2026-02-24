file = input("immetere i percorso file: ")

def robe(file):
    lista1 = []
    punti1 = []
    with open(file, "r") as fil:
        contenuto = fil.read()
    for x in contenuto:
        if x == " ":
            lista1.append(x)
        elif x == ".":
            punti1.append(x)
    return lista1, punti1

lista1, punti1 = robe(file)
print("il numero di spazi è:", len(lista1))
print("il numero dei punti è : ", len(punti1))




'''file = input("Immettere il percorso file: ")

def robe(file):
    lista1 = []
    with open(file, "r") as f:
        contenuto = f.read()
    for x in contenuto:
        if x == " ":
            lista1.append(x)
    return lista1

num_spazi = (len(robe(file)))
print("il numero di spazi è: ", num_spazi)'''

