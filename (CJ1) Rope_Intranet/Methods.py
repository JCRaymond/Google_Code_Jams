def get_num_intersects(wires):
    intersections = 0
    for w1 in wires:
        for w2 in wires:
            if w1 != w2:
                if ((w1[0] - w2[0]) * (w1[1] - w2[1]) < 0):
                    intersections += 1
    intersections /= 2

    return intersections