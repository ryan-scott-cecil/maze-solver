from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    l = Line(Point(69, 69), Point(420, 420))
    win.draw_line(l, "black")
    l2 = Line(Point(69, 420), Point(420, 69))
    win.draw_line(l2, "red")
    win.wait_for_close()

main()
