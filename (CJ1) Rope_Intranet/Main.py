from Utils.CJFileIO import *
from Methods import *

fio = CJFileIO()

t = int(fio.readln())

for j in range(t):
    n = int(fio.readln())

    wires = []
    for i in range(n):
        w = fio.readln()
        w = w.split(" ")
        wires.append((int(w[0]), int(w[1])))

    ints = get_num_intersects(wires)

    fio.write_case(ints)

fio.close()