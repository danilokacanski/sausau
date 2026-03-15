#%% md
# # Sturkture podataka 2
#%% md
# ## Stack
#%%
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Dodaje novi element na vrh steka"""
        self.items.append(item)

    def pop(self):
        """Uklanja i vraća poslednji ubačeni element"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Vraća element sa vrha steka bez uklanjanja"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Proverava da li je stek prazan"""
        return len(self.items) == 0
#%%
s = Stack()
#%%
s.push(10)
s.push(20)
s.push(30)
#%%
print("Da li je stek prazan?", s.is_empty())
#%%
s.items
#%%
print("Element na vrhu:", s.peek())
#%%
print("Uklanjanje:", s.pop())
print("Novi vrh:", s.peek())
#%%
print("Uklanjanje:", s.pop())
print("Uklanjanje:", s.pop())
print("Uklanjanje sa praznog steka:", s.pop())
#%%
print("Da li je stek prazan?", s.is_empty())
#%% md
# ## Validacija izraza sa zagradama
#%%
def validacija_zagrada(izraz):
    stek = Stack()
    parovi = {')': '(', ']': '[', '}': '{'}

    for char in izraz:
        if char in '([{':
            stek.push(char)
        elif char in ')]}':
            if stek.is_empty() or stek.pop() != parovi[char]:
                return False
    return stek.is_empty()
#%%
print(validacija_zagrada("({[]})"))
print(validacija_zagrada("(([]{[]}))"))
print(validacija_zagrada("({[)]}"))
print(validacija_zagrada("(((()"))
print(validacija_zagrada(""))
#%% md
# ## Queue
#%%
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)  # dodaje na kraj reda

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()  # uklanja sa početka reda

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]  # prikazuje prvi bez uklanjanja

    def is_empty(self):
        return len(self.items) == 0
#%%
q = Queue()
#%%
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
#%%
print(q.is_empty())
#%%
print(q.dequeue())
#%%
print(q.peek())
#%%
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
#%% md
# ## Upravljanje redom zadataka
#%%
import time
# Lista zadataka: svaki je (naziv, trajanje)
zadaci = [
    ("Backup fajlova", 3),
    ("Slanje izveštaja", 2),
    ("Restart sistema", 1)
]

# Kreiramo red
red = Queue()

# Dodajemo zadatke u red
for z in zadaci:
    red.enqueue(z)

# Izvršavamo zadatke redom
while not red.is_empty():
    naziv, trajanje = red.dequeue()
    print(f"Izvršava se zadatak: {naziv} (traje {trajanje} sekundi)")
    time.sleep(trajanje)  # simulacija trajanja

# Provera da li je red prazan
print("Svi zadaci su izvršeni:", red.is_empty())
#%% md
# ## Linked List
#%%
class Node:
    def __init__(self, value):
        self.value = value  # vrednost čvora
        self.next = None    # veza ka sledećem čvoru

class LinkedList:
    def __init__(self):
        self.head = None  # početak liste

    def append(self, value):
        """Dodavanje čvora na kraj liste"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        """Dodavanje čvora na početak liste"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Brisanje prvog čvora sa datom vrednošću"""
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def find(self, value):
        """Pronalazak elementa u listi"""
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def print_list(self):
        """Pomoćna metoda za ispis liste"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista je prazna.")
#%%
ll = LinkedList()
#%%
ll.append(10)
ll.append(20)
ll.append(30)
print("Lista nakon dodavanja na kraj:")
ll.print_list()
#%%
ll.prepend(5)
print("Lista nakon dodavanja na početak:")
ll.print_list()
#%%
print("Da li postoji 20?", "Da" if ll.find(20) else "Ne")
print("Da li postoji 99?", "Da" if ll.find(99) else "Ne")
#%%
ll.delete(20)
print("Lista nakon brisanja 20:")
ll.print_list()
#%%
ll.delete(5)
print("Lista nakon brisanja 5:")
ll.print_list()
#%%
ll.delete(30)
print("Lista nakon brisanja 30:")
ll.print_list()
#%%
ll.delete(10)
print("Lista nakon brisanja 10:")
ll.print_list()
#%% md
# ## Josephus Problem
#%%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Dodaje novi čvor u kružnu listu"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Sam na sebe pokazuje
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove_next(self, prev_node):
        """Briše čvor koji sledi nakon datog čvora i vraća njegovu vrednost"""
        removed_node = prev_node.next
        prev_node.next = removed_node.next
        if removed_node == self.head:
            self.head = removed_node.next
        return removed_node.value
#%%
def josephus(n, k):
    # Inicijalizacija kružne liste
    circle = CircularLinkedList()
    for i in range(1, n + 1):
        circle.append(i)

    result = []  # Redosled eliminacije
    current = circle.head

    while current.next != current:  # Dok ne ostane samo jedan čvor
        for _ in range(k - 2):
            current = current.next
        eliminated = circle.remove_next(current)
        result.append(eliminated)
        current = current.next

    survivor = current.value
    return result, survivor
#%%
eliminated, winner = josephus(7, 3)
print("Redosled eliminacije:", eliminated)
print("Pobednik:", winner)
#%% md
# ## Tree
#%%
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def print_tree(self, node = None, prefix="", is_left=True):
        if node is not None:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
#%%
tree = BinaryTree(10)
#%%
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(20)
#%%
print("Preorder obilazak stabla:")
tree.preorder(tree.root)
#%%
tree.print_tree(tree.root)
#%%
tree.insert(22)
tree.insert(18)
tree.insert(1)
tree.insert(4)
tree.insert(33)
tree.insert(99)
#%%
tree.print_tree(tree.root)
#%%
print("Da li postoji čvor sa vrednošću 7?", "Da" if tree.search(7) else "Ne")
#%%
print("Da li postoji čvor sa vrednošću 100?", "Da" if tree.search(100) else "Ne")
#%% md
# ## Sortirani telefonski kontakti
#%%
class ContactTree(BinaryTree):
    def inorder(self, node=None):
        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
#%%
contacts = ContactTree("Maja")
contacts.insert("Ana")
contacts.insert("Jovan")
contacts.insert("Zoran")
contacts.insert("Ivana")
contacts.insert("Boris")
contacts.insert("Luka")

print(" Kontakti po abecednom redu:")
contacts.inorder(contacts.root)