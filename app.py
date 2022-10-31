import tkinter as tk
HIGHT = 300
WIDTH = 400
 
root = tk.Tk()

canvas = tk.Canvas(root, height=HIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1,  relwidth=0.8, relheight=0.8)

button = tk.Button(frame, text="Test button", bg='gray',)
button.pack()

label = tk.Label(frame, text="This is label", bg='yellow')
label.pack()

entry =  tk.Entry(frame, bg='green')
entry.pack()



root.mainloop()

 