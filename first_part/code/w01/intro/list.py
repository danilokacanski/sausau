#%% md
# # Liste
#%% md
# ## Primer liste i osnovne osobine
#%%
niz = [4, 7, 1, 9]
print("Lista:", niz)
print("Tip:", type(niz))
print("Prvi element:", niz[0])
print("Poslednji element:", niz[-1])
print("Duplikati su dozvoljeni:", [1, 1, 2])
print("Ugnježdene liste:", [1, [2, 3]])
#%% md
# ## Pristup i izmena
#%%
print("Element na indeksu 2:", niz[2])
niz[2] = 10
print("Izmenjena lista:", niz)
#%% md
# g## Dodavanje i uklanjanje elemenata
#%%
niz.append(5)
print("Dodajemo 5:", niz)
niz.insert(1, 6)
print("Ubacujemo 6 na poziciju 1:", niz)
niz.extend([7, 8])
print("Dodajemo više elemenata:", niz)
#%%
niz.pop()
print("Uklanjamo poslednji element:", niz)
niz.remove(6)
print("Uklanjamo vrednost 6:", niz)
del niz[1]
print("Brišemo element na poziciji 1:", niz)
#%% md
# ## Slicing
#%%
print("Prva dva elementa:", niz[:2])
print("Svaki drugi element:", niz[::2])
print("Obrnuta lista:", niz[::-1])
#%% md
# ## Korisne funckije
#%%
print("Dužina:", len(niz))
print("Najmanji:", min(niz), "Najveći:", max(niz))
print("Zbir:", sum(niz))
print("Broj pojavljivanja broja 4:", niz.count(4))
#%% md
# ## Iteracija
#%%
print("Pristup elementima direktno:")
for x in niz:
    print(x)
#%%
print("Pristup sa indeksom:")
for i in range(len(niz)):
    print(f"Indeks {i}: vrednost {niz[i]}")
#%% md
# ## Tipicne primene
#%%
print("Maksimum:", max(niz))
print("Građenje DP tabele:")
n = 5
dp = [0] * (n + 1)
print(dp)
#%% md
# ## Greske i saveti
#%%
try:
    print(niz[100])  # IndexError
except IndexError as e:
    print("Greška:", e)
#%%
niz_kopija = niz.copy()
print("Kopirana lista:", niz_kopija)
#%%
niz_fiksna = [0] * 10
print("Fiksna dužina:", niz_fiksna)