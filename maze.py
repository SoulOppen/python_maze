from cell import Cell
import time
import random
class Maze:
    def __init__(self,   
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None):
        if seed is not None:
            random.seed(a=None, version=2)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        
        self.__create_cells()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.__break_entrance_and_exit()
    def __create_cells(self):
        for i in range(self.num_cols):
            column = []  
            for j in range(self.num_rows):

                cell = Cell(self.win)
                column.append(cell)
            self.__cells.append(column) 
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)
    def __draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    def __break_entrance_and_exit(self):
        # Romper entrada (arriba izquierda)
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # Romper salida (abajo derecha)
        last_col = self.num_cols - 1
        last_row = self.num_rows - 1
        self.__cells[last_col][last_row].has_bottom_wall = False
        self.__draw_cell(last_col, last_row)
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited=True
        while True:
            # Direcciones posibles: vecinos no visitados (dentro de los límites)
            directions = []

            # Izquierda
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append(('left', i - 1, j))
            # Derecha
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                directions.append(('right', i + 1, j))
            # Arriba
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append(('up', i, j - 1))
            # Abajo
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                directions.append(('down', i, j + 1))

            if not directions:
                # No hay vecinos no visitados, dibujamos y retornamos
                self.__draw_cell(i, j)
                return

            # Elegir dirección aleatoria
            direction, ni, nj = random.choice(directions)

            # Romper muros entre cell y vecino según dirección
            current_cell = self.__cells[i][j]
            next_cell = self.__cells[ni][nj]

            if direction == 'left':
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif direction == 'right':
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif direction == 'up':
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif direction == 'down':
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False

            # Recursión al vecino
            self.__break_walls_r(ni, nj)
    def __reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False