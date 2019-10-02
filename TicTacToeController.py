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
    return (board[7] == symbol and board[8] == symbol and board[9] == symbol) or
    (board[4] == symbol and board[5] == symbol and board[6] == symbol) or
    (board[1] == symbol and board[2] == symbol and board[3] == symbol) or
    (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
    (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
    (board[3] == symbol and board[6] == symbol and board[9] == symbol) or
    (board[1] == symbol and board[5] == symbol and board[9] == symbol) or 
    (board[3] == symbol and board[5] == symbol and board[7] == symbol)

def playerMove():
    pass

def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    pass

def main():
    pass

main()
