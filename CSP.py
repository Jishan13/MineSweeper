'''
Created on Mar 16, 2021

@author: Jishan Desai and Gazal Arora

'''
'''
create_variables()
    keep adding the variable name, 
    the square from which we got that variable 
    and the clue-num of mines to the dictionary
    
    dict will look like:
    { Square at (1,5):  { (x1, x2): [ (solution combos), (), .... ] }, "Square at 1,6":  }
'''

import Agent

def create_variables(agent, board):
    agent.print_board()
    data = {}
    #num = 0
    for r in range(agent.dim):
        for c in range(agent.dim):
            if(board[r][c].clue > 0):
                _, covered_neighbors = agent.num_covered_neigbors(r,c)
                variables_list = []
                for neighbor in covered_neighbors:
                    if (neighbor.variable != ''):
                        variables_list.append(neighbor.variable)
                    elif(neighbor.variable == ''):
                        neighbor.variable = 'x'+ str(neighbor.row) + str(neighbor.col)
                        #print(f'For ({r}, {c}), variables are: {neighbor.variable}')
                        #num+=1
                        variables_list.append(neighbor.variable)
                        
                variable_tuple = tuple(variables_list)
                #print(f'For ({r}, {c}), variables are: {variable_tuple} len of tup: {len(variable_tuple)}')
                if (variable_tuple):
                    data[board[r][c]] = { variable_tuple: [] }
                    
    keyList = assign_values(data, board)
    #print(data)
    print()  
    return data, keyList

def decToBinary(n):
    return bin(n).replace("0b", "")

def generateSolutions(num_variables, summ):
    solutions = []
    for i in range(2**num_variables):
        sttr = decToBinary(i)
        
        #print("dec to binary: " + sttr)
        while(len(sttr) < num_variables):
            sttr = "0" + sttr
        k = sttr.count("1")
        #print("after count: "+ sttr)
        if(k==summ):
            if(len(sttr)==1 and num_variables == 1):
                sttr = "(" + sttr+ ",)"
                sttr = eval(sttr)
                solutions.append(sttr)
                continue
            sttr = sttr.replace("", ",")
            sttr = sttr.strip(",")
            #print("in summ: " + sttr)
            sttr = eval(sttr)
            solutions.append(sttr)
    print(solutions)
    return solutions     
#def most_pop():
    
    
def assign_values(data,a):
    print("Here")
    keyList = data.keys()
    fringe = []
    for key in keyList:
        r, c = key.get_loc()
        Sqr = a[r][c]
        clue = Sqr.clue
        mines = Sqr.num_mines
        summ = clue - mines
        temp = data[key]
        #print(temp)
        
        keys = temp.keys()
        #print(keys)
        for k in keys:
            #print(temp[k])
            num_variables = len(k)
            temp[k] = (generateSolutions(num_variables, summ))
            for sol in temp[k]:
                #print("sol: ", end =" ")
                #print(sol) 
                fringe.append(sol)
    print(fringe)
    return keyList
def improved_agent(agent, board):
    fringe, KeyList = create_variables(agent, board)
    solutions =[]
    for key in KeyList:
        solutions.append(fringe.pop(key))
        
    
        