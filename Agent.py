'''
Created on Mar 9, 2021

@author: Jishan Desai and Gazal Arora
'''
import Environment as en
import random

class Square(object):
    def __init__(self,num_covered,num_safe,num_mines,clue, row, col,isCovered):
        self.row = row
        self.col = col
        self.num_covered = num_covered
        self.num_safe = num_safe
        self.num_mines = num_mines #num of identified mines
        self.isSafe = False
        self.clue = clue    
        ''' clue = 0 means covered square
        clue = -1 means mine
        clue = some integer means real clue use it!!'''
        self.isCovered = isCovered 
    def get_loc(self):
        return self.row,self.col
class Agent(object):
    def __init__(self,dim):
        self.dim = dim 
        self.board = [[(Square(8, 0, 0, 0, r, c,True)) for r in range(dim)] for c in range(dim)]
        self.score = 0
    def set_score(self,n):
        self.score = n
        
    def update_query(self,r,c,b):
        res=b.get_loc(r, c)
        if(res!="x"):
            self.board[r][c].clue = int(res)
            self.board[r][c].isSafe = True
            self.board[r][c].isCovered = False
        else:
            self.board[r][c].clue = -1
            self.board[r][c].isSafe = False
            self.board[r][c].isCovered = False
            
    def num_covered_neigbors(self,r,c):
        if (r-1) > -1 and self.board[r-1][c].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (r+1) < self.dim and self.board[r+1][c].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (c-1) > -1 and self.board[r][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (c+1) < self.dim and self.board[r][c+1].isCovered: 
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (r+1) < self.dim and (c+1) < self.dim and self.board[r+1][c+1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (r+1) < self.dim and (c-1) > -1 and self.board[r+1][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (r-1) > -1 and (c-1) > -1 and self.board[r-1][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        if (r-1) > -1 and (c+1) < self.dim  and self.board[r-1][c+1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
        return self.board[r][c].num_covered
    
    def num_safe_squares(self,r,c):
        if (r-1) > -1 and self.board[r-1][c].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (r+1) < self.dim and self.board[r+1][c].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (c-1) > -1 and self.board[r][c-1].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (c+1) < self.dim and self.board[r][c+1].isSafe: 
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (r+1) < self.dim and (c+1) < self.dim and self.board[r+1][c+1].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (r+1) < self.dim and (c-1) > -1 and self.board[r+1][c-1].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (r-1) > -1 and (c-1) > -1 and self.board[r-1][c-1].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        if (r-1) > -1 and (c+1) < self.dim  and self.board[r-1][c+1].isSafe:
            self.board[r][c].num_safe=self.board[r][c].num_safe+1
        return self.board[r][c].num_safe
    
    def get_num_neigbor(self,i,j):
        counter = 0
        if (i-1) > -1 :
            counter = counter + 1
        if (i+1) < self.dim :
            counter = counter + 1 
        if (j-1) > -1:
            counter = counter + 1
        if (j+1) < self.dim : 
            counter = counter + 1
        if (i+1) < self.dim and (j+1) < self.dim :
            counter = counter + 1
        if (i+1) < self.dim and (j-1) > -1 :
            counter = counter + 1
        if (i-1) > -1 and (j-1) > -1:
            counter = counter + 1
        if (i-1) > -1 and (j+1) < self.dim :
            counter = counter + 1
        return counter    
    # flag = 0 means safe
    # flag = 1 means mine 
    def mark_unhide_neighbor(self,i,j,flag,next_list,b):
        unhide_counter=0
        if (i-1) > -1 and self.board[i-1][j].isCovered:
            if flag == 0:
                self.board[i-1][j].isSafe = True
                self.update_query(i-1, j, b)
                next_list.append(self.board[i-1][j])
            self.board[i-1][j].isCovered = False
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and self.board[i+1][j].isCovered:
            if flag == 0:
                self.board[i+1][j].isSafe = True
                self.update_query(i+1, j, b)
                next_list.append(self.board[i+1][j])
            self.board[i+1][j].isCovered = False
            unhide_counter = unhide_counter+1
        if (j-1) > -1 and self.board[i][j-1].isCovered:
            if flag == 0:
                self.board[i][j-1].isSafe = True
                self.update_query(i, j-1, b)
                next_list.append(self.board[i][j-1])
            self.board[i][j-1].isCovered = False
            unhide_counter = unhide_counter+1
        if (j+1) < self.dim and self.board[i][j+1].isCovered: 
            if flag==0:
                self.board[i][j+1].isSafe = True
                self.update_query(i,j+1, b)
                next_list.append(self.board[i][j+1])
            self.board[i][j+1].isCovered = False
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and (j+1) < self.dim and self.board[i+1][j+1].isCovered:
            if flag == 0:
                self.board[i+1][j+1].isSafe = True
                self.update_query(i+1,j+1, b)
                next_list.append(self.board[i+1][j+1])
            self.board[i+1][j+1].isCovered = False
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and (j-1) > -1 and self.board[i+1][j-1].isCovered:
            if flag == 0:
                self.board[i+1][j-1].isSafe = True
                self.update_query(i+1,j-1, b)
                next_list.append(self.board[i+1][j-1])
            self.board[i+1][j-1].isCovered = False
            unhide_counter = unhide_counter+1
        if (i-1) > -1 and (j-1) > -1 and self.board[i-1][j-1].isCovered:
            if flag == 0:
                self.board[i-1][j-1].isSafe = True
                self.update_query(i-1,j-1, b)
                next_list.append(self.board[i-1][j-1])
            self.board[i-1][j-1].isCovered = False
            unhide_counter = unhide_counter+1
        if (i-1) > -1 and (j+1) < self.dim and self.board[i-1][j+1].isCovered:
            if flag == 0:
                self.board[i][j+1].isSafe = True
                self.update_query(i-1,j+1, b)
                next_list.append(self.board[i-1][j+1])
            self.board[i-1][j+1].isCovered = False
            unhide_counter = unhide_counter+1
        return unhide_counter        
    def basic_agent(self, b):
        next_loc_list = []
        next_loc_list.append(self.board[0][0])
        total_hidden = self.dim
        reveal_mine = 0
        while total_hidden != 0:
            curr_sqr = next_loc_list.pop(0)
            r,c = curr_sqr.get_loc()
            curr_sqr.isCovered = False
            self.update_query(r,c,b)
            curr = self.board[r][c].clue
            if curr == -1 and r==0 and c==0:
                k = random.randint(1,3)
                if(k==1):
                    self.update_query(0,1,b)
                elif k == 2:
                    self.update_query(1,0,b)
                elif k == 3:
                    self.update_query(1,1,b)
                reveal_mine = reveal_mine + 1
            elif curr != -1:
                self.board[r][c].isSafe = True 
                covered = self.num_covered_neigbors(r, c)
                rev_safe_square = self.num_safe_squares(r, c)
                total_neigbor = self.get_num_neigbor(r, c)
                if (total_neigbor - curr) == covered:
                    num_unhidden = self.mark_unhide_neighbor(r, c, 0,next_loc_list,b)
                    total_hidden = total_hidden - num_unhidden
            
            
            
if __name__ == '__main__':
    dimension = int(input("Enter Dimension: "))
    mine_num = int(input("Enter Mine number: "))
    b = en.Board(dimension,mine_num)
    a = Agent(dimension)
    a.basic_agent(b)        