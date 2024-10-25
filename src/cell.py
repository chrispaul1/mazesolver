from window import Point, Line

class Cell:
    def __init__(self,win=None):
        self.win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.visited = False
    
    def draw(self,x1,y1,x2,y2,fill_color="black"):
        if self.win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            self.win.draw_line(Line(Point(x1,y1),Point(x1,y2)),fill_color)
        else:
            self.win.draw_line(Line(Point(x1,y1),Point(x1,y2)),"white")

        if self.has_right_wall:
            self.win.draw_line(Line(Point(x2,y1),Point(x2,y2)),fill_color)
        else:
            self.win.draw_line(Line(Point(x2,y1),Point(x2,y2)),"white")

        if self.has_top_wall:
            self.win.draw_line(Line(Point(x1,y1),Point(x2,y1)),fill_color)
        else:
            self.win.draw_line(Line(Point(x1,y1),Point(x2,y1)),"white")

        if self.has_bottom_wall:
            p1 = Point(x1,y2)
            p2 = Point(x2,y2)
            self.win.draw_line(Line(Point(x1,y2),Point(x2,y2)),fill_color)
        else:
            self.win.draw_line(Line(Point(x1,y2),Point(x2,y2)),"white")
    

    def draw_move(self,to_cell,undo=False):
        half_length_xp1 = (self.x2-self.x1)//2
        half_length_yp1 = (self.y2-self.y1)//2
        half_length_xp2 = (to_cell.x2-to_cell.x1)//2
        half_length_yp2 = (to_cell.y2-to_cell.y1)//2
        p1 = Point(self.x1+half_length_xp1,self.y1+half_length_yp1)
        p2 = Point(to_cell.x1+half_length_xp2,to_cell.y1+half_length_yp2)
        self.win.draw_line(Line(p1,p2),"red" if not undo else "gray")
