from graphics import Window,Cell
def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.draw(100, 50, 150, 100)

    cell1.draw_move(cell2)  # Movimiento normal
    cell2.draw_move(cell1, undo=True)  # Retroceso en rojo
    win.wait_for_close()
main()
