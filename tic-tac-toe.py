
class TicTacToe:
    def __init__(self) -> None:
        self.player = 'X'
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

    def display_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=' ')
            print()

    def play(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Wrong row or col")
        elif self.board[row][col] == '-':
            self.board[row][col] = self.player
            self.player = 'X' if self.player == 'O' else 'O'
        else:
            print("Error, position is occupied")

    def get_winner(self):

        # checks for winner in horizonal row 
        for i in range(3):
            if self.board[i] == ['X','X','X']:
                return "X"
            
            if self.board[i] == ['O','O','O']:
                return "O"
               
        # check for winner in vertial 
        for i in range(3):
            if all(self.board[j][i] == 'X' for j in range(3)):
                return 'X'
            if all(self.board[j][i] == 'O' for j in range(3)):
                return 'O'

        # check for winner in diagonal
        if self.board[1][1] != '-':
            if self.board[0][0] == self.board[1][1] ==  self.board[2][2] == 'X':
                return 'X'
            if self.board[0][0] == self.board[1][1] ==  self.board[2][2] == 'O':
                return 'O'
            if self.board[0][2] == self.board[1][1] ==  self.board[2][0] == 'X':
                return 'X'
            if self.board[0][2] == self.board[1][1] ==  self.board[2][0] == 'O':
                return 'O'

    # is a tie function
    def is_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board [i][j] == '-':
                    return False
        return True 

            
game = TicTacToe()
while True:
    print(game.player, "plays")
    game.display_board()
    row = int(input("Row: "))
    col = int(input("Col: "))
    game.play(row, col)
    winner = game.get_winner()
    if winner is not None:
        print(winner, "wins")
        break
    if game.is_tie() is True:
        print("It's a tie")
        break
    



# tic = [
#     ['X','O','X'],
#     ['X','-','X'],
#     ['X','O','O'],
# ]

# x = 5 # x becomes 5 
# x == 5 # checks if the values is 5

# if tic[0][0] == tic[1][0] and tic[1][0] == tic[2][0]:
#     print("we have a winner")


# for i in range(3):
#     print(tic[i])



# if tic[0] == ['X','X','X'] or tic[0] == ['O','O','O']:
#     print('we have a winner')

# else:
#     print("la caca no winner yet! :<")

