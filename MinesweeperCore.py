from pprint import pprint
from random import randint


class Node:
    _planted = False
    def __init__(self, x, y):
        self.coords = (x,y)

    def ifPlanted(self):
        return self._planted
    def Plant(self):
        self._planted = True

    def __repr__(self):
        if self._planted:
            return "1"
        else:
            return "0"

# Core is just giving information about what happening while
# opening one or another node and about win or lose, so it is not safe
# from double opening or same things. You must block corresponding nodes in
# realization.


class MinesweeperCore:
    _playfield = []  # matrix of nodes
    _safeNodes = 0  # counting safe nodes, 0 = win

    def NewGame(self, width, height, bombs):  # init
        self._playfield = [[Node(j,i) for j in range(width)]
                           for i in range(height)]
        self._safeNodes = width * height - bombs

        allnodes = [i for i in range(width*height)]
        for i in range(bombs):
            plant = randint(0,len(allnodes))
            x = allnodes[plant] % width
            y = allnodes[plant] // width
            self._playfield[x][y].Plant()
            del allnodes[plant]

    def GetPlayfield(self):
        return self._playfield

    def OpenNode(self, x, y):
        pass


def main():
    Core = MinesweeperCore()
    Core.NewGame(10, 10, 50)
    pprint(Core.GetPlayfield())


if __name__ == '__main__':
    main()
