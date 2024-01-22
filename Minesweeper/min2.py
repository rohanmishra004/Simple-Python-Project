import random

class Minesweeper:

    #initialize the board
    def __init__(self,rows,cols,mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.place_mines()
        #method calculates the number of mines surrounding each cell.
        self.calculate_numbers()

    #place mines randomly 
    def place_mines(self):
        mine_spots = random.sample(range(self.rows*self.cols), self.mines)
        for spot in mine_spots:
            row = spot // self.cols
            col = spot % self.cols
            self.board[row][col]='M'

    def calculate_numbers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]=='M':
                    continue
                count =0
                for x in range(max(0,i-1), min(self.rows, i+2)):
                    for y in range(max(0, j - 1), min(self.cols, j + 2)):
                        if self.board[x][y]=='M':
                            count+=1
                self.board[i][j] = str(count) if count>0 else ' '

    def display_board(self, reveal=False):
        for row in self.board:
            print(' '.join(row if reveal else map(lambda x: x if x=='M' or x==' ' else '_', row )))

    def play(self):
        while True:
            self.display_board()
            row = int(input("Enter row : "))
            col = int(input("Enter column : "))

            if self.board[row][col] == 'M':
                print("game over")
                break
            elif self.board[row][col] == ' ':
                print('You cleared an empty spot')
            else:
                print(f'There are {self.board[row][col]} mines nearby')
            
            self.board[row][col] = 'C'

            #Check for win condition
            if all(cell == 'C' or cell.isdigit() for row in self.board for cell in row if cell != 'M'):
                print("Congratulations! You won!")
                break



if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mines = int(input("Enter the number of mines: "))

    game = Minesweeper(rows, cols, mines)
    game.play()