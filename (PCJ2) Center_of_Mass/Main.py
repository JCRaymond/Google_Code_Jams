from Utils.CJFileIO import *
from Methods import *
from Classes import *

f = CJFileIO("B")

T = f.readi()

for t in range(T):
    N = f.readi()

    poss = []
    vels = []
    for n in range(N):
        poss.append(Vec3(f.readi(), f.readi(), f.readi()))
        vels.append(Vec3(f.readi(), f.readi(), f.readi()))

    avg_pos = get_avg_val(poss)
    avg_vel = get_avg_val(vels)

    center_pos = lambda t: avg_pos + (t * avg_vel)

    pdv = avg_pos*avg_vel
    vdv = avg_vel*avg_vel

    time = 0
    if vdv != 0:
        time = -pdv/vdv
    if time < 0:
        time = 0

    case = str(center_pos(time).lnorm(2)) + " " + str(time)
    f.write_next_case(case)
