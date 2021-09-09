

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    

class Board:
    
    def __init__(self):
        self.grid = [0,0,0,0,0,0,0,0,0]
        
        
    def print_board(self):
        print(" " + self.int_to_printable(self.grid[0]) + " | " + self.int_to_printable(self.grid[1]) + " | " + self.int_to_printable(self.grid[2]) + 
                "\n " + self.int_to_printable(self.grid[3]) + " | " + self.int_to_printable(self.grid[4]) + " | " + self.int_to_printable(self.grid[5]) +
                "\n " + self.int_to_printable(self.grid[6]) + " | " + self.int_to_printable(self.grid[7]) + " | " + self.int_to_printable(self.grid[8]))
    
    def int_to_printable(self, int_sign: int)-> str: # modifies the input int to a output string
        if int_sign == 0:
            return " "
        elif int_sign == 1:
            return "X"
        else:
            return "O"
        
    def move(self, position, player) -> bool:
        if self.is_valid(position): #check if move is valid
            self.grid[position] = player.symbol
            return True
        return False
        
        
    def check_win(self, player)-> bool:
        p = player.symbol
        
        # check win condition on rows
        if self.grid[0] == p and self.grid[1] == p and self.grid[2] == p:
             return True
        elif self.grid[3] == p and self.grid[4] == p and self.grid[5] == p:
            return True
        elif self.grid[6] == p and self.grid[7] == p and self.grid[8] == p:
            return True           
        # check win condition on columns
        if self.grid[0] == p and self.grid[3] == p and self.grid[6] == p:
             return True
        elif self.grid[1] == p and self.grid[4] == p and self.grid[7] == p:
            return True
        elif self.grid[2] == p and self.grid[5] == p and self.grid[8] == p:
            return True           
        # check win condition on diagonals
        if self.grid[0] == p and self.grid[4] == p and self.grid[8] == p:
             return True
        elif self.grid[3] == p and self.grid[4] == p and self.grid[6] == p:
            return True

        return False
        
        
    def is_valid(self, position: int)->bool:    # checks if the move was valid or not
        if self.grid[position] == 0:
            return True
        return False
    
    
    def full(self) -> bool: # checks if the board is full
        for i in self.grid:
            if i == 0:
                return False
        return True
 

def main():
    board = Board()
    player1 = Player(1)
    player2 = Player(2)
    
    active_player = player1
    
    # Gamloop
    while not board.full():
        board.print_board()
        try:
            pos = int(input("Please insert a number between 1-9! : "))
        except ValueError:
            print("Invalid input, must be a number between 1-9")
            continue
        pos = pos-1 # subtract 1 to get the grid position for the array
        
        if not board.move(pos, active_player):
            print("Invalid move, please try again!")
            continue
        
        if board.check_win(active_player):
            board.print_board()
            print("Congrats, you won")
            break
        
        if active_player == player1:
            active_player = player2
        else:
            active_player = player1
            
if __name__ == "__main__":
    main()


