import time
import os
from pyfiglet import Figlet
import getch

blank = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
gcursorpos = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
cursorpos = 0
state = "title"
p1 = True
winC = False
f = Figlet(font='slant')


def start():
    os.system("clear")
    print("Welcome to \n")
    print(f.renderText('Py-Tac-Toe!'))
    time.sleep(2)


def title():
    os.system("clear")
    print("PY-TAC-TOE")
    print("\n\n")
    print("Use WASD to select and space to confirm")
    if cursorpos == 0:
        print("-> Controls")
    else:
        print("Controls")
    if cursorpos == 1:
        print("-> Start 2 player mode")
    else:
        print("Start 2 player mode")
    if cursorpos == 2:
        print("-> Start AI mode - Coming Soon, Maybe?")
    else:
        print("Start AI mode - Coming Soon, Maybe?")
    if cursorpos == 3:
        print("-> Quit")
    else:
        print("Quit")


def controls():
    os.system("clear")
    print("Py-Tac-Toe\n\n")
    print("Use WASD to navigate the menus and game board")
    print("Press space to select or play")
    print("-> Back")


def pointer(pos):
    gcursorpos = []
    for i in range(0, pos):
        gcursorpos.append(" ")
    gcursorpos.append(">")
    for i in range(pos + 1, 9):
        gcursorpos.append(" ")
    return gcursorpos


def reset():
    global p1, positions, cursorpos, state
    p1 = True
    positions = [" "] * 9
    cursorpos = 1
    state = "title"
    redraw(state)


def win():
    os.system("clear")
    if p1 is False:
        player = "PLAYER 1"
    elif p1 is True:
        player = "PLAYER 2"
    print(f.renderText('You win,'))
    print('\n')
    print(f.renderText(f'{player}!'))
    time.sleep(3)
    reset()


def vs():
    os.system("clear")
    cursorarray = pointer(cursorpos)

    print(
        cursorarray[0]
        + positions[0]
        + " |"
        + cursorarray[1]
        + positions[1]
        + " |"
        + cursorarray[2]
        + positions[2]
        + " "
    )
    print("---+---+---")
    print(
        cursorarray[3]
        + positions[3]
        + " |"
        + cursorarray[4]
        + positions[4]
        + " |"
        + cursorarray[5]
        + positions[5]
        + " "
    )
    print("---+---+---")
    print(
        cursorarray[6]
        + positions[6]
        + " |"
        + cursorarray[7]
        + positions[7]
        + " |"
        + cursorarray[8]
        + positions[8]
        + " "
    )
    if wincheck():
        print("\nPress space to continue")
    elif " " not in positions and not wincheck():
        print("\nNo more moves!")
        time.sleep(2)
        reset()


def redraw(st):
    if st == "title":
        title()
    elif st == "controls":
        controls()
    elif st == "play2P":
        vs()
    elif st == "win":
        win()
        global state
        state = 'title'


def wincheck():
    if positions[0] == positions[4] == positions[8] and positions[0] != " ":
        return "win"
    elif positions[0] == positions[1] == positions[2] and positions[0] != " ":
        return "win"
    elif positions[0] == positions[3] == positions[6] and positions[0] != " ":
        return "win"
    elif positions[1] == positions[4] == positions[7] and positions[1] != " ":
        return "win"
    elif positions[2] == positions[5] == positions[8] and positions[2] != " ":
        return "win"
    elif positions[2] == positions[4] == positions[6] and positions[2] != " ":
        return "win"
    elif positions[3] == positions[4] == positions[5] and positions[3] != " ":
        return "win"
    elif positions[6] == positions[7] == positions[8] and positions[6] != " ":
        return "win"


start()

while True:
    redraw(state)
    keypress = getch.getch()
    if state == "title":
        if keypress == 'w':
            if cursorpos - 1 < 0:
                pass
            else:
                cursorpos = cursorpos - 1
        elif keypress == 's':
            if cursorpos + 1 > 3:
                pass
            else:
                cursorpos = cursorpos + 1
        elif keypress == " ":
            if cursorpos == 0:
                state = "controls"
            elif cursorpos == 1:
                state = "play2P"
                cursorpos = 4
            elif cursorpos == 2:
                state = "title"
                cursorpos = 2
            elif cursorpos == 3:
                os.system("clear")
                break
    elif state == "controls":
        if keypress == " ":
            state = "title"
    elif state == "play2P":
        if wincheck():
            state = wincheck()
        if keypress == "w" and cursorpos - 3 >= 0:
            cursorpos = cursorpos - 3
        elif keypress == "s" and cursorpos + 3 <= 8:
            cursorpos = cursorpos + 3
        elif keypress == "a" and cursorpos - 1 >= 0:
            cursorpos = cursorpos - 1
        elif keypress == "d" and cursorpos + 1 <= 8:
            cursorpos = cursorpos + 1
        elif keypress == " " and positions[cursorpos] == " ":
            if p1 is True:
                positions[cursorpos] = "X"
            else:
                positions[cursorpos] = "O"
            p1 = not p1
