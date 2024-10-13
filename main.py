import tkinter as tk

root = tk.Tk()
root.title("Creating a Grid")
root.geometry("500x450")

for i in range (3):
    for j in range(3):
        frame = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame,text=f"row {i+1} x col {j+1}")
        label.pack()
root.mainloop()

