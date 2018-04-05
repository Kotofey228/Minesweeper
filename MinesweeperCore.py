from pprint import pprint
from random import randint


class Node:
    _planted = False
    _opened = False

    def __init__(self, x, y):
        self.coords = (x, y)

    def ifPlanted(self):
        return self._planted

    def ifOpened(self):
        return self._opened

    def Open(self):
        self._opened = True

    def Plant(self):
        self._planted = True

    def __repr__(self):
        if self._planted:
            return "1"
        else:
            return "0"

# Core is just giving information about what happening while
# opening one or another node and about win or lose, so it is not safe
# from double opening or same things, anyway, nothing will happened.
# You must block corresponding nodes in realization.


class MinesweeperCore:
    _playfield = []  # matrix of nodes
    _safeNodes = 0  # counting safe nodes, 0 = win

    def NewGame(self, width, height, bombs):  # init
        if not(0 <= bombs <= width * height):
            raise Exception("Bombs should be from 0 to %s" % (width * height))
        self._playfield = [[Node(j, i) for j in range(width)]
                           for i in range(height)]
        self._safeNodes = width * height - bombs

        allnodes = [i for i in range(width * height)]

        for i in range(bombs):
            plant = randint(0, len(allnodes) - 1)
            x = allnodes[plant] % width
            y = allnodes[plant] // width
            # at first Y(vertical) then X(horizontal)
            self._playfield[y][x].Plant()
            del allnodes[plant]

    def GetPlayfield(self):
        return self._playfield  # returns current matrix of Node()

    def CheckEnvir(self, x, y):  # counting bombs around that point
        checkNodes = []
        checkNodes.append((x - 1, y - 1))
        checkNodes.append((x - 1, y))
        checkNodes.append((x - 1, y + 1))
        checkNodes.append((x, y - 1))
        checkNodes.append((x, y + 1))
        checkNodes.append((x + 1, y - 1))
        checkNodes.append((x + 1, y))
        checkNodes.append((x + 1, y + 1))
        envir = 0
        for i in range(8):
            try:
                tx, ty = checkNodes[i]
                if (tx < 0 or ty < 0):  # INVERSE INDEXING KOSTYL
                    raise Exception("KOSTYL")
                if self._playfield[ty][tx].ifPlanted():
                    envir += 1
            except Exception:
                pass
        return envir

    def OpenEnvir(self, x, y):  # counting bombs around that point
        openNodes = []
        openNodes.append((x - 1, y - 1))
        openNodes.append((x - 1, y))
        openNodes.append((x - 1, y + 1))
        openNodes.append((x, y - 1))
        openNodes.append((x, y + 1))
        openNodes.append((x + 1, y - 1))
        openNodes.append((x + 1, y))
        openNodes.append((x + 1, y + 1))
        nodesToOpen = []
        for i in range(8):
            try:
                tx, ty = openNodes[i]
                if (tx < 0 or ty < 0):  # INVERSE INDEXING KOSTYL
                    raise Exception("KOSTYL")
                anotherNodesToOpen = self.OpenNode(tx, ty)
                if anotherNodesToOpen != None:
                    for i in range(len(anotherNodesToOpen)):
                        nodesToOpen.append(anotherNodesToOpen[i])
            except Exception:
                pass
        return nodesToOpen

    def OpenNode(self, x, y):
        if self._playfield[y][x].ifOpened():  # check for opened
            return None
        self._playfield[y][x].Open()  # after that open it

        if self._playfield[y][x].ifPlanted():  # check for DEADPOINT
            return "LOOSE"

        envir = self.CheckEnvir(x, y)          # you are lucky...
        nodesToOpen = []
        nodesToOpen.append((x, y, envir))
        if envir > 0:
            return nodesToOpen
        else:
            anotherNodesToOpen = self.OpenEnvir(x, y)
            for i in range(len(anotherNodesToOpen)):
                nodesToOpen.append(anotherNodesToOpen[i])
        return nodesToOpen


def main():
    Core = MinesweeperCore()
    Core.NewGame(10, 10, 20)
    pprint(Core.GetPlayfield())
    print(Core.OpenNode(0, 0))


if __name__ == '__main__':
    main()
