import random

def show_board(board):
    "shows current board"
    print()
    print(board[6],"|", board [7] , "|" , board[8])
    print("----------")
    print(board[3],"|", board [4] , "|" , board[5])
    print("----------")
    print(board[0],"|", board [1] , "|" , board[2])   
    
    
def player_marker ():
    "assigns marker to players"
    player1 = input("Player 1 please pick a marker 'X' or 'O': ")
    player2 = "X"
    while player1 != "X" and player1 != "O":
        print("please select 'X' or 'O' as a marker")
        player1 = input("Please pick a marker 'X' or 'O'")        
    if player1 == "X":
        player2 = "O"
    print("player 1: ",player1)
    print("player 2: ",player2)
    return player1, player2



def Assign_marker_to_board (board,marker,position):
    "Assign marker to position in board"
    board[position-1] = marker
    return board


def Marker_won (board,marker):
    "Checks if marker won"
    Win = False
    #Horizontal Lines
    if board[0] == marker and board[1] == marker and board[2] == marker:        
        Win = True
    elif board[3] == marker and board[4] == marker and board[5] == marker:        
        Win = True
    elif board[6] == marker and board[7] == marker and board[8] == marker:        
        Win = True
    #Vertical Lines
    elif board[6] == marker and board[3] == marker and board[0] == marker:        
        Win = True
    elif board[7] == marker and board[4] == marker and board[1] == marker:        
        Win = True
    elif board[8] == marker and board[5] == marker and board[2] == marker:        
        Win = True
    #diagonals
    elif board[6] == marker and board[4] == marker and board[2] == marker:        
        Win = True
    elif board[0] == marker and board[4] == marker and board[8] == marker:        
        Win = True
    return Win


def Who_First():
    "Chose wich player goes first"
    n = random.randint(1,2)
    print("player",n,"goes first")
    return n
    
    
def Space_available (board, position):
    "Returns True if space available"
    return board[position-1] == " "

def Board_full (board):
    "Cheks if board is full"
    full = False
    if " " not in board:
        full = True        
    return full
    
def Player_move (board):
    "Ask for position and check if space is avalable"   
    position = int(input("chose position (1-9): "))    
    while position not in range(1,10):
            print("Wrong Value")
            position = int(input("chose position (1-9): "))
    
    while Space_available (board, position) == False:
        print("Position already used")
        position = int(input("chose position (1-9): "))
        while position not in range(1,10):
            print("Wrong Value")
            position = int(input("chose position (1-9): "))
    return position
            

def Replay ():
    replay = False
    print("Do you want to play again?")
    ask = input("Type yes or no: ")
    answer = ask.lower()    
    while answer != "yes" and answer != "no":
        print("Please enter a valid answer")
        ask = input("Type 'yes' or 'no': ")
        answer = ask.lower()
    if answer == "yes":
        replay = True
    return replay


# MAIN PROGRAM


while True:
    game_going = True
    print('\n'*100)
    print("Welcome to Tic Tac Toe!")
    #Set up the game
    board = [" "," "," "," "," "," "," "," "," "]
    marker1,marker2 = player_marker()
    turn = Who_First()
    show_board(board)
    
    while game_going == True:
        if turn ==1:
            position = Player_move (board)
            Assign_marker_to_board (board,marker1,position)
            show_board(board)
            
            if Marker_won (board,marker1):
                print("player 1 won")
                game_going = False
            elif Board_full (board):
                print("draw")
                game_going = False
            else:
                turn = 2
        if turn == 2:
            position = Player_move (board)
            Assign_marker_to_board (board,marker2,position)
            show_board(board)
            
            if Marker_won (board,marker2):
                print("player 2 won")
                game_going = False
            elif Board_full (board):
                print("draw")
                game_going = False
            else:
                turn = 1
    
                
    if Replay() == False:
        print("Thank you for Playing!")
        break

input()
            
    
    
            
            
     
    
    
                
        
        
        
        
        
        
    
    
    
    
    
    
    
    
        
    
        

    








    
    
       
    
    
    




















        
    
    
    
    






    
        
    
    

    

    
    









    
    