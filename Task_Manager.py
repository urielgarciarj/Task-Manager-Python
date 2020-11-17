import tkinter as tk

class Process:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration

root = tk.Tk()
root.title("Practica 2 Computacion Tolerante a Fallas")

rowCounter = 0
columnCounter = 4
ProcessList = []

def checkValues():
    global ProcessList
    for entry in ProcessList:
        print("Valor: ", entry.start.get(), entry.duration.get())

def addingNewProcess():
    global rowCounter
    rowCounter = rowCounter + 1
    tk.Label(root, text="Inicio: ").grid(row=rowCounter, column=0)
    start = tk.Entry(root, width=10)
    start.grid(row=rowCounter, column=1)
    tk.Label(root, text="Duracion").grid(row=rowCounter, column=2)
    duration = tk.Entry(root, width=10)
    duration.grid(row=rowCounter, column=3)
    ProcessList.append(Process(start, duration))

def action():
    print("Hello!")

if __name__ == '__main__':
    tk.Label(root, text="Inicio: ").grid(row=rowCounter, column=0)
    start = tk.Entry(root, width=10)
    start.grid(row=rowCounter, column=1)
    tk.Label(root, text="Duracion").grid(row=rowCounter, column=2)
    duration = tk.Entry(root, width=10)
    duration.grid(row=rowCounter, column=3)
    ProcessList.append(Process(start, duration))
    addProcessbtn = tk.Button(root, text="Add", command=addingNewProcess).grid(row=0, column=4)

    tk.Button(root, text="Comenzar", command=checkValues).place(x=10, y=300)

    root.geometry("400x400")
    root.mainloop()
