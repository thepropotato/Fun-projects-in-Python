grid = [[' ' for j in range (0,3)] for i in range (0,3)]

passcases = ["XXX", "OOO"]

def tictactoe () :
    
    print("PLAYER 1 : O ")
    print("PLAYER 2 : X ")
    round = 0
    
    while round<9 :
        if round%2 == 0 :
            sym = 'O'
        elif round%2 == 1 :
            sym = 'X'

        row = int(input('Enter the row    : '))
        col = int(input('Enter the column : '))
        grid[row][col] = sym
        
        passcases = ["OOO", "XXX"]
        rowsum = [''.join(row) for row in grid]

        newg = list(zip(*grid))
        colsum = [''.join(row) for row in newg]
        
        for row in grid :
            print(row)
            
        i = 0
        gameover = 0
        
        while i<3 :
            if rowsum[i] in passcases or colsum[i] in passcases or grid[1][1] == grid[0][0] == grid[2][2] != " ":
                print("PLAYER 1 (O) WON !") if round%2 == 0 else None
                print("PLAYER 2 (X) WON !") if round%2 == 1 else None
                round = round + (10-round)
                i = 3
                gameover = 1
            i = i+1
        round = round+1
        
        if gameover != 1 and round >= 9:
            print(" TIE ") 
        
    return grid


tictactoe()