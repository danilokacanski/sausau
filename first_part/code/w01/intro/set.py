#%% md
# # Set
#%% md
# ## Inicijalizacija seta
#%%
# Kreiranje seta
moj_set = {1, 2, 3}
print("Set:", moj_set)

# Prazan set (mora set(), {} pravi dict)
prazan_set = set()
print("Prazan set:", prazan_set)
#%% md
# ## Duplikati i redosled
#%%
duplikati = {1, 2, 2, 3}
print("Bez duplikata:", duplikati)  # duplikati se automatski uklanjaju

neuredjen_set = {5, 2, 9, 1}
print("Redosled nije garantovan:", neuredjen_set)
#%% md
# ## Provera postojanja
#%%
skup = {10, 20, 30}
print(20 in skup)   # True
print(50 in skup)   # False
#%% md
# ## Dodavanje i uklanjanje
#%%
skup = {1, 2, 3}
skup.add(4)
print("Nakon add:", skup)

skup.update([5, 6])
print("Nakon update:", skup)

skup.remove(2)
print("Nakon remove:", skup)

# discard ne baca grešku ako element ne postoji
skup.discard(10)
print("Nakon discard:", skup)

skup.clear()
print("Prazan skup:", skup)
#%% md
# ## Iteracija
#%%
skup = {"a", "b", "c"}
for el in skup:
    print("Element:", el)
#%% md
# ## Tipične primene
#%%
# Uklanjanje duplikata iz liste
lista = [1, 2, 2, 3]
bez_duplikata = set(lista)
print("Bez duplikata:", bez_duplikata)
#%% md
# ## Skupovske operacije
#%%
a = {1, 2, 3}
b = {3, 4, 5}

print("Unija:", a | b)
print("Presek:", a & b)
print("Razlika (a - b):", a - b)
print("Simetrična razlika:", a ^ b)
#%% md
# ## Česte greške
#%%
skup = {1, 2, 3}

# remove baca grešku ako ne postoji
# skup.remove(10)  # Greška!

# discard ne baca grešku
skup.discard(10)