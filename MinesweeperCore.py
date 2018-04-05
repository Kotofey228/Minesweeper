from pprint import pprint


class Node:
    planted = False
    opened = False
    def ifPlanted(self):
        return planted

    def __repr__(self):
        return "ID:%s" % id(self)


class MinesweeperCore:
    _playfield = []

    def NewGame(self, width, height, bombs):
        self._playfield = [[Node() for j in range(width)]
                          for i in range(height)]
    def GetPlayfield(self):
        return _playfield


def main():
    Core = MinesweeperCore()
    Core.NewGame(10, 10, 15)
    pprint(Core.playfield)


if __name__ == '__main__':
    main()
