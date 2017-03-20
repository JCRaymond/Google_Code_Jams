from Utils.CJFileIO import *

f = CJFileIO(pracnum = 2)

T = f.readi()

for t in range(T):
    N = f.readi()

    names = [f.readln() for n in range(N)]
    last_name = names[0]
    cost = 0
    for name in names:
        if name < last_name:
            cost += 1
        else:
            last_name = name

    f.write_next_case(cost)

f.close()