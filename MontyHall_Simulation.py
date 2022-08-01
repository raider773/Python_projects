# Simulation Monty Hall with n samples

#functions
    
import random


def doors ():
    doors = [0,0,0]
    car = random.randint(0,2)
    doors[car] = 1
    return doors
    
def player (doors):
    choice = random.randint(0,2)
    doors[choice] = 2
    return doors

def host (doors):
    elimination = random.randint(0,2)
    if 1 not in doors:
        while doors[elimination] == 2:
            elimination = random.randint(0,2)
        del doors[elimination]
    elif 1 in doors and 2 in doors:
        del doors[doors.index(0)]
        
    return doors

def stay (doors):
    condition = None
    if 1 in doors:
        condition = False
    elif 1 not in doors:
        condition = True       
    return condition


def change (doors):
    condition = None
    if 1 in doors:
        condition = True
    elif 1 not in doors:
        condition = False      
    return condition
    

#program
    
if __name__ == "__main__":   
    
    n = int(input('Number of Even Samples: '))
    while n % 2 != 0:
        print('I said even dude')
        n = int(input('Number of Even Samples: '))
    cont_stay = n/2
    cont_change = n/2
    
    wins_stay = 0
    wins_change = 0
    
    lost_stay = 0
    lost_change = 0
   
    for i in range(0,n):
        #Half samples stay in door, other half change door  
        
        while cont_stay != 0:
            game = host(player(doors()))
            result = stay(game) 
            if result == True:
                wins_stay += 1
            elif result == False:
                lost_stay += 1
            cont_stay = cont_stay - 1
            
            
        while cont_change != 0:
            game = host(player(doors()))
            result = change(game) 
            if result == True:
                wins_change += 1
            elif result == False:
                lost_change += 1
            cont_change -= 1
     
    #if simulation is ok then Change wins doubles Stay wins, simulating 2/3 chance of wining when you change door
    #and 1/3 when you stay in the door you initially selected       
    print(f"Stay wins {wins_stay} , Stay losses {lost_stay}")    
    print(f"Change wins {wins_change} , Change losses {lost_change}")
    
   
     
    
    
         