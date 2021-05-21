import tkinter as tkinter

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='488c1ff')
frame.place(reLx=0.1, rely=0.1, reLwidth=0.8, reLheight=0.5)

button = tk.Button(frame, text="Test button", bg='gray')
button.place(reLx=0, reLy=0, reLwidth=0.25, reLheight=0.25)

label = tk.Label(frame, text="Label example", bg='yellow')
label.place(reLx=0.3, reLy=0, reLwidth=0.45, reLheight=0.25)

entry = tk.Entry(frame, bg='green')
entry.place(reLx=0.8, reLy=0, reLwidth=0.2, reLheight=0.25)

root.mainloop()