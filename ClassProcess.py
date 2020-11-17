import tkinter as tk

def show_entry_fields():
    print("Inicio: %s\nDuracion: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

master = tk.Tk()
tk.Label(master, text="Inicio").grid(row=0)
tk.Label(master, text="Duracion").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()

tk.mainloop()



