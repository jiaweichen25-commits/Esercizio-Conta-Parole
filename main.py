file = input("immetere i percorso file: ")

def robe(file):
    lista1 = []
    punti1 = []
    parole = []
    with open(file, "r") as fil:
        contenuto = fil.read()
    #parole = contenuto.split()
    for x in contenuto.split():
        if x.isalpha():
            parole.append(x)
    for x in contenuto:
        if x == " ":
            lista1.append(x)
        elif x == ".":
            punti1.append(x)
    return lista1, punti1, parole

lista1, punti1, parole = robe(file)
print("il numero di spazi è:", len(lista1))
print("il numero dei punti è : ", len(punti1))
print("I numeri delle parole sono:", len(parole))
print("La parola più lunga è: ", max(parole, key=len))#serza key=len prende le parole in ordine alfabetico
print("La parola più corta è : ", min(parole, key=len))





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

