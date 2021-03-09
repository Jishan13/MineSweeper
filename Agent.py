'''
Created on Mar 9, 2021

@author: Jishan Desai and Gazal Arora
'''
import Environment as en
import random

class Square(object):
    def __init__(self,num_covered,num_safe,num_mines,clue, row, col):
        self.row = row
        self.col = col
        self.num_covered = num_covered
        self.num_safe = num_safe
        self.num_mines = num_mines #num of identified mines
        #self.flag = 0 # 0 for safe, 1 for mine flag
        self.clue = clue    
        ''' clue = 0 means covered square
        clue = -1 means mine
        clue = some integer means real clue use it!!''' 
class Agent(object):
    def __init__(self,dim):
        self.dim = dim 
        self.board = [[(Square(8, 0, 0, 0, r, c)) for r in range(dim)] for c in range(dim)]
        self.score = 0
        
    def set_score(self,n):
        self.score = n
        
    def update_query(self,r,c,b):
        res=b.get_loc(r, c)
        if(res!="x"):
            self.board[r][c].clue = int(res)
        else:
            self.board[r][c].clue = 1
    def basic_agent(self, b):
        safe_list = []
        self.update_query(0,0,b)
        curr = self.board[0][0].clue
        if curr == -1:
            #out of (0,1), (1,0) and (1,1) atleast one has to be safe
            self.board[0][0].num_safe = 1
            self.board[0][0].num_covered = 3
            k = random.randint(1,3)
            if(k==1):
                #safe_list.append(self.board[0][1])
                self.update_query(0,1,b)
            elif k == 2:
                #safe_list.append(self.board[1][0])
                self.update_query(1,0,b)
            elif k == 3:
                #safe_list.append(self.board[1][1])
                self.update_query(1,1,b)
        elif curr == 1:
            #randomly selecting which cell is a mine
            k = random.randint(1,3)
            if(k==1):
                self.board[0][1].clue = -1
            elif k == 2:
                self.board[1][0].clue = -1
            elif k == 3:
                self.board[1][1].clue = -1
        elif curr == 2:
            #randomly selecting which cell is safe
            k = random.randint(1,3)
            if(k==1):
                self.update_query(0,1,b)
            elif k == 2:
                self.update_query(1,0,b)
            elif k == 3:
                self.update_query(1,1,b)
        elif curr == 3:
            self.board[0][1].clue = -1
            self.board[1][0].clue = -1
            self.board[1][1].clue = -1
            
             
                
            
            
            
if __name__ == '__main__':
    dimension = int(input("Enter Dimension: "))
    mine_num = int(input("Enter Mine number: "))
    b = en.Board(dimension,mine_num)
    a = Agent(dimension)
    a.basic_agent(b)        