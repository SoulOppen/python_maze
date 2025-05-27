from graphics import Window,Point,Line
def main():
    win = Window(800, 600)
    lines_with_colors = [
        (Line(Point(100, 100), Point(400, 100)), "red"),
        (Line(Point(100, 150), Point(400, 200)), "blue"),
        (Line(Point(100, 200), Point(400, 300)), "green"),
        (Line(Point(100, 250), Point(400, 400)), "purple"),
        (Line(Point(100, 300), Point(400, 500)), "orange"),
    ]

    for line, color in lines_with_colors:
        win.draw_line(line, color)
    win.wait_for_close()
main()
