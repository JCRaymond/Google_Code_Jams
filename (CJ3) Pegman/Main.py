from Utils.CJFileIO import *
from Methods import *

fio = CJFileIO()

T = int(fio.readln())

for t in range(T):
    R = int(fio.read())
    C = int(fio.read())

    grid = []
    for r in range(R):
        grid.append(fio.readln())

    numchanges = get_min_required_changes(grid)

    fio.write_case(numchanges)

fio.close()
