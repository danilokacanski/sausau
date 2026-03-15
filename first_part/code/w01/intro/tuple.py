#%% md
# # Tuple
#%% md
# ## Inicijalizacija tuple
#%%
koordinate = (4, 7)
print("Tuple:", koordinate)
print("Tip:", type(koordinate))
#%%
prazan_tuple = ()
print("Prazan tuple:", prazan_tuple)
#%% md
# ## Pristup i sečenje
#%%
print("Prvi element:", koordinate[0])
print("Poslednji element:", koordinate[-1])
print("Prva dva:", koordinate[0:2])
print("Obrnuti redosled:", koordinate[::-1])
#%% md
# ## Korisne funkcije
#%%
print("Broj elemenata:", len(koordinate))
print("Najmanji element:", min(koordinate))
print("Najveći element:", max(koordinate))
#%% md
# ## Iteracija i primene
#%%
for x in koordinate:
    print("Element:", x)
#%%
for i in range(len(koordinate)):
    print("Indeks:", i, "Vrednost:", koordinate[i])
#%%
def vrati_par():
    return (1, 2)
#%%
print("Tuple iz funkcije:", vrati_par())
#%% md
# ## Pretvaranje i česte greške
#%%
lista = [1, 2, 3]
t = tuple(lista)
print("Lista u tuple:", t)
#%%
t2 = (1, 2, 3)
l = list(t2)
print("Tuple u listu:", l)
#%%
try:
    t2[0] = 10
except TypeError as e:
    print("Greška:", e)