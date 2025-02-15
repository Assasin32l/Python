from math import sqrt
import random


def checkBoard(board, row, col, num):
    def checkRow():
        for i in range(len(board)):
            if board[row][i] == num:
                return False
            
        return True

    def checkCol():
        for i in range(len(board)):
            if board[i][col] == num:
                return False
            
        return True

    def checkBox():
        boxColSize = int(sqrt(len(board)))
        boxRowSize = len(board) // boxColSize

        startRow = row - row % boxRowSize
        startCol = col - col % boxColSize

        for i in range(boxRowSize):
            for j in range(boxColSize):
                if board[i + startRow][j + startCol] == num:
                    return False
                
        return True


    return checkRow() and checkCol() and checkBox()


def checkSize(boardSize):
    if boardSize < 4 or boardSize > 9:
        return False

    boxColSize = int(sqrt(boardSize))
    boxRowSize = boardSize // boxColSize

    return boxRowSize * boxColSize == boardSize


def createBoard(board, difficulty = 0):
    def createDiagonal():
        nums = list(range(1, len(board) + 1))

        for i in range(len(board)):
            if i % boxRowSize == 0 or i % boxColSize == 0:
                random.shuffle(nums)
            
            board[i][i] = nums[i % len(board)]

    def fillRemaining():
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    nums = list(range(1, len(board) + 1))
                    random.shuffle(nums)

                    for num in nums:
                        if checkBoard(board, i, j, num):
                            board[i][j] = num

                            if fillRemaining():
                                return True
                            
                    board[i][j] = 0

                    return False

        return True

    def removeDigits():
        probability = [0, 1, 2, 3, 4, 5, 6, 6, 6]

        for i in range(len(board)):
            for j in range(len(board)):
                if random.choice(probability) <= difficulty:
                    board[i][j] = 0


    boxColSize = int(sqrt(len(board)))
    boxRowSize = len(board) // boxColSize

    createDiagonal()

    while not fillRemaining():
        print("Failed to fill the board. Trying again.")
        continue
    
    removeDigits()
    
    return board


def printBoard(board, colorBoard):
    colors = {0: "\033[0m", 1: "\033[32m", 2: "\033[93m", 3: "\033[91m", 4: "\033[33m"}
    rowLabels = [i + 65 for i in range(len(board))]
    boxColSize = int(sqrt(len(board)))
    boxRowSize = len(board) // boxColSize


    print(end = "\n   |")

    for i in range(len(board)):
        print(end = f" {i + 1} ")
        
        if (i + 1) % boxColSize == 0:
            print(end = "|")


    rowBlank = "\n---+"

    for i in range(len(board)):
        rowBlank += "---"

        if (i + 1) % boxColSize == 0:
            rowBlank += "+"
    
    print(end = rowBlank)


    for i in range(len(board)):
        print(f"\n {chr(rowLabels[i])} |", end = "")

        for j in range(len(board)):
            color = colors[colorBoard[i][j]]

            if board[i][j] == 0:
                if colorBoard[i][j] in range(2, 5):
                    print(color, "*", colors[0], end = "")

                else:
                    print(end = "   ")

            else:
                print(color, str(board[i][j]), colors[0], end = "")
            
            if (j + 1) % boxColSize == 0:
                print(end = "|")
        
        if (i + 1) % boxRowSize == 0:
            print(end = rowBlank)


def solveBoard(board, colorBoard):
    while True:
        printBoard(board, colorBoard)

        if all(board[i][j] != 0 for i in range(len(board)) for j in range(len(board))):
            print("\n\nCongratulations! You have completed the board.")
            break

        s = True
        slct = ""

        while ( not slct or not len(slct) > 2 or ord(slct[0]) not in range(len(board) + 65) 
                or int(slct[1]) not in range(len(board) + 1) or int(slct[2]) not in range(len(board) + 1) 
                or board[ord(slct[0]) - 65][int(slct[1]) - 1] != 0 ):
            
            if s == True:
                slct = input("\n\nSelect a cell to fill and the number to add to the cell: ").upper().replace(" ", "")
                s = False
            
            else:
                slct = input("\n\nInvalid input. Please try again: ").upper().replace(" ", "")
        
        row = ord(slct[0]) - 65
        col = int(slct[1]) - 1
        num = int(slct[2])
        action = slct[3] if len(slct) > 3 else ""

        if action == "P":
            if colorBoard[row][col] == 3:
                colorBoard[row][col] = 4
            
            else:
                colorBoard[row][col] = 2
        
        elif action == "B":
            if colorBoard[row][col] == 2:
                colorBoard[row][col] = 4
            
            else:
                colorBoard[row][col] = 3
        
        elif checkBoard(board, row, col, num):
            board[row][col] = num
            colorBoard[row][col] = 1
    
    return board, colorBoard


def sudokuMenu():
    boardSize = int(input("Enter the size of the board: "))

    while not checkSize(boardSize):
        boardSize = int(input("Invalid input. Enter the size of the board: "))

    board = [[0 for i in range(boardSize)] for j in range(boardSize)]
    colorBoard = [[0 for i in range(boardSize)] for j in range(boardSize)]


    difficulty = int(input("Enter the difficulty level (1-5): "))

    while difficulty not in range(6):
        difficulty = int(input("Invalid input. Enter the difficulty level (1-5): "))


    board = createBoard(board, difficulty)
    board, colorBoard = solveBoard(board, colorBoard)


if __name__ == "__main__":
    sudokuMenu()