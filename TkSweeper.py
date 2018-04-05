from tkinter import *

global buttons  # Array of playfield buttons


def button_clicked(x, y):
    print(x, y)
    disable_button(x, y)
    # buttons[x][y].config(state=DISABLED)
    # buttons[x][y].grid_remove();


def disable_button(x, y):
    buttons[x][y].grid_remove()
    Label(root, text="1").grid(column=x, row=y)


root = Tk()

n = 10
m = 10
buttons = []
for i in range(n):
    buttons.append([0] * m)

for i in range(n):
    for j in range(m):
        buttons[i][j] = Button(
            root, text="*", command=lambda x=i, y=j: button_clicked(x, y))
        buttons[i][j].grid(column=i, row=j)


root.mainloop()
