#%% md
# # Zadaci za vezbu
#%% md
# ## Zadatak 1. - Da li niz sadrži duplikat? (LeetCode ID: 217)
#%%
def sadrziDuplikat1(nums):
    # Koristimo set da pratimo već viđene brojeve
    vidjeni = set()
    for broj in nums:
        if broj in vidjeni:
            return True
        vidjeni.add(broj)
    return False
#%%
def sadrziDuplikat2(nums):
    return len(nums) != len(set(nums))
#%%
# Primer 1
print(sadrziDuplikat1([1, 2, 3, 1]))

# Primer 2
print(sadrziDuplikat1([1, 2, 3, 4]))

# Primer 3
print(sadrziDuplikat1([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
#%% md
# ## Zadatak 2. - Da li je reč anagram? (LeetCode ID: 242)
#%%
def daLiJeAnagram(s, t):
    # Anagram ima ista slova u istom broju — možemo uporediti sortirane verzije
    return sorted(s) == sorted(t)
#%%
# Primer 1
print(daLiJeAnagram("anagram", "nagaram"))

# Primer 2
print(daLiJeAnagram("rat", "car"))
#%% md
# ## Zadatak 3. - Sortiraj parne i neparne indekse (LeetCode ID: 2164)
#%%
def sortirajParneNeparneIndekse(nums):
    parni = sorted([nums[i] for i in range(0, len(nums), 2)])
    neparni = sorted([nums[i] for i in range(1, len(nums), 2)], reverse=True)

    rezultat = [0] * len(nums)
    rezultat[::2] = parni       # parni indeksi
    rezultat[1::2] = neparni    # neparni indeksi

    return rezultat
#%%
# Primer 1
print(sortirajParneNeparneIndekse([4, 1, 2, 3]))

# Primer 2
print(sortirajParneNeparneIndekse([2, 1]))

# Dodatni primer
print(sortirajParneNeparneIndekse([9, 7, 8, 6, 5, 4]))
#%% md
# ## Zadatak 4. - Sortiraj niz po parnosti (LeetCode ID: 905)
#%%
def sortirajPoParnosti(nums):
    parni = [x for x in nums if x % 2 == 0]
    neparni = [x for x in nums if x % 2 == 1]
    return parni + neparni
#%%
# Primer 1
print(sortirajPoParnosti([3, 1, 2, 4]))

# Primer 2
print(sortirajPoParnosti([0]))

print(sortirajPoParnosti([7, 2, 6, 3, 9, 4]))
#%% md
# ## Zadatak 5. - Relativni plasmani takičara (LeetCode ID: 506)
#%%
def relativniPlasmani(score):
    n = len(score)
    # Sačuvamo i indeks kako bismo znali gde da vratimo rezultat
    sortirani = sorted(enumerate(score), key=lambda x: -x[1])
    rezultat = [''] * n

    for i, (indeks, _) in enumerate(sortirani):
        if i == 0:
            rezultat[indeks] = "Gold Medal"
        elif i == 1:
            rezultat[indeks] = "Silver Medal"
        elif i == 2:
            rezultat[indeks] = "Bronze Medal"
        else:
            rezultat[indeks] = str(i + 1)

    return rezultat
#%%
# Primer 1
print(relativniPlasmani([5, 4, 3, 2, 1]))

# Primer 2
print(relativniPlasmani([10, 3, 8, 9, 4]))

# Dodatni primer
print(relativniPlasmani([99]))