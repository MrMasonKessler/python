'''
While I have gotten practice from the TicTacToe tkinter project, there are some commands here that I still needed to look up, and do not claim credit for.
A great help for me was Vakus on stack overflow, as they used button commands that I didn't know about. (Stuff like sticky, lambda, and using a button list instead of making
the buttons manually.)
'''

from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Minesweeper GUI")
#WIDTH = 600
#HEIGHT = 600
size = 4
bombs = 3
board = []
buttons = []
#root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(True,True)

#I can add pictures for the numbers and bombs if I want, and if I add flag functionality, I will have an image for that too.

def play():
    makePopup()
    makeBombBoard()

def makeBombBoard():
    #Make the field
    global size,bombs,board
    board = []
    for x in range(0,size):
        board.append([])
        for y in range(0,size):
            board[x].append(0)
    #Distribute bombs
    for _ in range(0,bombs):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        while board[x][y] == 'X':
            x = random.randint(0,size-1)
            y = random.randint(0,size-1)            
        board[x][y] == 'X'
        if(board[y][x] != 'X'):
                board[y][x] = 'X'
                if(y >= 0 and y <= size-2):
                    if board[y+1][x] != 'X':
                        board[y+1][x] += 1 # bottom center
                if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
                    if board[y+1][x+1] != 'X':
                        board[y+1][x+1] += 1 # bottom right
                if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
                    if board[y+1][x-1] != 'X':
                        board[y+1][x-1] += 1 # bottom left
                #Check top next:
                if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
                    if board[y-1][x] != 'X':
                        board[y-1][x] += 1 # top center
                if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
                    if board[y-1][x+1] != 'X':
                        board[y-1][x+1] += 1 # top right
                if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
                    if board[y-1][x-1] != 'X':
                        board[y-1][x-1] += 1 # top left
                #Check sides:
                if (x >= 1 and x <= size-1):
                    if board[y][x-1] != 'X':
                        board[y][x-1] += 1
                if (x >= 0 and x <= size-2):
                    if board[y][x+1] != 'X':
                        board[y][x+1] += 1
    return board

def makePopup():
    global size, buttons
    Button(root, text="Restart", command=restartGame).grid(row=0, column=0, columnspan=size, sticky=N+W+S+E)
    buttons = []
    for x in range(0,size):
        buttons.append([])
        for y in range(0,size):
            button = Button(root,text=" ", width=2,command=lambda x=x,y=y:press(x,y))
            button.grid(row=x+1,column=y,sticky=N+S+W+E)
            buttons[x].append(button)


def restartGame():
    pass

def press(row,col): #STILL NEED TO FINISH THIS FUNCTION
    global size, board, buttons
    buttons[row][col]["text"]=str(board[row][col])
    if board[row][col] == 'X':
        buttons[row][col]["text"] = "*"
        messagebox.showinfo("Game over, you lose!")
        for x in range(0,size):
            for y in range(0,size):
                buttons[x][y]["text"] = "*"
    else:
        pass
    checkWin()

def checkWin():
    global buttons,board,size
    win = True
    for x in range(0,size):
        for y in range(0,size):
            if board[x][y] != 'X' and buttons[x][y]["state"] == "normal":
                win = False
    if win:
        messagebox.showinfo("Game over, you win!")



play()
root.mainloop()
