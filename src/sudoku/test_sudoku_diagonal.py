#!/usr/bin/python
# -*-coding:utf-8 -*-
import time
from sudoku_solve import sudoku



sudoku1 = sudoku(is_diagonal=True)

def solve(grid):
    sudoku1.display(sudoku1.grid_values(grid))
    print('-'*50)
    tic = time.clock()
    sudoku1.display(sudoku1.search(sudoku1.parse_grid(grid)))
    toc = time.clock()
    print('='*50)
    print("%.4f"%(toc - tic))
    print('='*50)


grid1 = '\
000208915\
700005020\
000000000\
070800000\
000516000\
000007060\
000000000\
080700006\
453109000\
'
solve(grid1)

#with open('./sudokus/sudokus_diagonal.csv', 'r') as f:
#    for line in f:
#        #print(line.rstrip('\n'))
#        solve(line.rstrip('\n'))
