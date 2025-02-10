import random


def createBoard(board):
    def createDiagonal(board):
        nums = list(range(1, 10))

        random.shuffle(nums)

        for i in range(9):
            board[i][i] = nums[i]
        
        return board


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


    def fillRemaining(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if checkRow(board, i, num) and checkCol(board, j, num) and checkBox(board, i - i % 3, j - j % 3, num):
                            board[i][j] = num

                            if fillRemaining(board):
                                return True
                            
                            board[i][j] = 0
                    
                    return False
        
        return True

    board = createDiagonal(board)

    while not fillRemaining(board):
        print("Failed to fill the board.")
        continue

    return board


def printBoard(board):
    row_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    print("   | 1  2  3 | 4  5  6 | 7  8  9")
    print("---+---------+---------+---------")

    for i in range(9):
        row = " " + row_labels[i] + " |"

        for j in range(9):
            row += " " + str(board[i][j]) + " "

            if (j + 1) % 3 == 0 and j != 8:
                row += "|"
        
        print(row)

        if (i + 1) % 3 == 0 and i != 8:
            print("---+---------+---------+---------")


if __name__ == "__main__":
    board = [[0 for _ in range(9)] for _ in range(9)]
    board = createBoard(board)
    printBoard(board)