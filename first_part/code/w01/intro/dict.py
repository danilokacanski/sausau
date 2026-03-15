#%% md
# # Dict
#%% md
# ## Inicijalizacija i osnovna svojstva
#%%
# Kreiranje rečnika
osoba = {
    "ime": "Ana",
    "godine": 25,
    "student": True
}

print("Rečnik osoba:", osoba)
print("Tip:", type(osoba))
#%% md
# ## Dodavanje i ažuriranje
#%%
# Dodavanje novog ključa
osoba["prezime"] = "Petrović"

# Ažuriranje postojeće vrednosti
osoba["godine"] = 26

print("Ažurirani rečnik:", osoba)
#%% md
# ## Brisanje elemenata
#%%
# Brisanje pomoću del
del osoba["student"]

# Brisanje i vraćanje vrednosti
godine = osoba.pop("godine")
print("Izbačeno 'godine':", godine)

print("Rečnik nakon brisanja:", osoba)
#%% md
# ## Pristup vrednostima
#%%
# Direktan pristup
print("Ime:", osoba["ime"])

# Bezbedan pristup
print("Visina:", osoba.get("visina"))  # None jer ne postoji
#%% md
# ## Pregled sadržaja
#%%
print("Ključevi:", osoba.keys())
print("Vrednosti:", osoba.values())
print("Parovi:", osoba.items())
#%% md
# ## Iteracija kroz rečnik
#%%
# Kroz ključeve
for kljuc in osoba:
    print("Kljuc:", kljuc)

# Kroz vrednosti
for vrednost in osoba.values():
    print("Vrednost:", vrednost)

# Kroz parove
for kljuc, vrednost in osoba.items():
    print(f"{kljuc}: {vrednost}")
#%% md
# ## Ostale korisne metode
#%%
# Dodavanje više vrednosti
osoba.update({"država": "Srbija", "ime": "Ana"})

# Provera da li ključ postoji
print("Da li postoji ključ 'ime'? -", "ime" in osoba)
#%% md
# ## Česte greške i saveti
#%%
# Greška: pristupanje nepostojećem ključu bez provere
try:
    print(osoba["visina"])
except KeyError as e:
    print("Greška:", e)

# Greška: promenljiva struktura kao ključ
try:
    los_kljuc = [1, 2]
    test = {los_kljuc: "ne valja"}
except TypeError as e:
    print("Greška:", e)

# Savet: koristi .get()
print("Visina (get):", osoba.get("visina", "Nije uneto"))

# Savet: koristi .items()
for k, v in osoba.items():
    print(f"{k} => {v}")
#%% md
# ## Tipične primene
#%%
# Brojanje pojavljivanja
brojevi = [1, 2, 1, 3, 2, 1]
brojanja = {}
for x in brojevi:
    brojanja[x] = brojanja.get(x, 0) + 1
print("Brojanja:", brojanja)

# Primer mapiranja ID -> vrednost
mapa_id = {100: "Ana", 101: "Marko"}
print("Ime za ID 101:", mapa_id.get(101))