from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.root_widget.title("Maze Solver")
        self.canvas_widget = Canvas(self.root_widget,bg="white",width=self.width,height=self.height)
        self.canvas_widget.pack(fill=BOTH,expand=1)
        self.window_running = False
    
    
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def draw_line(self,line,fill_color="black"):
        line.draw(self.canvas_widget,fill_color)
    
    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()
    
    def close(self):
        self.window_running = False

class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self,canvas,fill_color="black"):
        canvas.create_line( self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill=fill_color,width=2)