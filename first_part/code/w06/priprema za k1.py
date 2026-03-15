#%% md
# # Priprema za K1
#%% md
# ## Zadatak 1
# Modifikovati DFS algoritam tako da vrši proveru da li je graf jako povezan. Graf je jako povezan ako se iz svakog čvora može stići do svakog drugog čvora u grafu.
#%%
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.DFS(u, visited)

    def jakoPovezan(self):
        n = len(self.graph)
        for i in range(n):
            visited = [False] * n
            self.DFS(i, visited)
            for b in visited:
                if not b:
                    return False
        return True
#%%
graph = Graph()
graph.addEdge(0, 4)
graph.addEdge(1, 0)
graph.addEdge(1, 2)
graph.addEdge(2, 1)
graph.addEdge(2, 4)
graph.addEdge(3, 1)
graph.addEdge(3, 2)
graph.addEdge(4, 3)

if graph.jakoPovezan():
    print('Graf je jako povezan')
else:
    print('Graf nije jako povezan')
#%%
graph2 = Graph()
graph2.addEdge(0, 1)
graph2.addEdge(0, 2)

if graph2.jakoPovezan():
    print('Graf je jako povezan')
else:
    print('Graf nije jako povezan')

#%% md
# ## Zadatak 2
# 
# Modifikovati DFS algoritam tako da vraća indeks izvornog čvora u grafu. Izvorni čvor je onaj čvor od kog se može stići do svakog drugog čvora u grafu. U grafu sa slike ispod izvorni čvor je 4.
#%%
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def DFS(self, v, visited):
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.DFS(u, visited)

    def pronadjiIzvorniCvor(self):
        n = len(self.graph)
        visited = [False] * n
        v = 0

        for i in range(n):
            if not visited[i]:
                self.DFS(i, visited)
                v = i

        visited = [False] * n
        self.DFS(v, visited)

        for i in range(n):
            if not visited[i]:
                return -1
        return v

#%%
graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 0)
graph.addEdge(4, 3)
graph.addEdge(4, 5)
graph.addEdge(5, 0)

root = graph.pronadjiIzvorniCvor()
if root != -1:
    print('Izvorni čvor je', root)
else:
    print('Izvorni čvor ne postoji')
#%% md
# ## Zadatak 3
# 
# Za dati neusmereni graf izvršiti proveru da li je bipartitivan. Bipartitivan graf je onaj kod kog se čvorovi mogu podeliti u dve grupe, pri čemu je svaki čvor iz jedne grupe povezan sa bar jednim iz druge grupe, dok čvorovi iz iste grupe ne formiraju veze.
#%%
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bipartitanGraf(self):
        n = len(self.graph)
        visited = [False] * n
        level = [None] * n

        for start in range(n):
            if not visited[start]:
                queue = [start]
                visited[start] = True
                level[start] = 0

                while queue:
                    v = queue.pop(0)
                    for u in self.graph[v]:
                        if not visited[u]:
                            visited[u] = True
                            level[u] = level[v] + 1
                            queue.append(u)
                        elif level[u] == level[v]:
                            return False
        return True
#%%
graph = Graph()
graph.addEdge(0, 5)
graph.addEdge(1, 5)
graph.addEdge(1, 6)
graph.addEdge(2, 7)
graph.addEdge(2, 8)
graph.addEdge(3, 6)
graph.addEdge(4, 5)
graph.addEdge(4, 8)

if graph.bipartitanGraf():
    print('Graf je bipartitivan')
else:
    print('Graf nije bipartitivan')
