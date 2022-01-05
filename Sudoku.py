from random import sample

class SudokuApp:

    def __init__(self):
        # Initial values for our sudoku game, they will not be changable
        self.base = 3
        self.side = self.base*self.base
        self.brd = []

    def start(self):

        self.brd = self.create()

        self.brd = self.solve()

        return self.brd


    def pattern(self,r,c): return (self.base *(r % self.base) + r//self.base + c)% self.side

    def shuffle(self,s): return sample(s, len(s))


    def create(self):
        # Creates rows and col, with a 3x3 base useing rBase
        rBase = range(self.base)
        rows = [g * self.base + r for g in self.shuffle(rBase) for r in self.shuffle(rBase)]
        col = [g * self.base + c for g in self.shuffle(rBase) for c in self.shuffle(rBase)]
        print(col)
        print(rows)
        # Reshuffles and adds to the rows and cols "+1", to get rid of the initial "0" from using range above
        #And to add up to 9
        nums = self.shuffle(range(1, self.base*self.base + 1))

        # Creates 9 total 3x3 tables, and adds the sudoku rules pattern
        self.brd =[[nums[self.pattern(r,c)] for c in col]for r in rows]

        self.brd = self.emptysquares()

        return self.brd

    def emptysquares(self):

        squares = self.side * self.side
        empties = squares * 3//4

        # Interates to turn to 0 three quarters of the board

        for p in sample(range(squares),empties):
            self.brd[p//self.side][p%self.side]= 0

        return self.brd

    def print_brd(self):
        # Every third row print line
        for c in range(len(self.brd)):
            if c % 3 == 0 and c != 0:
                print("- - - - - - - - - - - - - ")

            # Every third element print horizontal line
            for r in range(len(self.brd[0])):
                if r % 3 == 0 and r != 0:
                    print("| ", end="")

                # Last possition check
                if r == 8:
                    print(self.brd[c][r])
                else:
                    print(str(self.brd[c][r]) + " ", end="")



    def find_empty(self):
        # Finds the next row, col on the puzzle that is empty
        # Loop through the board, if we find the position that is empty (zero is that case)
        # Return the position

        for c, row in enumerate(self.brd):
            for r, val in enumerate(row):
                if val == 0:
                    return (c,r)




    def is_valid(self, num, pos):
        # Check row
        for c in range(len(self.brd[0])):
            if self.brd[pos[0]][c] == num and pos[1] != c:
                return False

        # Check column
        for c in range(len(self.brd)):
            if self.brd[c][pos[1]] == num and pos[0] != c:
                return False

        # Check box 3x3
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for c in range(box_y*3, box_y*3 + 3):
            for r in range(box_x * 3, box_x*3 + 3):
                if self.brd[c][r] == num and (c, r) != pos:
                    return False

        return True


    def solve(self):
        find = self.find_empty()
        if not find:
            return self.brd
        else:
            row, col = find

        for c in range(1, 10):
            if self.is_valid(c, (row, col)):
                self.brd[row][col] = c

                if self.solve():
                    return self.brd

                self.brd[row][col] = 0

        return False


if __name__== '__main__':
    s = SudokuApp()
    s.start()
    s.print_brd()
