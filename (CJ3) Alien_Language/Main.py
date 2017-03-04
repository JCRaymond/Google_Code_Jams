from Utils.CJFileIO import CJFileIO
from Methods import *

fio = CJFileIO()

L = int(fio.read())
D = int(fio.read())
N = int(fio.read())

dict = []
for i in range(D):
    dict.append(fio.readln())

for i in range(N):
    string = fio.readln()
    template = parse_str(string)
    num_matches = count_dict_fits_to_template(dict, template)
    fio.write_case(num_matches)

fio.close()