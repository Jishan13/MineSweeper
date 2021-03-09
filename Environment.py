'''
Created on Mar 2, 2021

@author: Jishan Desai and Gazal Arora
'''
import random
class Board(object):
    '''
    classdocs
    '''
    def __init__(self, dim, num_mines):
        self.dim = dim
        self.total_mines = num_mines
        self.board = [['_' for r in range(dim)] for c in range(dim)]
        self.initialize_board()
        self.print_board()
    def initialize_board(self):
        mines_placed = 0
        while mines_placed != self.total_mines:
            loc = random.randint(0,self.dim**2 - 1)
            r = loc // (self.dim)
            c = loc % (self.dim)
            if self.board[r][c] != "x":
                self.board[r][c] = "x"
                mines_placed = mines_placed+1
        self.fill_mine_distances()
    def print_board(self):
        print(" ", end = "\t")
        for i in range(self.dim):
            print(i, end = " ")
        print()
        row_num = 0
        for row in self.board:
            print(row_num,end="\t")
            row_num=row_num+1
            for col in row:
                print(col,end = " ")
            print()
    def fill_mine_distances(self):
        for i in range(self.dim):
            for j in range(self.dim):
                counter = 0
                if self.board[i][j] == "x":
                    continue
                if (i-1) > -1 and self.board[i-1][j] == "x":
                    counter = counter + 1
                if (i+1) < self.dim and self.board[i+1][j] == "x":
                    counter = counter + 1 
                if (j-1) > -1 and self.board[i][j-1] == "x":
                    counter = counter + 1
                if (j+1) < self.dim and self.board[i][j+1] == "x": 
                    counter = counter + 1
                if (i+1) < self.dim and (j+1) < self.dim and self.board[i+1][j+1] == "x":
                    counter = counter + 1
                if (i+1) < self.dim and (j-1) > -1 and self.board[i+1][j-1] == "x":
                    counter = counter + 1
                if (i-1) > -1 and (j-1) > -1 and self.board[i-1][j-1] == "x":
                    counter = counter + 1
                if (i-1) > -1 and (j+1) < self.dim  and self.board[i-1][j+1] == "x":  
                    counter = counter + 1           
                self.board[i][j] = str(counter)
    def get_loc(self,row,col):
        return self.board[row][col]                                        
if __name__ == '__main__':
    dimension = int(input("Enter Dimension: "))
    mine_num = int(input("Enter Mine number: "))
    b = Board(dimension,mine_num)