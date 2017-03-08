from Utils.CJFileIO import CJFileIO
from Methods import *

fio = CJFileIO()

T = fio.readi()

for t in range(T):
    S = fio.readln()
    fio.write_next_case(get_containing_num(S))

fio.close()