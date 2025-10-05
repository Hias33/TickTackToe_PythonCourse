from random import randrange

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

game_over = False

def PrintBoard(pBoard):
    for row in pBoard:
        for col in row:
            print(str(col), end=' ')
        print()
    print()

def EnterMove(pBoard, pPlayer, pPosition):
    row = pPosition // 3
    col = pPosition % 3
    pBoard[row][col] = pPlayer
    PrintBoard(pBoard)

def CheckWin(pBoard):
    # Check rows
    for row in pBoard:
        if row[0] == row[1] == row[2]:
            return True

    # Check columns
    for col in range(3):
        if pBoard[0][col] == pBoard[1][col] == pBoard[2][col]:
            return True

    # Check diagonals
    if pBoard[0][0] == pBoard[1][1] == pBoard[2][2]:
        return True
    if pBoard[0][2] == pBoard[1][1] == pBoard[2][0]:
        return True

    return False

def CheckForFreeSpaces(pBoard):
    freeSpaces = []
    for row in pBoard:
        for col in row:
            if col != "X" and col != "O":
                freeSpaces.append(col)
    return freeSpaces

def EnterPlayerMove(pBoard):
    freeSpaces = CheckForFreeSpaces(pBoard)
    try:
        position = int(input("Enter your move: "))
        if position not in freeSpaces:
            print("Invalid move, try again.")
    except ValueError:
        print("Please enter a valid number.")

    EnterMove(pBoard, "X", position - 1)

def EnterComputerMove(pBoard):
    freeSpaces = CheckForFreeSpaces(pBoard)
    if not freeSpaces:
        return

    compPosition = freeSpaces[randrange(len(freeSpaces))]
    print(f"Computer's move: {compPosition}")
    EnterMove(pBoard, "O", compPosition - 1)

def main():
    global game_over
    PrintBoard(board)
    while not game_over:
        # Player turn
        EnterPlayerMove(board)
        if CheckWin(board):
            print("You win!")
            game_over = True
            break

        # Check tie
        if not CheckForFreeSpaces(board):
            print("It's a tie!")
            break

        # Computer turn
        EnterComputerMove(board)
        if CheckWin(board):
            print("Computer wins!")
            game_over = True
            break

        # Check tie after computer move
        if not CheckForFreeSpaces(board):
            print("It's a tie!")
            break

main()
