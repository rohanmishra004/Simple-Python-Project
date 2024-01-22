#Minesweeper game - build with recursion and classes
import random
import re
#Create a board object
class Board:
    def __init__(self,dim_size, num_bombs):
        #keep track of these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create a board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        #initialize a set to keep track of location that have already been dug
        #we will save (row,col) tuples into this set
        self.dug = set() #if we dig at 0,0 , self.dug={(0,0)}

    def make_new_board(self):
        #construct a new board based on the dim size and num_bombs
        #we are using list of list to represent 2-D board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]
        # we can see how this represents a board!
        #plant the bombs
        bombs_planted =0
        while bombs_planted<self.num_bombs:
            loc = random.randint(0,self.dim_size**2-1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == '*': #this means we have actually planted a bomb there already so keep going
                continue
            board[row][col] ="*"
            bombs_planted+=1
        return board
    

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':#if this is already a bomb , we dont want to calculate aything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)


    def get_num_neighboring_bombs(self,row,col):
        num_neighboring_bombs = 0
        #this checks for bombs at 1 row above and below , and same is the case for columns as well 
        #max and min are added to prevent from going overbounds
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    #our original loc
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs +=1
        return num_neighboring_bombs
    def dig(self, row,col):
        #Sceanrios to encounter
        #Sc 1 - hit a bomb --> game over
        #Sc 2 - dig at location with neighbouring bomb
        #Sc 3 - dig at loc with no bomb , recursively dig neighbours
        self.dug.add((row,col)) #keep track that we have dug
        if self.board[row][col]=='*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0,row-1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue #dont dig as we already know this position
                self.dig(r,c)
        return True
    
    def __str__(self,reveal=False):
        for row in self.board:
            for cell in row:
                if reveal:
                    print(cell, end=' ')
                else:
                    print('X', end=' ')

        print()
    
    # def __str__(self):
    #     # this is a magic function where if you call print on this object,
    #     # it'll print out what this function returns!
    #     # return a string that shows the board to the player

    #     # first let's create a new array that represents what the user would see
    #     visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
    #     for row in range(self.dim_size):
    #         for col in range(self.dim_size):
    #             if (row,col) in self.dug:
    #                 visible_board[row][col] = str(self.board[row][col])
    #             else:
    #                 visible_board[row][col] = ' '
        
    #     # put this together in a string
    #     string_rep = ''
    #     # get max column widths for printing
    #     widths = []
    #     for idx in range(self.dim_size):
    #         columns = map(lambda x: x[idx], visible_board)
    #         widths.append(
    #             len(
    #                 max(columns, key = len)
    #             )
    #         )

    #     # print the csv strings
    #     indices = [i for i in range(self.dim_size)]
    #     indices_row = '   '
    #     cells = []
    #     for idx, col in enumerate(indices):
    #         format = '%-' + str(widths[idx]) + "s"
    #         cells.append(format % (col))
    #     indices_row += '  '.join(cells)
    #     indices_row += '  \n'
        
    #     for i in range(len(visible_board)):
    #         row = visible_board[i]
    #         string_rep += f'{i} |'
    #         cells = []
    #         for idx, col in enumerate(row):
    #             format = '%-' + str(widths[idx]) + "s"
    #             cells.append(format % (col))
    #         string_rep += ' |'.join(cells)
    #         string_rep += ' |\n'

    #     str_len = int(len(string_rep) / self.dim_size)
    #     string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

    #     return string_rep              

def play(dim_size =10, num_bombs=10):
    #Step 1 - create a board
    board = Board(dim_size, num_bombs)

    #Step 2 - Show user the board
    safe=True
    #Step 3a - if location is bomb , show gameover message
    #Step 3b - if location is not a bomb , dig recursively until each square is atleast next to bomb
    #Step 4 - repeat steps 2 and 3a/b until board is filled
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*' ,input('Input row,col : '))
        row , col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col>= board.dim_size:
            print("Invalid Location..")
            continue

        #if its valid , we dig
        safe = board.dig(row,col)
        if not safe:
            #dug a bomb 
            break; #Game over
    
    #2 ways to end - either board complete
    if safe:
        print("VICTORY")
    else: 
        print("GAME OVER")

        board.dug = [[r,c] for r in range(board.dim_size) for c in range(board.dim_size) ]
        print(board)
 
if __name__ == '__main__':
    play()