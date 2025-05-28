import unittest
from maze import Maze 

class Tests(unittest.TestCase):

    def test_maze_create_cells_dimensions(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_1x1(self):
        m = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(len(m._Maze__cells), 1)
        self.assertEqual(len(m._Maze__cells[0]), 1)

    def test_maze_3x7(self):
        m = Maze(0, 0, 3, 7, 10, 10)
        self.assertEqual(len(m._Maze__cells), 7)
        self.assertEqual(len(m._Maze__cells[0]), 3)

    def test_maze_20x5(self):
        m = Maze(0, 0, 20, 5, 10, 10)
        self.assertEqual(len(m._Maze__cells), 5)
        self.assertEqual(len(m._Maze__cells[0]), 20)

    def test_animate_no_window(self):
        try:
            m1 = Maze(0, 0, 2, 2, 10, 10, win=None)
            self.assertTrue(True) 
        except Exception as e:
            self.fail(f"_animate() lanzó una excepción inesperada: {e}")
    def test_break_entrance_and_exit(self):
        # Crear un laberinto de 5x5
        m = Maze(0, 0, 5, 5, 10, 10)

        # Llamar al método privado
        m._Maze__break_entrance_and_exit()

        # Verificar que la entrada no tiene pared superior
        self.assertFalse(m._Maze__cells[0][0].has_top_wall, "La entrada aún tiene pared superior")

        # Verificar que la salida no tiene pared inferior
        self.assertFalse(
            m._Maze__cells[4][4].has_bottom_wall,
            "La salida aún tiene pared inferior"
        )
    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, seed=0)
        
        # Marcar algunas celdas como visitadas a mano para el test
        maze._Maze__cells[0][0].visited = True
        maze._Maze__cells[2][3].visited = True
        
        # Llamar al método que queremos testear
        maze._Maze__reset_cells_visited()
        
        # Comprobar que todas las celdas están en False
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertFalse(maze._Maze__cells[i][j].visited)
if __name__ == "__main__":
    unittest.main()
