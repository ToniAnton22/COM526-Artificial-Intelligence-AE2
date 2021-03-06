import unittest
import pytest
from Sudoku import *

class MyTestCase(unittest.TestCase):

    def test_create(self):
        # Test if the table is created
        s = SudokuApp()
        brd = s.create()
        self.assertIsNotNone(brd,msg = "Table is not created or is not created properly")

    def test_solve(self):
        # Tests if the table created is the same with the one solved.
        s = SudokuApp()
        brd1 = s.create()
        brd2 = s.solve()
        self.assertListEqual(brd2,brd1, msg="The A.I is successful")

    def test_pattern(self):
        # Tests pattern
        s = SudokuApp()
        self.assertNotEqual(s.pattern(0,0),(2,1), msg ="Doesn't work as intended")

    def test_shuffle(self):
        s = SudokuApp()
        # NOTE, there is a small change the shuffle might make them equal
        ed = s.shuffle((4,5,2,13,45))
        ed1= s.shuffle((4,5,2,13,45))
        self.assertNotEqual(ed,ed1,msg = "Shuffle went wrong")

    def test_everything(self):
        # Puts everything into play, tests every function working together
        s = SudokuApp()
        brd= s.start()
        self.assertTrue(brd is not None)

if __name__ == '__main__':

    unittest.main()
