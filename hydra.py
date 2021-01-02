#hydra.py


import tkinter as tk
from random import randint


class Hydra:
    head_num = 0
    
    
    def __init__(self, master):
        self.master = master
        
        self.master.protocol('WM_DELETE_WINDOW', self.new_window)
        
        w, h = 400, 100
        
        screen_w = self.master.winfo_screenwidth()
        screen_h = self.master.winfo_screenheight()
        
        x = (screen_w - randint(0, screen_w))
        y = (screen_h - randint(0, screen_h))
        
        self.master.geometry(f"{w}x{h}+{x}+{y}")
        self.master.winfo_toplevel().title(f"Head {Hydra.head_num}")

        self.label = tk.Label(self.master, text = 'cut off one head and\ntwo more will take its place....')
        self.label.config(font=("Courier", 20))
        self.label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        

    def new_window(self):
        for x in range(2):
            Hydra.head_num += 1;
            self.newRoot = tk.Tk()
            self.app = Hydra(self.newRoot)
        self.master.destroy()
        

def main():
    root = tk.Tk()
    app = Hydra(root)
    root.mainloop()

    
if __name__ == '__main__':
    main()