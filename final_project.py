#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Final project: Tic-tac-toe game"""
"""
Created on Sun Apr 18 12:00:47 2021

@author: indeshwarchaudhary
"""

import sys
import random
class Tic_Tac_Toe:
    player = 'X'
    opponent = 'O'
    
    A = -99999      #initialize the A represent the Alpha symbol
    B = 99999       #initialize the B reprents the Beta symbol
  
    
    #return utility of board
    def utility(self, board, player):
        
         #checking wheather all the X or O  are in the same rows
        for i in range(len(board)):   
            if board[i][0] ==  board[i][1] and board[i][1] == board[i][2]:     
                if board[i][0] == self.player:
                    return 1
                elif board[i][0] == self.opponent:
                    return -1
        
        
        
        #check wheather all the X or O are  in same column
        for i in range(len(board)):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] == self.player:
                    return 1
                elif board[0][i] == self.opponent:
                    return -1
                
        
        #Checking whether left diagnonal has X or O
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == self.player:
                return 1
            elif board[0][0] == self.opponent:
                return -1
            
         #Checking whether right diagnonal has X or O
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == self.player:
                return 1
            elif board[0][2] == self.opponent:
                return -1
        
        return 0 # return zero if draw
                    
    
    #this function return False if it is non terminal state
    def terminal(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '_':   #check whether board is empty or not
                    return False
        
        return True
    
  
    def alpha_beta_pruning(self, board, isMax): 
       
        point = self.utility(board, self.player) #compute the utility of the board
        
        
        if point == 1:            #if max win, return 1
            return point
        
        if point == -1:          #if min win, return -1
            return point
        
        
        if self.terminal(board) == True:  #if the game is tie, return 0
            return 0
        
        if isMax == True:               #max turn
            best_score = -99999         #contains the best score of board
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == '_':          #if any place is empty, place player
                        board[i][j] = self.player
                        
                        #recursive call of alpha_beta_pruning method
                        #compute the maximum score from min player
                        best_score = max(best_score, self.alpha_beta_pruning(board, not isMax))    
                        
                        board[i][j] = '_' #undo the all taken moves
                           
                        
                        
        if isMax == False:              #min turn
            best_score = 99999          #contains the best score of board
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == '_':                 #if any place is empty, place opponent
                    
                        if best_score > self.A:            #if best_score is greater than Alpha, explore the remaining node   
                            board[i][j] = self.opponent    #place the opponent player in the empty place
                            
                            #recursive call of minimax method
                            #compute the minimum score from max player
                            best_score = min(best_score, self.alpha_beta_pruning(board, not isMax))     
                        
                            board[i][j] = '_' #undo the all taken moves
                            
                            if best_score < self.B:         #update the value of Beta if best_score is less than Beta 
                                self.B = best_score
                                self.A = self.B             #update Alpha
                        
                            
                        else:                               # If Alpa is greater than the best_score, no need to explore remaining node
                              break
                        
                        
        return best_score
                      
    #traverse all the possible move
    #and then return best move
    def actions(self, board, player):
       
        best_Move = (-1,-1)       #contains the indexes of best move 
        
        if player == self.player:
            best_heurestic = -99999         #cotains best value of board
            for i in range(len(board)):
                for j in range(len(board)):
                
                    if board[i][j]  == '_':    #check which position of board is empty
                        board[i][j] = self.player      #place the player at that postion
                    
                        current_heurestic = self.alpha_beta_pruning(board, False)      #evaluate the board
                    
                        board[i][j] = '_'                             #undo the board
                    
                        if current_heurestic > best_heurestic:
                            best_heurestic = current_heurestic        #update the best_heurestic
                            best_Move = (i,j)                         #update the best_Move
                            
        elif player == self.opponent:
            best_heurestic = 99999        #cotains best value of board
            for i in range(len(board)):
                for j in range(len(board)):
                
                    if board[i][j]  == '_':    #check which position of board is empty
                        board[i][j] = self.opponent      #place the player at that postion
                    
                        current_heurestic = self.alpha_beta_pruning(board, True)      #evaluate the board
                    
                        board[i][j] = '_'                             #undo the board
                    
                        if current_heurestic < best_heurestic:
                            best_heurestic = current_heurestic        #update the best_heurestic
                            best_Move = (i,j)                         #update the best_Move
                            
                        
                            
                                          
        return best_Move
        
    #return the best  board after a player completing  actions
    def result(self, board, i,j, ply):
       
        board[i][j] = ply
                    
        return board
    
    
    #this function plays game human vs computer
    def human_V_computer(self, board):
     
        isMax = False
        while True:
            if isMax == True:
                a = self.actions(board, self.player)        #compute the all possible moves and returns the indexes of best moves   
                i, j = a                       # 'i'  and 'j' are indexes of row and column of a board
                self.result(board, i, j, self.player);        #return the board after  computer taking its turn
                isMax = False
            
             
            if self.terminal(board) == False and isMax == False:       # if the current board is not in terminal state, do the following
                isMax = True
                print("Computer turn:")
                for k in range(len(board)):     #print the current board
                    print(board[k])
                    
                if self.utility(board, self.player) == 1:  #check whether computer win
                    print("You Lose");
                    break
                elif self.utility(board, self.opponent) == -1: #check whether  user win
                    print("You won")
                    break
                
                inp = input("Enter indexes of position where you want to place 'O' :")  #user input place
                c = inp.split(',')
                i = int(c[0])
                j = int(c[1])
                
                self.result(board, i,j, self.opponent)  #return the board after user taking his/her turn
                for k in range(len(board)):     #print the current board
                    print(board[k])      
                
            else:              #check whether game is tie                      
                print("Tie")
            
                break  #break the loop
                
    #this function plays game Max Vs Min
    def computer_V_computer(self, board):
        isMax = False          #initialize isMax to False
        
        while True:
            if isMax == True:
                a = self.actions(board, self.player)        #compute the all possible moves of max and returns the indexes of best moves   
                i, j = a                                    # 'i'  and 'j' are indexes of row and column of a board
                self.result(board, i, j, self.player);      #return the board after  max taking its turn
        
                isMax = False                                                       
             
            if self.terminal(board) == False and isMax == False:       # if the current board is non terminal state, do the following
                isMax = True
                print("Max turn")
                for k in range(len(board)):     #print the current board
                    print(board[k])
                    
                if self.utility(board, self.player) == 1:  #check whether max win
                    print("Max won");
                    break
                elif self.utility(board, self.opponent) == -1: #check whether  min win
                    print("Min won")
                    break
                
                o = self.actions(board, self.opponent)   #compute the all possible moves of min and returns the indexes of best moves 
                i, j = o
                self.result(board, i,j, self.opponent)  #return the board after min taking its turn
                
                print("Min turn")
                for k in range(len(board)):     #print the current board
                    print(board[k])
                
                       
                
            else:              #check whether game is tie                      
                print("Tie")
            
                break  #break the loop
                
    #generate random intial state board      
    def intial_board(self, player):
        
        board =  [
 	[ '_', '_', '_' ],
 	[ '_', '_', '_' ],
 	[ '_', '_', '_' ]]

       
        row = random.randint(0, 2)    #random index of row of board
        col = random.randint(0,2)     #random index of column of board
        board[row][col] = player
        
        return board
        
        
        
    
    #play the game on selected options
    def choose_options(self, options):
        b = self.intial_board(self.player)       #generate random intial board
        
        if options == 'h':          # options of human vs computer
            self.human_V_computer(b)
        
        elif options == 'c':     #options of computer vs computer
            self.computer_V_computer(b)
            
        else:                    #print the instruction of game
            print(options)
                
                
            

file_name = sys.argv[1]
options = open(file_name, 'r').read()

t = Tic_Tac_Toe()
t.choose_options(options)










