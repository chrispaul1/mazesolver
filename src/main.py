from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():   
    num_rows = 15
    num_cols = 15
    margin = 50
    screen_x = 800
    screen_y = 800
    win = Window(screen_x,screen_y)
    cell_size = min(((screen_x-2*margin)//num_cols),((screen_y-2*margin)//num_rows))
    maze = Maze(margin,margin,num_rows,num_cols,cell_size,cell_size,win)
    win.wait_for_close()

    
main()