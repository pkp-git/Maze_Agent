import turtle
import time
import random
import tkinter as tk

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Solving Program")
wn.setup(1300, 700)

# the five classes below are drawing turtle images to construct the maze.
class Maze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):               # Visited Cell
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):               # Frontier Cell
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):                # Start Cell
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
          # point turtle to point down
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):           # End Cell and Path
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

def Gridmake(lenx, leny):
    gridin=''
    for i in range(leny - 1):
        if i == 0:
            for j in range(lenx):
                gridin += '+'
            gridx.append(gridin)
            gridin = ''
        else:
            for j in range(lenx - 2):
                if j == 0:
                    gridin += '+'
                rand = random.choice(["+", " ", " "])
                gridin += rand
            gridin += '+'
            gridx.append(gridin)
            gridin = ''
    for j in range(lenx):
        gridin += '+'
    gridx.append(gridin)


def StartEnd(sx, sy, ex, ey):
    listin = gridx[sy]
    listout = []
    for i in listin:
        listout.append(i)
    listout[sx] = 's'
    listin = ''
    for i in listout:
        listin += i
    gridx[sy] = listin

    listin = gridx[ey]
    listout = []
    for i in listin:
        listout.append(i)
    listout[ex] = 'e'
    listin = ''
    for i in listout:
        listin += i
    gridx[ey] = listin

def Display_maze(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -288
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()

    start = turtle.textinput("Parameters of Start", "Co-ordinates of Start Point: (ex. 2,2)")
    end = turtle.textinput("Parameters of End", "Co-ordinates of End Point: (ex. 11,12)")
    temp = start.split(",")
    sx = int(temp[0])
    sy = int(temp[1])
    temp = end.split(",")
    ex = int(temp[0])
    ey = int(temp[1])
    StartEnd(sx, sy, ex, ey)


def Setup_Maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # iterate through each line in the grid
        for x in range(len(grid[y])):          # iterate through each character in the line
            character = grid[y][x]             # assign the variable character to the y and x positions of the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -288
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":                   # if character contains a '+'
                maze.goto(screen_x, screen_y)      # move pen to the x and y location and
                maze.stamp()                       # stamp a copy of the white turtle on the screen
                walls.append((screen_x, screen_y)) # add cell to the walls list

            if character == " ":                    # if no character found
                path.append((screen_x, screen_y))   # add to path list

            if character == "e":                    # if cell contains an 'e'
                yellow.goto(screen_x, screen_y)     # move pen to the x and y location and
                yellow.stamp()                      # stamp a copy of the yellow turtle on the screen
                end_x, end_y = screen_x, screen_y   # assign end locations variables to end_x and end_y
                path.append((screen_x, screen_y))   # add cell to the path list

            if character == "s":                       # if cell contains a "s"
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)           # send red turtle to start position

def DFS_and_Map(x,y):
    frontier.append((x, y))                            # add the x and y position to the frontier list
    solution[x, y] = x, y                              # add x and y to the solution dictionary
    while len(frontier) > 0:                           # loop until the frontier list is empty
        time.sleep(0)                                  # change this value to make the animation go slower
        current = (x,y)                                # current cell equals x and  y positions

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            cellleft = (x - 24, y)
            frontier.append(cellleft)
            solution[cellleft] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellleft)        # blue turtle goto the  cellleft position
            blue.stamp()               # stamp a blue turtle on the maze

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            celldown = (x, y - 24)
            frontier.append(celldown)
            solution[celldown] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(celldown)
            blue.stamp()

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            cellright = (x + 24, y)
            frontier.append(cellright)
            solution[cellright] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellright)
            blue.stamp()

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            cellup = (x, y + 24)
            frontier.append(cellup)
            solution[cellup] = x, y  # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cellup)
            blue.stamp()

        x, y = frontier.pop()           # remove last entry from the frontier list and assign to x and y
        visited.append(current)         # add current cell to visited list
        green.goto(x,y)                 # green turtle goto x and y position
        green.stamp()                   # stamp a copy of the green turtle on the maze
        if (x,y) == (end_x, end_y):     # makes sure the yellow end turtle is still visible after been visited
            yellow.stamp()              # restamp the yellow turtle at the end position
        if (x,y) == (start_x, start_y): # makes sure the red start turtle is still visible after been visited
            red.stamp()                 # restamp the red turtle at the start position

def Sol(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    try:
        while (x, y) != (start_x, start_y):
            yellow.goto(solution[x, y])        # move the turtle to the value of solution ()
            yellow.stamp()
            x, y = solution[x, y]
    except:
        root = tk.Tk()
        root.title("  ERROR  ")
        l1 = tk.Label(root, text="Path Does Not Exist!!", font=("Arial", 15), width=40, height=20)
        l1.pack()
        root.mainloop()

global gridx, gridin
gridx = []
gridin = ''
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = []
frontier = []
solution = {}
start_x = 0
start_y = 0
end_x = 0
end_y = 0

lenx = int(turtle.numinput("Maze Dimensions", "Maze Width (Recommended: 15<VAL<35)"))
leny = int(turtle.numinput("Maze Dimensions", "Maze Length (Recommended: 15<VAL<35)"))

Gridmake(lenx+2, leny+2)
Display_maze(gridx)
Setup_Maze(gridx)

DFS_and_Map(start_x, start_y)
Sol(end_x, end_y)

wn.exitonclick()