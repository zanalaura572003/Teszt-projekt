import tkinter as tk
from tkinter import messagebox
import os


class Jegyrendszer_ZL:
    def __init__(self, root):
        self.app = root
        self.app.title("Jegyfoglaló Rendszer ZL")
        self.app.geometry("400x350")

        self.cimke_nev = tk.Label(self.app, text="Vásárló neve:")
        self.cimke_nev.pack(pady=5)

        self.mezo_nev = tk.Entry(self.app, bg="white", fg="black", insertbackground="black")
        self.mezo_nev.pack(pady=5)

        self.cimke_tipus = tk.Label(self.app, text="Jegy típusa (diák/felnőtt/nyugdíjas):")
        self.cimke_tipus.pack(pady=5)

        self.mezo_tipus = tk.Entry(self.app, bg="white", fg="black", insertbackground="black")
        self.mezo_tipus.pack(pady=5)

        self.cimke_db = tk.Label(self.app, text="Darabszám:")
        self.cimke_db.pack(pady=5)

        self.mezo_db = tk.Entry(self.app, bg="white", fg="black", insertbackground="black")
        self.mezo_db.pack(pady=5)

        self.gomb_vasarlas = tk.Button(self.app, text="Vásárlás", command=self.vasarlas_esemeny_ZL)
        self.gomb_vasarlas.pack(pady=20)

    def ar_szamitas_ZL(self, tipus, db):
        alapar = 0
        if tipus.lower() == "diák":
            alapar = 1000
        elif tipus.lower() == "felnőtt":
            alapar = 2500
        elif tipus.lower() == "nyugdíjas":
            alapar = 1500
        else:
            return 0

        return alapar * db

    def fajlba_iras_ZL(self, nev, tipus, db, ar):
        with open("foglalasok.txt", "a", encoding="utf-8") as fajl:
            sor = f"Név: {nev.ljust(20, ' ')} | Típus: {tipus.ljust(10, ' ')} | Db: {str(db).ljust(3, ' ')} | Ár: {ar} Ft\n"
            fajl.write(sor)

    def vasarlas_esemeny_ZL(self):
        nev = self.mezo_nev.get()
        tipus = self.mezo_tipus.get()

        try:
            db = int(self.mezo_db.get())
        except ValueError:
            messagebox.showerror("Hiba", "A darabszámnak számnak kell lennie!")
            return

        if not nev or not tipus or not db:
            messagebox.showwarning("Figyelmeztetés", "Minden mezőt ki kell tölteni!")
            return

        fizetendo = self.ar_szamitas_ZL(tipus, db)

        if fizetendo == 0:
            messagebox.showerror("Hiba", "Érvénytelen jegytípus! (diák/felnőtt/nyugdíjas)")
            return

        self.fajlba_iras_ZL(nev, tipus, db, fizetendo)
        messagebox.showinfo("Siker", f"Sikeres foglalás!\nFizetendő összeg: {fizetendo} Ft")

        self.mezo_nev.delete(0, tk.END)
        self.mezo_tipus.delete(0, tk.END)
        self.mezo_db.delete(0, tk.END)