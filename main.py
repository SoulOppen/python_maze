from graphics import Window,Cell
def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell2.draw(50, 100, 100, 150)

    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_top_wall = False
    cell3.draw(100, 100, 150, 150)
    win.wait_for_close()
main()
