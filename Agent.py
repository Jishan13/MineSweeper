'''
Created on Mar 9, 2021

@author: Jishan Desai and Gazal Arora
'''
import Environment as en
class Square(object):
    def __init__(self,num_hidden,num_safe,num_mines,clue):
        self.num_hidden = num_hidden
        self.num_safe = num_safe
        self.num_mines = num_mines
        self.clue = clue     
class Agent(object):
    def __init__(self,dim):
        self.dim = dim 
        self.board = [[(Square(8, 0, 0, 0)) for r in range(dim)] for c in range(dim)]
        self.score = 0
        
    def set_score(self,n):
        self.score = n
    def update_query(self,r,c,b):
        res=b.get_loc(r, c)
        
if __name__ == '__main__':
    dimension = int(input("Enter Dimension: "))
    mine_num = int(input("Enter Mine number: "))
    b = en.Board(dimension,mine_num)
    a = Agent(dimension)
    a. update_query(0, 0,b)        