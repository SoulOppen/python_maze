from line import Line
from point import Point
class Cell():
    def __init__(self,win=None):
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
        if self.__win is None:
            return
        wall_color = "black"
        erase_color = "#d9d9d9" 
        # Left Wall
        line = Line(Point(x1, y1), Point(x1, y2))            
        color_left= wall_color if self.has_left_wall else erase_color
        self.__win.draw_line(line,color_left)

        # Top Wall
        line = Line(Point(x1, y1), Point(x2, y1))
        color_top= wall_color if self.has_top_wall else erase_color
        self.__win.draw_line(line,color_top)

        # Right Wall
        line = Line(Point(x2, y1), Point(x2, y2))
        color_right= wall_color if self.has_right_wall else erase_color
        self.__win.draw_line(line,color_right)

        # Bottom Wall
        line = Line(Point(x1, y2), Point(x2, y2))
        color_bottom= wall_color if self.has_bottom_wall else erase_color
        self.__win.draw_line(line,color_bottom)
    def draw_move(self, to_cell, undo=False):
        # Calculamos el centro de la celda actual
        x_mid = (self.__x1 + self.__x2) // 2
        y_mid = (self.__y1 + self.__y2) // 2

        # Calculamos el centro de la celda destino
        to_x_mid = (to_cell.__x1 + to_cell.__x2) // 2
        to_y_mid = (to_cell.__y1 + to_cell.__y2) // 2

        # Línea entre los dos centros
        line = Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid))
        if self.__win is None:
            return
        if undo:
            self.__win.draw_line(line,"red")
        else:
            self.__win.draw_line(line,"grey")