#%% md
# ## Zadatak 4
# 
# Rukovodilac u kompaniji treba da oceni svoje zaposlene
# Za svakog zaposlenog dobija se informacija o tome koliko je sati proveo na poslu svakog dana tokom prethodnih 15 radnih dana (minimalna vrednost 0, maksimalna vrednost 10)
# Zaposleni dobija prelaznu ocenu ako se bar jednom u prethodnih 15 dana desilo da je barem 5 dana zaredom proveo najmanje 7 sati na poslu
# Napisati algoritam koji određuje da li zaposleni zaslužuje prelaznu ocenu
# 
# Napomena: Voditi računa o kompleksnosti!
#%%
def imaPrelaznuOcenu(radni_sati):
    uzastopni_dani = 0

    for sati in radni_sati:
        if sati >= 7:
            uzastopni_dani += 1
            if uzastopni_dani == 5:
                return True
        else:
            uzastopni_dani = 0

    return False
#%%
zaposleni1 = [6, 7, 7, 8, 7, 9, 6, 5, 4, 7, 7, 7, 7, 7, 6]
zaposleni2 = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

print("Zaposleni 1:", imaPrelaznuOcenu(zaposleni1))
print("Zaposleni 2:", imaPrelaznuOcenu(zaposleni2))
#%% md
# ## Zadatak 5
# 
# Neka je dat sortiran binarni niz (niz koji se sastoji isključivo od nula i jedinica, pri čemu se elementi mogu ponavljati)
# Modifikovati algoritam binarne pretrage tako da kao povratnu vrednost vraća broj jedinica u takvom nizu
# 
# Napomena: Voditi računa o kompleksnosti!
#%%
def broj_jedinica(niz):
    levo = 0
    desno = len(niz) - 1
    prvi_jedinica = -1

    while levo <= desno:
        sredina = (levo + desno) // 2

        if niz[sredina] == 1:
            prvi_jedinica = sredina
            desno = sredina - 1  # tražimo još raniju jedinicu
        else:
            levo = sredina + 1

    if prvi_jedinica == -1:
        return 0  # Nema jedinica
    return len(niz) - prvi_jedinica
#%%
print(broj_jedinica([0, 0, 0, 1, 1, 1, 1]))
print(broj_jedinica([0, 0, 0, 0, 0]))
print(broj_jedinica([1, 1, 1, 1]))
#%% md
# ## Zadatak 6
# 
# Neka je dat niz uređenih trojki, takvih da prvi element uređene trojke predstavlja broj datih golova neke ekipe, drugi element predstavlja broj primljenih golova, a treći element predstavlja ukupan broj osvojenih bodova te ekipe
# Modifikovati Selection sort algoritam tako da izvrši sortiranje datog niza po broju bodova, počevši od ekipe sa najviše bodova
# Ako dve ekipe imaju isti broj bodova, bolja je ona ekipa koja ima bolju gol razliku (gol razlika = broj datih golova – broj primljenih golova)
# 
# 
# Napomena: Ne povećavati kompleksnost izvornog algoritma!
# 
# 
# Primer ulaznog niza:
# 
#     [(92, 34, 79), (99, 28, 81), (83, 22, 79), (44, 51, 56), (101, 44, 85), (42, 48, 56)]
# 
# Očekivani izlaz:
# 
#     [(101, 44, 85), (99, 28, 81), (83, 22, 79), (92, 34, 79), (42, 48, 56), (44, 51, 56)]
#%%
def selection_sort_timovi(timovi):
    n = len(timovi)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            bodovi_j = timovi[j][2]
            bodovi_max = timovi[max_idx][2]

            if bodovi_j > bodovi_max:
                max_idx = j
            elif bodovi_j == bodovi_max:
                gol_razlika_j = timovi[j][0] - timovi[j][1]
                gol_razlika_max = timovi[max_idx][0] - timovi[max_idx][1]
                if gol_razlika_j > gol_razlika_max:
                    max_idx = j

        # Zameni elemente
        timovi[i], timovi[max_idx] = timovi[max_idx], timovi[i]

    return timovi
#%%
timovi = [
    (92, 34, 79),
    (99, 28, 81),
    (83, 22, 79),
    (44, 51, 56),
    (101, 44, 85),
    (42, 48, 56)
]

sortirani = selection_sort_timovi(timovi)
print(sortirani)