# Jegyfoglaló Rendszer (Python Projektfeladat)

## Hallgató
**Név:** Vezetéknév Keresztnév (Monogram: ZL)

## Feladat leírása
A program egy egyszerű jegyfoglaló és értékesítő rendszer grafikus felülettel. A felhasználó megadhatja a nevét, a kívánt jegy típusát (diák, felnőtt, nyugdíjas) és a mennyiséget. A program eseménykezeléssel (gombnyomás) kiszámolja a fizetendő összeget a jegy típusa alapján (elágazásokkal), és az adatokat (a string metódusokkal formázva) elmenti egy `foglalasok.txt` fájlba. Amennyiben hibás adatot adunk meg (pl. szöveget a darabszámhoz), a program kivételkezelést (try-except) és hibaüzeneteket használ.

## Használt modulok és függvények

### Beépített (tanult) modulok:
- `tkinter`: A grafikus felület (GUI) létrehozásához.
    - Függvények/Metódusok: `Tk()`, `Label()`, `Entry()`, `Button()`, `pack()`, `get()`, `delete()`, `mainloop()`
- `tkinter.messagebox`: Felugró üzenetek (hiba, siker, figyelmeztetés) megjelenítéséhez.
    - Függvények: `showinfo()`, `showwarning()`, `showerror()`

### Saját (bemutatandó) modul:
- `jegy_kezeles_ZL`: A program üzleti logikáját és a GUI elemek inicializálását tartalmazza.

### Saját osztály:
- `Jegyrendszer_ZL`: Ez az osztály fogja össze a program működését, az ablak elemeit és a metódusokat.

### Saját függvények a `Jegyrendszer_ZL` osztályon belül:
1. `__init__(self, root)`: Az osztály konstruktora, létrehozza a grafikus elemeket és elrendezi azokat az alapablakon.
2. `ar_szamitas_ZL(self, tipus, db)`: Elágazások (if/elif) segítségével meghatározza az egy darab jegy árát, majd kiszámolja és visszaadja (return) a teljes fizetendő összeget.
3. `fajlba_iras_ZL(self, nev, tipus, db, ar)`: Fájlkezelést valósít meg. Megnyitja (vagy létrehozza) a szöveges fájlt, és a `.ljust()` metódusok segítségével formázva, az `f-string` technológiával fájlba írja az adatokat.
4. `vasarlas_esemeny_ZL(self)`: Ez az eseménykezelő függvény fut le a gomb megnyomásakor. Kiolvassa az adatokat, elvégzi a kivételkezelést (try-except a szám konvertálásánál), meghívja a számító és fájlíró metódusokat, majd kiüríti a mezőket.