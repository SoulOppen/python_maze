from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Window")

        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Line:
    def __init__(self,point1,point2):
        self.point1=point1
        self.point2=point2
    def draw(self,canvas,fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
class Cell():
    def __init__(self,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1

        self.__win = win
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        # Left Wall
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line,"black")

        # Top Wall
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line,"black")

        # Right Wall
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line,"black")

        # Bottom Wall
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line,"black")
    def draw_move(self, to_cell, undo=False):
        # Calculamos el centro de la celda actual
        x_mid = (self.__x1 + self.__x2) // 2
        y_mid = (self.__y1 + self.__y2) // 2

        # Calculamos el centro de la celda destino
        to_x_mid = (to_cell.__x1 + to_cell.__x2) // 2
        to_y_mid = (to_cell.__y1 + to_cell.__y2) // 2

        # Línea entre los dos centros
        line = Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid))
        if undo:
            self.__win.draw_line(line,"red")
        else:
            self.__win.draw_line(line,"grey")