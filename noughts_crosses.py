# noughts and crosses


board = [[" "," "," "], #noughts and crosses board
         [" "," "," "],
         [" "," "," "]]

player = "x" #tracks player
end = False #if game is ended

def display(): #displays board
    global board
    for row in board:
        print(row)

def tplay(player): #player takes turn
    global board
    valid = False
    while valid == False:
        row = int(input("choose which row to play in (0-2) "))
        column = int(input("choose which column to play in (0-2) "))
        if board[row][column] != "x" and board[row][column] != "o":
            board[row][column] = player
            valid = True
        else:
            print("space taken")

def pturn(): #one player turn
    global player
    display()
    tplay(player)
    if player == "x":
        player = "o"
    else:
        player = "x"

def wincheck(): #checks for 3 in a row
    global board
    if board[0][0] == board[1][1] == board[2][2] != ' ': #checks diagonals
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    for row in board: #checks rows
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    for i in range(3): #checks columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    return False
        
    
board = [['x','o','x'],
         ['x','o','o'],
         ['x','o','o']]
print(wincheck())
while end == False:
    pturn()
    win = wincheck()
    if win == True:
        print(player + " wins")
        end = True
        
    
    
    
