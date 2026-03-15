# Topolosko sortiranje
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)

    def topoLogicalSort(self):
        visited = [False] * len(self.graph)
        stack = []
        for i in self.graph:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        #print(stack)
        return stack  # Dodato za animaciju


def animate_topo_sort(edges, order):
    G = nx.DiGraph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots()
    visited = set()

    def update(frame):
        ax.clear()
        visited.add(order[frame])
        node_colors = ['lightgreen' if node in visited else 'lightgray' for node in G.nodes]

        nx.draw(G, pos, with_labels=True, ax=ax,
                node_color=node_colors, edge_color='gray',
                node_size=600, arrows=True)
        ax.set_title(f"Korak {frame + 1}: Čvor {order[frame]} dodat u topološki red")

    ani = FuncAnimation(fig, update, frames=len(order), interval=1000, repeat=False)
    return ani

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Topološki sortiran graf:")
order = g.topoLogicalSort()  # Vraća listu koju prosleđuješ animaciji
print(order)
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
anim = animate_topo_sort(edges, order)
anim.save("animacije/topo_sort_animacija.mp4", writer="ffmpeg", fps=1)
plt.show()

# %% Primov algoritam (logika)
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_with_steps(self):
        visited = [False] * len(self.graph)
        visited[0] = True  # počinjemo od v0
        E = 0
        total_weight = 0
        steps = []

        while E < len(self.graph) - 1:
            minimum = float('inf')
            a = b = 0
            for n in range(len(self.graph)):
                if visited[n]:
                    for to, weight in self.graph[f"v{n}"]:
                        to_index = int(to[1:])
                        if not visited[to_index] and weight < minimum:
                            minimum = weight
                            a = n
                            b = to_index
            steps.append((f"v{a}", f"v{b}", minimum))
            total_weight += minimum
            visited[b] = True
            E += 1

        return steps, total_weight


#Građene grafa i animacija

G = Graph()
G.addEdge("v0", "v1", 4)
G.addEdge("v0", "v8", 8)
G.addEdge("v1", "v3", 8)
G.addEdge("v1", "v8", 11)
G.addEdge("v2", "v3", 2)
G.addEdge("v2", "v7", 6)
G.addEdge("v2", "v8", 7)
G.addEdge("v3", "v4", 7)
G.addEdge("v3", "v6", 4)
G.addEdge("v4", "v6", 14)
G.addEdge("v4", "v5", 9)
G.addEdge("v5", "v6", 10)
G.addEdge("v6", "v7", 2)
G.addEdge("v7", "v8", 1)

steps, total = G.prim_with_steps()

# Kreiramo prazan graf za crtanje
G_draw = nx.Graph()
all_nodes = list(G.graph.keys())
G_draw.add_nodes_from(all_nodes)

# Pozicije za crtanje fiksne
pos = {
    "v0": (0, 1),  "v1": (1, 2),  "v2": (1, 0),
    "v3": (2, 1),  "v4": (3, 2),  "v5": (4, 1),
    "v6": (3, 0),  "v7": (2, -1), "v8": (0, -1)
}

fig, ax = plt.subplots(figsize=(8, 6))
edge_labels = {}
colors = []

def update(i):
    ax.clear()
    nx.draw_networkx_nodes(G_draw, pos, node_color="lightblue", ax=ax)
    nx.draw_networkx_labels(G_draw, pos, ax=ax)
    for j in range(i + 1):
        u, v, w = steps[j]
        G_draw.add_edge(u, v, weight=w)
        edge_labels[(u, v)] = w
        colors.append("green")
    nx.draw_networkx_edges(G_draw, pos, edge_color=colors, width=2, ax=ax)
    nx.draw_networkx_edge_labels(G_draw, pos, edge_labels=edge_labels, ax=ax)
    ax.set_title(f"Korak {i+1} / {len(steps)}", fontsize=14)
    ax.axis("off")

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1500, repeat=False)

# Snimi animaciju
ani.save("v6/kod/animacije/prim_animacija.mp4", writer="ffmpeg", fps=1)
print(f"Ukupna težina MST: {total}")


# %% Kruskalov algoritam

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Graph:
    def __init__(self):
        self.edges = []

    def addEdge(self, u, v, w):
        self.edges.append((w, u, v))  # Sortiraćemo po težini

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, xroot, yroot):
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_with_steps(self):
        result = []
        self.edges.sort()
        parent = {}
        rank = {}

        nodes = set()
        for _, u, v in self.edges:
            nodes.add(u)
            nodes.add(v)

        for node in nodes:
            parent[node] = node
            rank[node] = 0

        for weight, u, v in self.edges:
            xroot = self.find(parent, u)
            yroot = self.find(parent, v)

            if xroot != yroot:
                result.append((u, v, weight))
                self.union(parent, rank, xroot, yroot)

        total_weight = sum([w for _, _, w in result])
        return result, total_weight

G = Graph()
G.addEdge("v0", "v1", 4)
G.addEdge("v0", "v8", 8)
G.addEdge("v1", "v3", 8)
G.addEdge("v1", "v8", 11)
G.addEdge("v2", "v3", 2)
G.addEdge("v2", "v7", 6)
G.addEdge("v2", "v8", 7)
G.addEdge("v3", "v4", 7)
G.addEdge("v3", "v6", 4)
G.addEdge("v4", "v6", 14)
G.addEdge("v4", "v5", 9)
G.addEdge("v5", "v6", 10)
G.addEdge("v6", "v7", 2)
G.addEdge("v7", "v8", 1)

steps, total = G.kruskal_with_steps()

G_draw = nx.Graph()
all_nodes = ["v0", "v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8"]
G_draw.add_nodes_from(all_nodes)

pos = {
    "v0": (0, 1),  "v1": (1, 2),  "v2": (1, 0),
    "v3": (2, 1),  "v4": (3, 2),  "v5": (4, 1),
    "v6": (3, 0),  "v7": (2, -1), "v8": (0, -1)
}

fig, ax = plt.subplots(figsize=(8, 6))
edge_labels = {}
colors = []

def update(i):
    ax.clear()
    nx.draw_networkx_nodes(G_draw, pos, node_color="lightblue", ax=ax)
    nx.draw_networkx_labels(G_draw, pos, ax=ax)
    for j in range(i + 1):
        u, v, w = steps[j]
        G_draw.add_edge(u, v, weight=w)
        edge_labels[(u, v)] = w
        colors.append("green")
    nx.draw_networkx_edges(G_draw, pos, edge_color=colors, width=2, ax=ax)
    nx.draw_networkx_edge_labels(G_draw, pos, edge_labels=edge_labels, ax=ax)
    ax.set_title(f"Kruskal korak {i+1}/{len(steps)}", fontsize=14)
    ax.axis("off")

ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=1500, repeat=False)

ani.save("v6/kod/animacije/kruskal_animacija.mp4", writer="ffmpeg", fps=1)

print(f"Ukupna težina MST: {total}")