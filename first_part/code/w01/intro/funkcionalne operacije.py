#%% md
# # Funkcionalne operacije nad kolekcijama
#%% md
# ## Lambda funkcija
#%%
# Lambda funkcija koja sabira 1 na dati broj
f = lambda x: x + 1
print(f(5))  

# Isto kao:
def f2(x):
    return x + 1
print(f2(5)) 
#%% md
# ## map()
#%%
brojevi = [1, 2, 3, 4]
kvadrati = list(map(lambda x: x**2, brojevi))
print(kvadrati)
#%% md
# ## filter()
#%%
brojevi = [1, 2, 3, 4, 5]
parni = list(filter(lambda x: x % 2 == 0, brojevi))
print(parni)
#%% md
# ## sorted()
#%%
parovi = [(7, 'a'), (2, 'c'), (18, 'b')]
sortirani = sorted(parovi, key=lambda x: x[1])
print(sortirani)
#%% md
# ## zip()
#%%
imena = ['Ana', 'Marko', 'Ivana']
godine = [23, 30, 27]
spojeno = list(zip(imena, godine))
print(spojeno)
#%% md
# ## enumerate()
#%%
imena = ['Ana', 'Marko', 'Ivana']
for i, ime in enumerate(imena):
    print(f"{i}: {ime}")