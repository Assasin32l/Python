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
    
    def checkBox(row, col):
        boxRow = int(sqrt(len(board)))
        boxCol = int(len(board) / boxRow)

        row -= row % boxRow
        col -= col % boxCol

        for i in range(boxRow):
            for j in range(boxCol):
                if board[i + row][j + col] == num:
                    return False
        
        return True
    

    if checkRow() and checkCol() and checkBox(row, col):
        return True
    
    return False


def checkSize(boardSize):
    boxRowSize = int(sqrt(boardSize))
    boxColSize = boardSize / boxRowSize

    if boxColSize % 1 != 0:
        return False
    
    return True


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
    

    boxRowSize = int(sqrt(len(board)))
    boxColSize = int(len(board) / boxRowSize)

    createDiagonal()

    while not fillRemaining():
        print("Failed to fill the board. Trying again.")
        continue
    
    removeDigits()
    
    return board


def printBoard(board, colorBoard):
    colors = {0: "\033[0m", 1: "\033[32m", 2: "\033[93m", 3: "\033[91m", 4: "\033[33m"}
    rowLabels = [i + 65 for i in range(len(board))]
    boxRowSize = int(sqrt(len(board)))
    boxColSize = int(len(board) / boxRowSize)


    print("\n   |", end = "")

    for i in range(len(board)):
        print(f" {i + 1} ", end = "")

        if (i + 1) % boxRowSize == 0:
            print("|", end = "")

    
    rowBlank = "\n---+"

    for i in range(len(board)):
        rowBlank += "---"

        if (i + 1) % boxRowSize == 0:
            rowBlank += "+"
    
    print(rowBlank, end = "")


    for i in range(len(board)):
        print(f"\n {chr(rowLabels[i])} |", end = "")

        for j in range(len(board)):
            color = colors[colorBoard[i][j]]

            if board[i][j] == 0:
                if colorBoard[i][j] in range(2, 5):
                    print(color, " * ", colors[0], end = "")
                
                else:
                    print("   ", end = "")
            
            else:
                print(color, str(board[i][j]), colors[0], end = "")
            
            if (j + 1) % boxRowSize == 0:
                print("|", end = "")
        
        if (i + 1) % boxColSize == 0:
            print(rowBlank, end = "")


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

    printBoard(board, colorBoard)
        

if __name__ == "__main__":
    sudokuMenu()