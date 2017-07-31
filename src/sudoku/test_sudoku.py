#!/usr/bin/python
# -*-coding:utf-8 -*-
import time
from sudoku_solve import sudoku

grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'


sudoku1 = sudoku()

def solve(grid):
    sudoku1.display(sudoku1.grid_values(grid))
    print('-'*50)
    tic = time.clock()
    sudoku1.display(sudoku1.search(sudoku1.parse_grid(grid)))
    toc = time.clock()
    print('='*50)
    print("%.4f"%(toc - tic))
    print('='*50)

grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

solve(grid1)
solve(grid2)
