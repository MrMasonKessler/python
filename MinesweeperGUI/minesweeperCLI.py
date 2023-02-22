import random
import os
import time

#DUPLICATE BOMBS ARE POSSIBLE, MUST FIX


#How a typical grid looks, use for reference:
# 0 1 2 3 4
# 1
# 2
# 3
# 4

def boardChoice():
    clear_term()
    choice = int(input("Please enter the what difficulty you would like to play on, 1 for easy, 2 for medium, 3 for hard: "))
    return choice

def makeBombBoard(choice):
    if choice == 1:
        size = 5
        bombs = 3
    if choice == 2:
        size = 7
        bombs = 7
    if choice == 3:
        size = 10
        bombs = 25
    count = 0
    array = [[0 for row in range(size)] for col in range(size)] #Makes the array used in generating the board
    for bomb in range(bombs):
        while count < bombs:
            x = random.randint(0,size-1) #Picks an x variable in the board to be a bomb
            y = random.randint(0,size-1) #Picks a y variable in the board to be a bomb
            if(array[y][x] != 'X'):
                array[y][x] = 'X'
                if(y >= 0 and y <= size-2):
                    if array[y+1][x] != 'X':
                        array[y+1][x] += 1 # bottom center
                if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
                    if array[y+1][x+1] != 'X':
                        array[y+1][x+1] += 1 # bottom right
                if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
                    if array[y+1][x-1] != 'X':
                        array[y+1][x-1] += 1 # bottom left
                #Check top next:
                if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
                    if array[y-1][x] != 'X':
                        array[y-1][x] += 1 # top center
                if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
                    if array[y-1][x+1] != 'X':
                        array[y-1][x+1] += 1 # top right
                if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
                    if array[y-1][x-1] != 'X':
                        array[y-1][x-1] += 1 # top left
                #Check sides:
                if (x >= 1 and x <= size-1):
                    if array[y][x-1] != 'X':
                        array[y][x-1] += 1
                if (x >= 0 and x <= size-2):
                    if array[y][x+1] != 'X':
                        array[y][x+1] += 1
                        count += 1 
            else:
                continue
    return array

def seenBoard(choice):
    if choice == 1:
        size = 5
    if choice == 2:
        size = 7
    if choice == 3:
        size = 10
    array = [['-' for row in range(size)] for col in range(size)]
    return array

def showBoard(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
        print("")

def winCon(board):
    #Check to see the number of moves made. Since I don't have a flag system yet, the number of moves in a win should be equal to size*size-bombs
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True

def clear_term(): #This function is to clear the terminal every time the game is started.
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def minesweeper():
    #status = True
    #while status:
        choice = boardChoice()
        if choice == 1:
            size = 5
            bombs = 3
        if choice == 2:
            size = 7
            bombs = 17
        if choice == 3:
            size = 10
            bombs = 36
        bombBoard = makeBombBoard(choice)
        print()
        print("Generating board . . .")
        time.sleep(1.5)
        print()
        clear_term()
        print("MINESWEEPER CLI GAME\n")
        playerBoard = seenBoard(choice)
        showBoard(playerBoard)
        moves = 0
        while True:
            print("Please pick which cell you wish to open")
            x = int(input("X: "))
            y = int(input("Y: "))
            time.sleep(0.5)
            clear_term()
            if bombBoard[y][x]=='X':
                print("You lose! Game over!")
                showBoard(bombBoard)
                break
            else:
                playerBoard[y][x] = bombBoard[y][x]
                showBoard(playerBoard)
                moves += 1
            if moves == (size*size-bombs):
                print("You win! Congratulations!")
                showBoard(bombBoard)
                break


def main():
    minesweeper()

if __name__ == "__main__":
    main()