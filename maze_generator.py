import random


class Maze:
    def __init__(self, rows: int, cols: int) -> None:
        self.__maze = []
        self.__rows = rows * 2 + 1
        self.__cols = cols * 2 + 1
        self.__fill_maze_with_walls()
        self.__break_walls()

    def __fill_maze_with_walls(self):
        for i in range(self.__rows):
            self.__maze.append([])
            for u in range(self.__cols):
                if (
                    u == 0
                    or i == 0
                    or u == self.__cols - 1
                    or i == self.__rows - 1
                    or u % 2 == 0
                    or i % 2 == 0
                ):
                    self.__maze[i].append("X")
                else:
                    self.__maze[i].append(" ")

    def __break_walls(self):
        self.vis = dict()
        x = random.randrange(1, self.__rows, 2)
        y = random.randrange(1, self.__cols, 2)

        self.__dfs(x, y)

    def __dfs(self, x: int, y: int):
        self.vis[(x, y)] = True
        self.__directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        random.shuffle(self.__directions)

        for add_x, add_y in self.__directions:
            if (
                x + add_x < self.__rows - 1
                and y + add_y < self.__cols - 1
                and add_x + x > 0
                and y + add_y > 0
                and (add_x + x, y + add_y) not in self.vis
            ):
                self.__dfs(add_x + x, y + add_y)
                self.__maze[x + add_x // 2][y + add_y // 2] = " "

    def get_maze(self):
        return self.__maze
