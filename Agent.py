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
        self.num_mines = num_mines #total num of interpreted + accidentally opened mines
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
        self.total_hidden = self.dim**2
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
            self.num_safe_squares(r, c, 0)
        
            
    def num_covered_neigbors(self,r,c):
        covered_neighbors = []
        if (r-1) > -1 and self.board[r-1][c].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r-1][c])
        if (r+1) < self.dim and self.board[r+1][c].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r+1][c])
        if (c-1) > -1 and self.board[r][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r][c-1])
        if (c+1) < self.dim and self.board[r][c+1].isCovered: 
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r][c+1])
        if (r+1) < self.dim and (c+1) < self.dim and self.board[r+1][c+1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r+1][c+1])
        if (r+1) < self.dim and (c-1) > -1 and self.board[r+1][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r+1][c-1])
        if (r-1) > -1 and (c-1) > -1 and self.board[r-1][c-1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r-1][c-1])
        if (r-1) > -1 and (c+1) < self.dim  and self.board[r-1][c+1].isCovered:
            self.board[r][c].num_covered=self.board[r][c].num_covered +1
            covered_neighbors.append(self.board[r-1][c+1])
        return self.board[r][c].num_covered, covered_neighbors
    
    def num_safe_squares(self,r,c, flag):
        num_unhidden = 0
        if (r-1) > -1 and self.board[r-1][c].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r-1][c].isCovered==False:
                self.board[r-1][c].num_mines += 1  
                self.basic_agent_algo(r-1, c, self.board[r-1][c].clue) 
                num_unhidden+=1    
        if (r+1) < self.dim and self.board[r+1][c].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r+1][c].isCovered==False:
                self.board[r+1][c].num_mines += 1
                self.basic_agent_algo(r+1, c, self.board[r+1][c].clue) 
                num_unhidden+=1  
        if (c-1) > -1 and self.board[r][c-1].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r][c-1].isCovered==False:
                self.board[r][c-1].num_mines += 1
                self.basic_agent_algo(r, c-1, self.board[r][c-1].clue)  
                num_unhidden+=1 
        if (c+1) < self.dim and self.board[r][c+1].isSafe: 
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r][c+1].isCovered==False:
                self.board[r][c+1].num_mines += 1
                self.basic_agent_algo(r, c+1, self.board[r][c+1].clue)  
                num_unhidden+=1 
        if (r+1) < self.dim and (c+1) < self.dim and self.board[r+1][c+1].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r+1][c+1].isCovered==False:
                self.board[r+1][c+1].num_mines += 1
                self.basic_agent_algo(r+1, c+1, self.board[r+1][c+1].clue) 
                num_unhidden+=1  
        if (r+1) < self.dim and (c-1) > -1 and self.board[r+1][c-1].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r+1][c-1].isCovered==False:
                self.board[r+1][c-1].num_mines += 1
                self.basic_agent_algo(r+1, c-1, self.board[r+1][c-1].clue) 
                num_unhidden+=1  
        if (r-1) > -1 and (c-1) > -1 and self.board[r-1][c-1].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r-1][c-1].isCovered==False:
                self.board[r-1][c-1].num_mines += 1
                self.basic_agent_algo(r-1, c-1, self.board[r-1][c-1].clue)  
                num_unhidden+=1 
        if (r-1) > -1 and (c+1) < self.dim  and self.board[r-1][c+1].isSafe:
            if flag==1:
                self.board[r][c].num_safe=self.board[r][c].num_safe+1
            elif flag==0 and self.board[r-1][c+1].isCovered==False:
                self.board[r-1][c+1].num_mines += 1
                self.basic_agent_algo(r-1, c+1, self.board[r-1][c+1].clue)  
                num_unhidden+=1 
        self.total_hidden -= num_unhidden
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
    def mark_unhide_neighbor(self,i,j,b):
        unhide_counter=0
        if (i-1) > -1 and self.board[i-1][j].isCovered:
            self.update_query(i-1, j, b)
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and self.board[i+1][j].isCovered:
            self.update_query(i+1, j, b)
            unhide_counter = unhide_counter+1
        if (j-1) > -1 and self.board[i][j-1].isCovered:
            self.update_query(i, j-1, b)
            unhide_counter = unhide_counter+1
        if (j+1) < self.dim and self.board[i][j+1].isCovered: 
            self.update_query(i,j+1, b)
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and (j+1) < self.dim and self.board[i+1][j+1].isCovered:
            self.update_query(i+1,j+1, b)
            unhide_counter = unhide_counter+1
        if (i+1) < self.dim and (j-1) > -1 and self.board[i+1][j-1].isCovered:
            self.update_query(i+1,j-1, b)
            unhide_counter = unhide_counter+1
        if (i-1) > -1 and (j-1) > -1 and self.board[i-1][j-1].isCovered:
            self.update_query(i-1,j-1, b)
            unhide_counter = unhide_counter+1
        if (i-1) > -1 and (j+1) < self.dim and self.board[i-1][j+1].isCovered:
            self.update_query(i-1,j+1, b)
            unhide_counter = unhide_counter+1
        return unhide_counter   
    
    def pick_random_neighbor(self, b, covered_neighbors, num_covered):
        k = random.randint(1,num_covered)
        r, c = covered_neighbors[k-1].get_loc()
        self.update_query(r,c,b)   
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
                if col.isCovered == True:
                    print('_',end = " ")
                elif col.isCovered == False:
                    if col.clue == -1:
                        print('X',end = " ")
                    else:
                        print(col.clue,end = " ")
            print()
            
    def basic_agent_algo(self, r, c, curr):
        num_unhidden = 0
        hidden, hidden_neighbors = self.num_covered_neigbors(r, c)
        safe_neighbors = self.num_safe_squares(r, c, 1)
        total_neighbor = self.get_num_neigbor(r, c)
        #self.board[r][c].num_mines = self.board[r][c].num_mines + (total_neighbor - safe_neighbors)
        
        if (curr-self.board[r][c].num_mines) == hidden: #all hidden neighbors are mines
            num_unhidden = self.mark_unhide_neighbor(r, c, b)
            self.score+=num_unhidden
        if ((total_neighbor - curr)-safe_neighbors) == hidden: #all hidden neighbors are safe
            num_unhidden = self.mark_unhide_neighbor(r, c, b)
        
        return num_unhidden
    
    def basic_agent(self, b):
        
        next_loc = self.board[0][0]
        
        
        while self.total_hidden > 0:
            
            curr_sqr = next_loc
            r,c = curr_sqr.get_loc()
            self.update_query(r,c,b)
            curr = self.board[r][c].clue
            self.total_hidden -= 1
            if curr!=-1:
                num_unhidden = self.basic_agent_algo(r, c, curr)
                self.total_hidden -= num_unhidden
            print("Querying: " + str(r) +", " + str(c)+" ,total hidden: " +str(self.total_hidden))
            self.print_board()
            while (True):
                loc = random.randint(0,self.dim**2 - 1)
                r = loc // (self.dim)
                c = loc % (self.dim)
                if self.board[r][c].isCovered==True:
                    next_loc = self.board[r][c]
                    break
        print("Score = "+str(self.score))            
if __name__ == '__main__':
    dimension = int(input("Enter Dimension: "))
    mine_num = int(input("Enter Mine number: "))
    b = en.Board(dimension,mine_num)
    a = Agent(dimension)
    a.basic_agent(b)        