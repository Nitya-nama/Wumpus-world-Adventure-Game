import random

class WumpusWorld():
    def __init__(self,size=4):
        self.size=size #4X4 grid
        self.player_pos=(0,0) #player start position 
        self.wumpus_pos=self.random_empty_cell() #select the wumpus position randomly
        self.gold_pos=self.random_empty_cell() #select the gold position randomly
        self.pits_pos={self.random_empty_cell() for i in range(2)} #place 2 pits anywhere randomly
        self.has_gold=False #player donot have gold at start
        self.arrow =1 #player has 1 arrow only
        self.game_over=False
        
    def random_empty_cell(self):
        """we need to generate all the postions of 4X4 grid except (0,0) as its the start position"""
        while True:
            pos=(random.randint(0,self.size-1),random.randint(0,self.size-1))
            if pos!=(0,0):
                return pos
            
    def get_perceptions(self):
        """we return the sensory perceptions of the player"""
        r,c=self.player_pos #row,column pair
        adjacent={(r+1,c),(r-1,c),(r,c+1),(r,c-1)}
        messages=[]
        if self.wumpus_pos in adjacent:
            messages.append("STENCH***")
        if self.pits_pos in adjacent:
            messages.append("BREEZE^^^") 
        if self.gold_pos in adjacent:
            messages.append("GLITTER!!!")    
        
        return messages
    
    def move(self,direction):
        """moves player in given direction"""
        if self.game_over:
            print("GAME OVER!!!")
            return
        r,c=self.player_pos #row,column pair
        if direction=="up" and r<self.size-1:
            r+=1
        elif direction=="down" and r>0:
            r-=1
        elif direction=="left" and c>0:
            c-=1
        elif direction=="right" and c<self.size-1:
            c+=1     
        else:
            print("invalid move")           
            return
        self.player_pos=r,c
        self.check_status()
        
    def check_status(self):
        """We check the status if player wins,looses or they can continue"""            
        if self.player_pos==self.gold_pos:
            self.has_gold=True
            print("YOU FOUN GOLD SO EXIT TO (0,0)")
        if self.player_pos==self.pits_pos:
            print("YOU FELL IN PIT SO GAME OVER***")
            self.game_over=True  
        if self.player_pos==self.wumpus_pos:
            print("YOU'RE CAUGHT BY WUMPUS SO GAME OVER***")
            self.game_over=True      
        if self.player_pos==(0,0) and self.has_gold==True :
            print("YOU HAVE SUCCESFULLY ESCAPED THE CAVE WITH GOLD!!!\n***YOU WIN***")
            self.game_over=True    
            
    def shoot_arrow(self,direction):
        if self.arrow==0:
            print("No arrows left to shoot")
            return   
        self.arrow-=1
        r,c=self.player_pos
        if direction=="up":
            while r<self.size-1:
                r+=1
                if(r,c)==self.wumpus_pos:
                    print("SCREAM IS HEARD!!!!!!!THE WUMPUS IS KILLED")
                    self.wumpus_pos=None
                    return
        elif direction=="down":
            while r>0:
                r-=1
                if(r,c)==self.wumpus_pos:
                    print("SCREAM IS HEARD!!!!!!!THE WUMPUS IS KILLED")
                    self.wumpus_pos=None
                    return
        elif direction=="right":
            while c<self.size-1:
                c+=1
                if(r,c)==self.wumpus_pos:
                    print("SCREAM IS HEARD!!!!!!!THE WUMPUS IS KILLED")
                    self.wumpus_pos=None
                    return
        elif direction=="left":
            while c>0:
                c-+1
                if(r,c)==self.wumpus_pos:
                    print("SCREAM IS HEARD!!!!!!!THE WUMPUS IS KILLED")
                    self.wumpus_pos=None
                    return
        print("YOU MISSED IT")
        
    def play(self):
        """main game"""
        print("Welcome to Wumpus World!")
        print("Move: 'move up/down/left/right' | Shoot: 'shoot up/down/left/right'")
        print("Find the gold and return to (0,0) to win!")

        while not self.game_over:
            print("\nPerceptions:", ", ".join(self.get_perceptions()))
            command = input("Enter move/shoot command: ").strip().lower()

            if command.startswith("move"):
                self.move(command.split()[1])
            elif command.startswith("shoot"):
                self.shoot_arrow(command.split()[1])
            else:
                print("Invalid command!")

        print("Game Over!")


# Run the game
game = WumpusWorld()
game.play()
                    
                  
                    
