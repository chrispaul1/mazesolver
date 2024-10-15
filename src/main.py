from window import Window, Point, Line, Cell

def main():
    win = Window(800, 800)
    point1 = Point(10,20)
    point2 = Point(100,300)
    test_line = Line(point1,point2)

    #win.draw_line(test_line,"black")
    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.draw(10,10,100,100)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(110,10,200,100)

    cell3 = Cell(win)
    cell3.has_top_wall= False
    cell3.draw(210,10,300,100)

    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.draw(310,10,400,100)

    win.wait_for_close()

    
main()