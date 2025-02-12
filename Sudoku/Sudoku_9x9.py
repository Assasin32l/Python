import random


def checkBoard(board, row, col, num):
    def checkRow(board, row, num):
        for i in range(9):
            if board[row][i] == num:
                return False
        
        return True

    def checkCol(board, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
        
        return True

    def checkBox(board, row, col, num):
        for i in range(3):
            for j in range(3):
                if board[i + row][j + col] == num:
                    return False
        
        return True
    

    if checkRow(board, row, num) and checkCol(board, col, num) and checkBox(board, row - row % 3, col - col % 3, num):
        return True


def createBoard(board, colorBoard, difficulty = 0):
    def createDiagonal(board):
        nums = list(range(1, 10))

        random.shuffle(nums)

        for i in range(9):
            board[i][i] = nums[i]
        
        return board


    def fillRemaining(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if checkBoard(board, i, j, num):
                            board[i][j] = num

                            if fillRemaining(board):
                                return True
                            
                            board[i][j] = 0
                    
                    return False
        
        return True


    def removeCells(board, difficulty):
        probabilities = [0, 1, 2, 3, 4, 5, 6, 6, 6]

        for i in range(9):
            for j in range(9):
                if random.choice(probabilities) <= difficulty:
                    board[i][j] = 0
                    colorBoard[i][j] = 1


    board = createDiagonal(board)

    while not fillRemaining(board):
        print("Failed to fill the board.")
        continue
    
    removeCells(board, colorBoard, difficulty)

    return board, colorBoard


def printBoard(board):
    row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    print("   | 1  2  3 | 4  5  6 | 7  8  9")
    print("---+---------+---------+---------")

    for i in range(9):
        row = " " + row_labels[i] + " |"

        for j in range(9):
            if board[i][j] == 0:
                row += "   "
            else:
                row += " " + str(board[i][j]) + " "

            if (j + 1) % 3 == 0 and j != 8:
                row += "|"
        
        print(row)

        if (i + 1) % 3 == 0 and i != 8:
            print("---+---------+---------+---------")


def solveBoard(board):


    printBoard(board)

    s = True
    while slct[0] not in "ABCDEFGHI" or int(slct[1]) not in range(1, 10) or int(slct[3]) not in range(1, 10) or board[ord(slct[0]) - 65][int(slct[1]) - 1] != 0:
        if s == True:
            slct = input("\nSelect a cell to fill and the number to add to the cell: ")
            s = False
        else:
            slct = input("\nInvalid input. Please try again: ")
    
    board[ord(slct[0]) - 65][int(slct[1]) - 1] = int(slct[3])

    return 0

if __name__ == "__main__":
    board = [[0 for _ in range(9)] for _ in range(9)]
    colorBoard = [[0 for _ in range(9)] for _ in range(9)]

    difficulty = int(input("Enter the difficulty level (1-5): "))

    board, colorBoard = createBoard(board, colorBoard, difficulty)
    solveBoard(board, colorBoard)