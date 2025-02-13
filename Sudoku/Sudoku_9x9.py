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

        for i in range(9):
            if i % 3 == 0:
                random.shuffle(nums)

            board[i][i] = nums[i % 9]

        return board


    def fillRemaining(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)

                    for num in nums:
                        if checkBoard(board, i, j, num):
                            board[i][j] = num

                            if fillRemaining(board):
                                return True
                            
                            board[i][j] = 0

                    return False
                
        return True


    def removeCells(board, colorBoard, difficulty):
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


def printBoard(board, colorBoard):
    row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    colors = {0: "\033[0m", 1: "\033[32m", 2: "\033[93m", 3: "\033[91m", 4: "\033[33m"}

    print("Predictions and Blocks:")

    for i in range(9):
        for j in range(9):
            if colorBoard[i][j] in [2, 3, 4]:
                cell = row_labels[i] + str(j + 1)
                color = colors[colorBoard[i][j]]

                print(f"{color}{cell}{colors[0]}: {colorBoard[i][j]}")

    print("\n   | 1  2  3 | 4  5  6 | 7  8  9")
    print("---+---------+---------+---------")

    for i in range(9):
        row = " " + row_labels[i] + " |"

        for j in range(9):
            color = colors[colorBoard[i][j]]

            if board[i][j] == 0:
                if colorBoard[i][j] == 2:
                    row += color + " * " + colors[0]

                elif colorBoard[i][j] == 3:
                    row += color + " * " + colors[0]

                elif colorBoard[i][j] == 4:
                    row += color + " * " + colors[0]

                else:
                    row += "   "

            else:
                row += color + " " + str(board[i][j]) + " " + colors[0]

            if (j + 1) % 3 == 0 and j != 8:
                row += "|"

        print(row)

        if (i + 1) % 3 == 0 and i != 8:
            print("---+---------+---------+---------")


def solveBoard(board, colorBoard):
    while True:
        printBoard(board, colorBoard)

        if all(board[i][j] != 0 for i in range(9) for j in range(9)):
            print("Congratulations! You have completed the board.")
            break

        s = True
        slct = ""

        while not slct or slct[0] not in "ABCDEFGHI" or int(slct[1]) not in range(1, 10) or int(slct[3]) not in range(1, 10) or board[ord(slct[0]) - 65][int(slct[1]) - 1] != 0:
            if s == True:
                slct = input("\nSelect a cell to fill and the number to add to the cell: ")
                s = False

            else:
                slct = input("\nInvalid input. Please try again: ")

        row = ord(slct[0]) - 65
        col = int(slct[1]) - 1
        num = int(slct[3])
        action = slct[5] if len(slct) > 4 else ""

        if action == "p":
            if colorBoard[row][col] == 3:
                colorBoard[row][col] = 4

            else:
                colorBoard[row][col] = 2

        elif action == "b":
            if colorBoard[row][col] == 2:
                colorBoard[row][col] = 4

            else:
                colorBoard[row][col] = 3

        elif checkBoard(board, row, col, num):
            board[row][col] = num
            colorBoard[row][col] = 1


if __name__ == "__main__":
    board = [[0 for _ in range(9)] for _ in range(9)]
    colorBoard = [[0 for _ in range(9)] for _ in range(9)]

    difficulty = int(input("Enter the difficulty level (1-5): "))

    board, colorBoard = createBoard(board, colorBoard, difficulty)
    solveBoard(board, colorBoard)