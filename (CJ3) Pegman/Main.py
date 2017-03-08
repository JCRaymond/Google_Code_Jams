from Utils.CJFileIO import *
from Methods import *

fio = CJFileIO()

T = fio.readi()

for t in range(T):
    R = fio.readi()
    C = fio.readi()

    grid = []
    for r in range(R):
        grid.append(fio.readln())

    numchanges = get_min_required_changes(grid)

    fio.write_next_case(numchanges)

fio.close()
