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

if __name__ == "__main__":
    unittest.main()
