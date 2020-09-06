import tkinter as Tk

def button_clicked(btn, lbl):
    # lbl["text"] = btn.config('text')[-1] + " Button Clicked"
    txt = lbl.get() + ' + ' + btn.config('text')[-1] + " Button Clicked"
    lbl.set(value=txt)

def btnLampOn_clicked():
    # button_clicked(btnLampOn, lblLampOn)
    button_clicked(btnLampOn, txtLampOn)

def btnStart_clicked():
    # button_clicked(btnStart, lblStart)
    button_clicked(btnStart, txtStart)

root = Tk.Tk()
root.geometry("400x400")
root.title("OPC UA")

frame = Tk.Frame(
    root,
    width = 400,
    height = 400,
    bg = 'black'
)
frame.pack(
    expand = 1,
    fill = Tk.BOTH
)

btnLampOn = Tk.Button(
    frame,
    text = "Lamp_On",
    command = btnLampOn_clicked
)
btnLampOn.grid(
    row = 0, column = 0,
    padx = 5, pady = 5,
    sticky = Tk.W + Tk.E + Tk.N + Tk.S
)

txtLampOn = Tk.StringVar(value='Lamp_On Label')

lblLampOn = Tk.Label(
    frame,
    textvariable = txtLampOn
)
lblLampOn.grid(
    row = 0, column = 1,
    padx = 5, pady = 5,
    columnspan = 2,
    sticky = Tk.W + Tk.E + Tk.N + Tk.S
)

btnStart = Tk.Button(
    frame,
    text = "Start",
    command = btnStart_clicked
)
btnStart.grid(
    row = 1, column = 0,
    padx = 5, pady = 5,
    sticky = Tk.W + Tk.E + Tk.N + Tk.S
)

txtStart = Tk.StringVar(value='Start Label')

lblStart = Tk.Label(
    frame,
    textvariable = txtStart
)
lblStart.grid(
    row = 1, column = 1,
    padx = 5, pady = 5,
    columnspan = 2,
    sticky = Tk.W + Tk.E + Tk.N + Tk.S
)

root.mainloop()
