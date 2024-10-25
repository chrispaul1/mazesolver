from cell import Cell
import time
import random

class Maze:

    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        if seed is None:
            self.seed = random.seed(seed)
        else:
            self.seed = seed
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self.cells = [[Cell(self.win) for j in range(self.num_cols)] for i in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        if self.win is None:
            return
        top_left_x = self.x1 + self.cell_size_x*j
        top_left_y = self.y1 + self.cell_size_y*i
        bottom_right_x = top_left_x + self.cell_size_x
        bottom_right_y = top_left_y + self.cell_size_y
        # if i==0 and j == 0:
        #     self.cells[i][j].draw(top_left_x,top_left_y,bottom_right_x,bottom_right_y,"red")
        # elif i == 1 and j == 0:
        #     self.cells[i][j].draw(top_left_x,top_left_y,bottom_right_x,bottom_right_y,"blue")
        # elif i == 0 and j == 1:
        #     self.cells[i][j].draw(top_left_x,top_left_y,bottom_right_x,bottom_right_y,"green")
        # else:
        self.cells[i][j].draw(top_left_x,top_left_y,bottom_right_x,bottom_right_y)

    def _animate(self):
        if self.win is None:
            return
        try:
            self.win.redraw()
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self.cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self._draw_cell(self.num_rows-1,self.num_cols-1)
    
    def _break_walls_r(self,i,j):
        # print(f"cell i and j  {i} {j}")
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if i-1 >= 0 and not self.cells[i-1][j].visited:
                to_visit.append((i-1,j))
            
            if i+1 < self.num_rows and not self.cells[i+1][j].visited:
                to_visit.append((i+1,j))
            
            if j-1 >= 0 and not self.cells[i][j-1].visited:
                to_visit.append((i,j-1))

            if j+1 < self.num_cols and not self.cells[i][j+1].visited:
                to_visit.append((i,j+1))
            
            if len(to_visit) > 0:
                choice = random.randrange(len(to_visit))
                next_i,next_j = to_visit[choice]
                # print(f"next i and j {next_i} {next_j}")

                if next_i < i:
                    # print("current top wall removed")
                    self.cells[i][j].has_top_wall = False
                    self.cells[next_i][next_j].has_bottom_wall = False
                
                if next_i > i:
                    # print("current bottom wall")
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[next_i][next_j].has_top_wall = False
                
                if next_j < j:
                    # print("current left wall")
                    self.cells[i][j].has_left_wall = False
                    self.cells[next_i][next_j].has_right_wall = False

                if next_j > j:
                    # print("current right wall")
                    self.cells[i][j].has_right_wall = False
                    self.cells[next_i][next_j].has_left_wall = False
                self._draw_cell(i,j)
                self._draw_cell(next_i,next_j)
                self._break_walls_r(next_i,next_j)
            else:
                self._draw_cell(i,j)
                return
            
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False

    def solve(self):
         return self._solve_r(self,0,0)

    def _solve_r(self,i,j):
        self._animate()
        self.cells[i][j].visited = True
        if i == self.num_rows-1 and j == self.num_cols-1:
            return True
        
        if i-1 >=0 and not self.cells[i][j].has_top_wall and not self.cells[i-1][j].visited:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self.cells[i][j].draw_move(self.cells[i-1][j],True)
        
        if j+1 < self.num_cols and not self.cells[i][j].has_right_wall and not self.cells[i][j+1].visited:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j+1],True)
        
        if i+1 < self.num_rows and not self.cells[i][j].has_bottom_wall and not self.cells[i+1][j].visited:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self.cells[i][j].draw_move(self.cells[i+1][j],True)

        if j-1 >= 0 and not self.cells[i][j].has_left_wall and not self.cells[i][j-1].visited:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self.cells[i][j].draw_move(self.cells[i][j-1],True)

        return False
