from Utils.CJFileIO import CJFileIO
from Methods import *

fio = CJFileIO()

L = fio.readi()
D = fio.readi()
N = fio.readi()

dict = []
for i in range(D):
    dict.append(fio.readln())

for i in range(N):
    string = fio.readln()
    template = parse_str(string)
    num_matches = count_dict_fits_to_template(dict, template)
    fio.write_next_case(num_matches)

fio.close()