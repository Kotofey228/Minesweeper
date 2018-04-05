from tkinter import *

import MinesweeperCore

global buttons  # Array of playfield buttons
Core = MinesweeperCore.MinesweeperCore()


def Loose():
    print("Loose")


def button_clicked(x, y):
    nodesToOpen = Core.OpenNode(x, y)
    if nodesToOpen == None:
        return None
    if nodesToOpen == "LOOSE":
        Loose()
        return None
    for i in range(len(nodesToOpen)):
        tx = nodesToOpen[i][0]
        ty = nodesToOpen[i][1]
        envir = nodesToOpen[i][2]

        openNode(tx, ty, envir)
    # buttons[x][y].config(state=DISABLED)
    # buttons[x][y].grid_remove();


def openNode(x, y, envir):
    print(x,y,envir)
    buttons[x][y].grid_remove()
    Label(root, text=envir).grid(column=x, row=y)


root = Tk()

n = 10
m = 10
Core.NewGame(n, m, 15)
buttons = []
for i in range(n):
    buttons.append([0] * m)

for i in range(n):
    for j in range(m):
        buttons[i][j] = Button(
            root, text="*", command=lambda x=i, y=j: button_clicked(x, y))
        buttons[i][j].grid(column=i, row=j)


root.mainloop()
