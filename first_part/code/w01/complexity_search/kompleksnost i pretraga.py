#%% md
# # Kompleksnost i pretraga
#%% md
# ## Vreme i inicijalizacija velikih nizova
#%%
import time
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print(f"Vreme: {end - start:.10f} sekundi")
#%%
import random

n = 10_000  # broj elemenata
small_random_list = [random.randint(0, 1_000_000) for _ in range(n)]
#%%
n = 1_000_000  # broj elemenata
big_random_list = [random.randint(0, 1_000_000) for _ in range(n)]
#%% md
# ## Kompleksnost
#%% md
# ### O(1)
#%%
def prvi_element(niz):
    return niz[0]
#%%
print("Test sa malim nizom:")
measure_time(prvi_element, small_random_list)

print("Test sa velikim nizom:")
measure_time(prvi_element, big_random_list)
#%% md
# ### O(log n)
#%%
def deljenje_sa_dva(n):
    while n > 1:
        n = n // 2
#%%
print("Test logaritamske složenosti sa malim n:")
measure_time(deljenje_sa_dva, len(small_random_list))

print("Test logaritamske složenosti sa velikim n:")
measure_time(deljenje_sa_dva, len(big_random_list))
#%% md
# ### O(n)
#%%
def ispis(n):
    for i in range(n):
        pass
#%%
print("Test linearne složenosti sa malim n:")
measure_time(ispis, len(small_random_list))

print("Test linearne složenosti sa velikim n:")
measure_time(ispis, len(big_random_list))
#%% md
# ### O(n^2)
#%%
def kvadratna(n):
    for i in range(n):
        for j in range(n):
            pass
#%%
print("Test kvadratne složenosti sa malim n:")
measure_time(kvadratna, 10_000)

print("Test kvadratne složenosti sa velikim n:")
measure_time(kvadratna,40_000)
#%% md
# ### O(2^n)
#%%
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
#%%
print("Test eksponencijalne složenosti za n=20:")
measure_time(fib, 20)

print("Test eksponencijalne složenosti za n=30:")
measure_time(fib, 30)
#%% md
# ### O(n!)
#%%
import itertools

def permutacije(n):
    elementi = list(range(n))
    for p in itertools.permutations(elementi):
        pass  # ne printamo, da ubrzamo test
#%%
print("Test faktorske složenosti za n=7:")
measure_time(permutacije, 7)

print("Test faktorske složenosti za n=8:")
measure_time(permutacije, 8)
#%% md
# ## Algoritmi pretrage
#%% md
# ### Linearna pretraga
#%%
def linear_search(niz, x):
    for i in range(len(niz)):
        if niz[i] == x:
            return i
    return -1
#%%
# Najbolji slučaj (element je na početku)
print("Linearna pretraga — najbolji slučaj (prvi element):")
measure_time(linear_search, small_random_list, small_random_list[0])
measure_time(linear_search, big_random_list, big_random_list[0])

# Srednji slučaj (element je na sredini)
print("\nLinearna pretraga — srednji slučaj (srednji element):")
measure_time(linear_search, small_random_list, small_random_list[len(small_random_list)//2])
measure_time(linear_search, big_random_list, big_random_list[len(big_random_list)//2])

# Najgori slučaj (element ne postoji)
print("\nLinearna pretraga — najgori slučaj (nema elementa):")
measure_time(linear_search, small_random_list, -1)
measure_time(linear_search, big_random_list, -1)
#%% md
# ### Linearna pretraga sa Strazarom
#%%
def sentinel_search(niz, x):
    n = len(niz)
    last = niz[-1]
    niz[-1] = x  # dodavanje stražara
    i = 0
    while niz[i] != x:
        i += 1
    niz[-1] = last  # vraćamo poslednji element
    if i < n - 1 or last == x:
        return i
    return -1
#%%
# Najbolji slučaj (na početku)
print("Sentinel pretraga — najbolji slučaj:")
measure_time(sentinel_search, small_random_list.copy(), small_random_list[0])
measure_time(sentinel_search, big_random_list.copy(), big_random_list[0])

# Srednji slučaj (u sredini)
print("\nSentinel pretraga — srednji slučaj:")
measure_time(sentinel_search, small_random_list.copy(), small_random_list[len(small_random_list)//2])
measure_time(sentinel_search, big_random_list.copy(), big_random_list[len(big_random_list)//2])

# Najgori slučaj (ne postoji)
print("\nSentinel pretraga — najgori slučaj:")
measure_time(sentinel_search, small_random_list.copy(), -1)
measure_time(sentinel_search, big_random_list.copy(), -1)
#%% md
# ### Binarna pretraga
#%%
def binary_search(niz, x):
    low, high = 0, len(niz) - 1
    while low <= high:
        mid = (low + high) // 2
        if niz[mid] == x:
            return mid
        elif niz[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#%% md
# #### Obavezno sortiranje
#%%
sorted_small = sorted(small_random_list)
sorted_big = sorted(big_random_list)
#%%
# Najbolji slučaj — tražimo srednji element
print("Binarna pretraga — najbolji slučaj:")
measure_time(binary_search, sorted_small, sorted_small[len(sorted_small)//2])
measure_time(binary_search, sorted_big, sorted_big[len(sorted_big)//2])

# Srednji slučaj — tražimo neki "nasumični" koji nije odmah na sredini
print("\nBinarna pretraga — srednji slučaj:")
measure_time(binary_search, sorted_small, sorted_small[len(sorted_small)//4])
measure_time(binary_search, sorted_big, sorted_big[len(sorted_big)//4])

# Najgori slučaj — tražimo nepostojeći element
print("\nBinarna pretraga — najgori slučaj:")
measure_time(binary_search, sorted_small, -1)
measure_time(binary_search, sorted_big, -1)
#%% md
# ### Rekurzivna binarna pretraga
#%%
def binary_search_recursive(niz, x, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if niz[mid] == x:
        return mid
    elif niz[mid] < x:
        return binary_search_recursive(niz, x, mid + 1, high)
    else:
        return binary_search_recursive(niz, x, low, mid - 1)
#%%
# Funkcija koja poziva rekurzivnu pretragu pravilno
def test_recursive_search(niz, x):
    return binary_search_recursive(niz, x, 0, len(niz) - 1)

# Najbolji slučaj: srednji element
print("Rekurzivna binarna pretraga — najbolji slučaj:")
measure_time(test_recursive_search, sorted_small, sorted_small[len(sorted_small)//2])
measure_time(test_recursive_search, sorted_big, sorted_big[len(sorted_big)//2])

# Srednji slučaj: element u prvoj četvrtini
print("\nRekurzivna binarna pretraga — srednji slučaj:")
measure_time(test_recursive_search, sorted_small, sorted_small[len(sorted_small)//4])
measure_time(test_recursive_search, sorted_big, sorted_big[len(sorted_big)//4])

# Najgori slučaj: element ne postoji
print("\nRekurzivna binarna pretraga — najgori slučaj:")
measure_time(test_recursive_search, sorted_small, -1)
measure_time(test_recursive_search, sorted_big, -1)