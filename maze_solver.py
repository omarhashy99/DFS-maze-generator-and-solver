from turtle import *
from maze_generator import Maze


def drow_maze():
    generator = Maze(15, 15)
    global maze
    maze = generator.get_maze()

    t = Turtle()
    t.shape("square")
    t.color("black")
    t.penup()
    t.speed(10)

    global maze_map
    global maze_map_reversed
    maze_map = dict()
    maze_map_reversed = dict()

    for i in range(len(maze)):
        for u in range(len(maze[i])):
            ch = maze[i][u]
            x = -260 + (u * 20) - 50
            y = 250 - (i * 20) + 50
            maze_map[(x, y)] = (i, u)
            maze_map_reversed[(i, u)] = (x, y)
            if ch == "X":
                t.goto(x, y)
                t.stamp()
            elif i == 1 and u == 1:
                t2.goto(x, y)
    t.hideturtle()


def dfs(current_x, current_y, x, y) -> list:
    if (
        (current_x, current_y) in dfs_visited
        or maze[current_x][current_y] == "X"
        or (x == current_x and y == current_y)
    ):
        return [(current_x, current_y)]

    dfs_visited[(current_x, current_y)] = True

    liDFS = dfs(current_x, current_y + 1, x, y)
    if liDFS[-1] == (x, y):
        return [(current_x, current_y)] + liDFS

    liDFS = dfs(current_x, current_y - 1, x, y)
    if liDFS[-1] == (x, y):
        return [(current_x, current_y)] + liDFS

    liDFS = dfs(current_x + 1, current_y, x, y)
    if len(liDFS) > 0 and liDFS[-1] == (x, y):
        return [(current_x, current_y)] + liDFS

    liDFS = dfs(current_x - 1, current_y, x, y)
    if liDFS[-1] == (x, y):
        return [(current_x, current_y)] + liDFS

    return [(current_x, current_y)]


def do_nothing(*args):
    pass


def on_point_click(x, y):
    win.onscreenclick(do_nothing)
    for temx, temy in maze_map.keys():
        if abs(temx - x) <= 10 and abs(temy - y) <= 10:
            x, y = maze_map[(temx, temy)]
            break
    else:
        print("out of the maze!!!!!!!")
        win.onscreenclick(on_point_click)
        return

    if maze[x][y] == "X":
        print("wall!!!!!!!!!!")
        win.onscreenclick(on_point_click)
        return
    global dfs_visited, t2_x_pos, t2_y_pos
    dfs_visited = dict()

    li = dfs(t2_x_pos, t2_y_pos, x, y)
    t2.clear()
    t2.pendown()
    t2.pensize(6)
    t2.pencolor("green1")
    for pos in li:
        x1, y1 = maze_map_reversed[pos]
        t2.goto(x1, y1)
    t2_x_pos, t2_y_pos = pos
    win.onscreenclick(on_point_click)


def main():
    global win, t2, t2_x_pos, t2_y_pos
    win = Screen()
    win.setup(1000, 800)
    win.onscreenclick(on_point_click)
    t2_x_pos, t2_y_pos = 1, 1
    t2 = Turtle()
    t2.penup()
    t2.hideturtle()
    t2.shape("circle")
    t2.color("green")
    t2.shapesize(0.7)
    t2.speed(2)

    drow_maze()

    t2.showturtle()
    done()


if __name__ == "__main__":
    main()
