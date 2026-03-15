#%% md
# # Sortiranja
#%% md
# ## Bubble Sort
#%%
def bubbleSort(niz):
    for i in range(len(niz)):
        for j in range(0, len(niz) - i - 1):
            if niz[j] > niz[j + 1]:
                # Zamena mesta ako su u pogrešnom redosledu
                niz[j], niz[j + 1] = niz[j + 1], niz[j]
#%%
test_niz = [8, 5, 3, 1, 4, 7, 9]
#%%
print("Pre sortiranja:", test_niz)
bubbleSort(test_niz)
print("Nakon standardne verzije:", test_niz)
#%% md
# ## Bubble Sort Optimizovana verzija
#%%
def bubbleSortOptimized(niz):
    for i in range(len(niz)):
        izvrsenaIzmena = False
        for j in range(0, len(niz) - i - 1):
            if niz[j] > niz[j + 1]:
                niz[j], niz[j + 1] = niz[j + 1], niz[j]
                izvrsenaIzmena = True
        if not izvrsenaIzmena:
            # Ako nije bilo nijedne zamene → niz je već sortiran
            break
#%%
test_niz = [8, 5, 3, 1, 4, 7, 9]
bubbleSortOptimized(test_niz)
print("Nakon optimizovane verzije:", test_niz)
#%% md
# ## Selection Sort
#%%
def selectionSort(niz):
    for index in range(len(niz)):
        min_index = index
        # Pronalazak najmanjeg u nesortiranom delu
        for j in range(index + 1, len(niz)):
            if niz[j] < niz[min_index]:
                min_index = j
        # Zamena sa prvim nesortiranim elementom
        niz[index], niz[min_index] = niz[min_index], niz[index]
#%%
test_niz = [6, 8, 3, 5, 9, 10, 7, 2, 4, 1]

print("Pre sortiranja:", test_niz)
selectionSort(test_niz)
print("Nakon sortiranja:", test_niz)
#%% md
# ## Insertion Sort
#%%
def insertionSort(niz):
    for i in range(1, len(niz)):
        trenutni = niz[i]
        j = i - 1
        # Pomeranje većih elemenata udesno
        while j >= 0 and niz[j] > trenutni:
            niz[j + 1] = niz[j]
            j -= 1
        # Ubacivanje trenutnog elementa na pravo mesto
        niz[j + 1] = trenutni
#%%
test_niz = [6, 5, 3, 1, 8, 7, 2, 4]

print("Pre sortiranja:", test_niz)
insertionSort(test_niz)
print("Nakon sortiranja:", test_niz)
#%% md
# ## Merge Sort
#%%
def mergeSort(niz):
    if len(niz) > 1:
        # 1. Podela
        sredina = len(niz) // 2
        L = niz[:sredina]
        R = niz[sredina:]

        # 2. Rekurzija
        mergeSort(L)
        mergeSort(R)

        # 3. Spajanje
        i = j = k = 0

        # Upoređivanje elemenata iz L i R i ubacivanje manjeg
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                niz[k] = L[i]
                i += 1
            else:
                niz[k] = R[j]
                j += 1
            k += 1

        # 4. Dodavanje preostalih elemenata
        while i < len(L):
            niz[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            niz[k] = R[j]
            j += 1
            k += 1
#%%
test_niz = [6, 8, 3, 5, 9, 10, 7, 2, 4, 1]

print("Pre sortiranja:", test_niz)
mergeSort(test_niz)
print("Nakon sortiranja:", test_niz)
#%% md
# ## Quick Sort
#%%
def partition(niz, donjaGranica, gornjaGranica):
    pivot = niz[gornjaGranica]  # pivot je poslednji element
    i = donjaGranica - 1        # indeks poslednjeg manjeg od pivota

    for j in range(donjaGranica, gornjaGranica):
        if niz[j] <= pivot:
            i += 1
            niz[i], niz[j] = niz[j], niz[i]  # zamena ako je niz[j] manji od pivota

    # Pivot ide na svoje mesto (iza poslednjeg manjeg)
    niz[i + 1], niz[gornjaGranica] = niz[gornjaGranica], niz[i + 1]
    return i + 1  # pozicija pivota
#%%
def quickSort(niz, donjaGranica, gornjaGranica):
    if donjaGranica < gornjaGranica:
        pi = partition(niz, donjaGranica, gornjaGranica)  # pozicija pivota
        # Sortiraj levo i desno od pivota
        quickSort(niz, donjaGranica, pi - 1)
        quickSort(niz, pi + 1, gornjaGranica)
#%%
test_niz = [8, 4, 7, 3, 9, 2, 6, 5, 1]

print("Pre sortiranja:", test_niz)
quickSort(test_niz, 0, len(test_niz) - 1)
print("Nakon sortiranja:", test_niz)