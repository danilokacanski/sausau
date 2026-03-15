#%% md
# ## Grafovi 1
#%% md
# ## BFS
#%%
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
#%%
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [8],
    5: [9],
    6: [10],
    7: [],
    8: [],
    9: [],
    10: []
}
#%%
bfs(graph, 1)
#%% md
# ## DFS
#%%
def DFS(visited, graph, cvor):
    if cvor not in visited:
        print(cvor)
        visited.append(cvor)
        for sused in graph[cvor]:
            DFS(visited, graph, sused)
#%%
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [8],
    5: [9],
    6: [10],
    7: [],
    8: [],
    9: [],
    10: []
}
#%%
visited = []
DFS(visited, graph, 1)
#%% md
# ## Dijkstra
#%%
import math
#%%
def dijkstra(graph, source):
    unvisited = graph.copy()
    dist = {}

    for cvor in unvisited:
        dist[cvor] = math.inf
    dist[source] = 0

    while unvisited:
        min_cvor = None
        for cvor in unvisited:
            if min_cvor is None or dist[cvor] < dist[min_cvor]:
                min_cvor = cvor

        for sused, tezina in unvisited[min_cvor]:
            if dist[min_cvor] + tezina < dist[sused]:
                dist[sused] = dist[min_cvor] + tezina

        unvisited.pop(min_cvor)

    print("Udaljenost čvorova od početnog čvora:")
    for cvor in dist:
        print(f"{cvor}\t\t{dist[cvor]}")
#%%
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('C', 11), ('D', 9)],
    'C': [('E', 3)],
    'D': [('E', 7), ('F', 2)],
    'E': [('F', 6)],
    'F': []
}
#%%
dijkstra(graph, 'A')
#%% md
# ## Bellman-Ford
#%%
def bellmanFord(graph, source):
    dist = {node: math.inf for node in graph}
    dist[source] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    # Provera negativnog ciklusa
    for u in graph:
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                print("Graf sadrži negativnu kružnu putanju!")
                return

    print("Najkraće rastojanje od čvora", source)
    for node in dist:
        print(f"{node}: {dist[node]}")
#%%
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('C', 11), ('D', 9)],
    'C': [('E', 3)],
    'D': [('E', 7), ('F', 2)],
    'E': [('F', 6)],
    'F': []
}
#%%
bellmanFord(graph, 'A')