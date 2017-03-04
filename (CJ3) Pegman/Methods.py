from Classes import *

dirs = {"^": Dir(-1, 0), ">": Dir(0, 1), "v": Dir(1, 0), "<": Dir(0, -1)}

def pointing_to_arrow(r, c, grid):
    p = Pos(r, c, Bounds(0, len(grid)), Bounds(0, len(grid[0])))
    dir = dirs[grid[r][c]]
    p+=dir
    while p.is_in_bounds():
        if grid[p.x][p.y] in dirs.keys():
            return True
        p += dir
    return False

def can_point_to_arrow(r, c, grid):
    for dir in dirs.values():
        p = Pos(r, c, Bounds(0, len(grid)), Bounds(0, len(grid[0])))
        p+=dir
        while p.is_in_bounds():
            if grid[p.x][p.y] in dirs.keys():
                return True
            p += dir
    return False

def get_min_required_changes(grid):
    numchanges = 0
    for r, row in enumerate(grid):
        for c, spot in enumerate(row):
            if spot != ".":
                if pointing_to_arrow(r, c, grid):
                    pass
                elif can_point_to_arrow(r, c, grid):
                    numchanges += 1
                else:
                    numchanges = "IMPOSSIBLE"
                    break
        else:
            continue
        break

    return numchanges