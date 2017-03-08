from Classes import *

def get_avg_val(vecs):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    num_v = float(len(vecs))
    for vec in vecs:
        x_sum += vec.x
        y_sum += vec.y
        z_sum += vec.z

    return Vec3(x_sum/num_v, y_sum/num_v, z_sum/num_v)
