from Utils.CJFileIO import CJFileIO
from Methods import *

fio = CJFileIO()

T = int(fio.readln())

for t in range(T):
    S = fio.readln()
    fio.write_case(get_containing_num(S))

fio.close()