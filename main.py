import tkinter as tk
from jegy_kezeles_ZL import Jegyrendszer_ZL

def main():
    root = tk.Tk()
    app = Jegyrendszer_ZL(root)
    root.mainloop()

if __name__ == "__main__":
    main()