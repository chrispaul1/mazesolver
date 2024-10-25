import unittest
from maze import Maze

def all_cells_unvisited(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j].visited == True:
                    return False
        return True

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(20,20,13,13,12,12)
        self.assertEqual(
            len(m1.cells),
            num_rows,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_cols,
        )
        self.assertEqual(m2.x1,20)
        self.assertEqual(m2.y1,20)
        self.assertEqual(len(m2.cells),13)
    
    def test_maze_walls(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(m1.cells[0][0].has_top_wall,False)
        self.assertEqual(m1.cells[num_rows-1][num_cols-1].has_bottom_wall,False)
        m1._reset_cells_visited()
        self.assertTrue(all_cells_unvisited(m1.cells))

if __name__ == "__main__":
    unittest.main()