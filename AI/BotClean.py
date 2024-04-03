#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dirty_cells = [(r, c) for r in range(5) for c in range(5) 
if board[r][c] == 'd']
    
    if (posr, posc) in dirty_cells:
        print("Clean")
        dirty_cells.remove((posr, posc))
        
    elif dirty_cells:
        min_destance_cell = min(dirty_cells, key=lambda cell: (cell[0], cell[1]))
        target_r, target_c = min_distance_cell
        if target_r < posr:
            print("UP")
        elif target_r>posr:
            print("DOWN")
        elif target_c<posc:
            print("LEFT")
        elif trage_c>posc:
            print("RIGHT")
            
        

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)