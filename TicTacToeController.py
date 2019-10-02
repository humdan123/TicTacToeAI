board = [' ' for x in range(10)]

def insertSymbol(symbol, pos):
  board[pos] = symbol

def isSpaceFree(pos):
   return board[pos] == ' '

def displayBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(board, symbol):
    return (board[7] == symbol and board[8] == symbol and board[9] == symbol) or(board[4] == symbol and board[5] == symbol and board[6] == symbol) or(board[1] == symbol and board[2] == symbol and board[3] == symbol) or(board[1] == symbol and board[4] == symbol and board[7] == symbol) or(board[2] == symbol and board[5] == symbol and board[8] == symbol) or(board[3] == symbol and board[6] == symbol and board[9] == symbol) or(board[1] == symbol and board[5] == symbol and board[9] == symbol) or(board[3] == symbol and board[5] == symbol and board[7] == symbol)

def playerMove():
    run = True

    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move =int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertSymbol('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range (1-9)! ")
        except:
            print("Please type a number! ")

def compMove():
    possibleMoves = [x for x, symbol in enumerate(board) if symbol == ' ' and x != 0]
    move = 0

    for symb in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = symb
            if isWinner(boardCopy,symb):
                move = i
                return move
        cornersOpen = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
        if len(cornersOpen) > 0:
            move = selectRandom(edgesOpen)
        return move


def selectRandom(lis):
    import random
    ln = len(lis)
    r = random.randrange(0, ln)
    return lis[r]

def isBoardFull(board):
    return not board.count(' ') > 1

def main():
    print('Welcome to Tic Tac Toe')
    displayBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            displayBoard(board)
        else:
            print("Sorry, O's won this time!")
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("Tie Game!")
            else:
                insertSymbol('O', move)
                print("Computer places an 'O' in position :", move)
                displayBoard(board)
        else:
            print("Congratulations! You won this time!")
            break

    if isBoardFull(board):
        print('Tied Game!')


main()
