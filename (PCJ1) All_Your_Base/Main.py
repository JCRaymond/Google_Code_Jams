from Utils.CJFileIO import *
from Methods import *

fio = CJFileIO()

T = int(fio.read())

for t in range(T):
    num = fio.readln()
    base = get_num_symbols(num)
    if base < 2:
        base = 2
    num = get_lowest_num(num)
    print num
    num10 = to_base_10(num, base)
    fio.write_next_case(num10)

fio.close()
