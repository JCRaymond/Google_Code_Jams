from Utils.CJFileIO import *
from Methods import *

f = CJFileIO("C", CJSize.large)

N = f.readi()

for n in range(N):
    P = f.readi()
    Q = f.readi()

    cells = [f.readi() for q in range(Q)]

    cost = alt_get_lowest_cost(P, cells)

    f.write_next_case(cost)

f.close()