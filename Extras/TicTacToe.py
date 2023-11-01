import os

class Board():
    def __init__(self):
        self.cells = [" "]*9

    def display(self):
        print()
        for i in range(0, 9, 3):
            print(" | ".join(self.cells[i:i+3]))
            if i < 6:
                print("----------")

    def update(self, cell, player):
        if cell in range(0,9) and self.cells[cell].startswith(" "):
            self.cells[cell] = str(player)
            return True
        else:
            print("Invalid Move! Try again.")
            return False

    def reset(self):
        self.cells = [" "]*9

    def is_winner(self, player):
        for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
            result = True
            
            for cell in combo:
                if self.cells[cell] != player:
                    result = False
            if result:
                return True
        return False

    def is_draw(self):
        return " " not in self.cells


board = Board()
    
def refresh():
    os.system("clear")
    board.display()

def rematch():
    rematch = input("Do you want to play again? (Y/N) --> ")
    if rematch.upper() == "Y":
        board.reset()
        return True
    elif rematch.upper() == "N":
        return False
    

while True:
    refresh()
    while True:
        x_ch = int(input("\nX: Select a box from 1-9 --> "))
        valid=board.update(x_ch-1, 'X')
        if valid == True:
            break
        
    refresh()
    
    if board.is_winner('X'):
        print("\n\nX is the winner !!")
        if rematch():
            continue
        else:
            break

    if board.is_draw():
        print("\n\nTie Game !!")
        if rematch():
            continue
        else:
            break
        
    
    while True:
        y_ch = int(input("\nO: Select a box from 1-9 --> "))
        valid=board.update(y_ch-1, 'O')
        if valid == True:
            break

    if board.is_winner('Y'):
        print("\n\nY is the winner !!")
        if rematch():
            continue
        else:
            break

    if board.is_draw():
        print("\n\nTie Game !!")
        if rematch():
            continue
        else:
            break