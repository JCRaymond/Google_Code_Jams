
def cache(f):
    cache = {}

    def newfunc(*args):
        if cache.get(args) == None:
            cache[args] = f(*args)
        return cache[args]

    return newfunc


def calc_cost(N, rem_cells):
    concurr_cells = [(1, N)]
    cost = 0
    for cell in rem_cells:
        for start, end in concurr_cells:
            if cell >= start and cell <= end:
                cost += end-start
                concurr_cells.remove((start, end))
                if start <= cell-1:
                    concurr_cells.append((start, cell-1))
                if end >= cell+1:
                    concurr_cells.append((cell+1, end))
                break
    return cost

######################################
#This is not my solution, it is a python adaptation of the solution given by the judge.
#The method by which I approached this problem generated a correct solution more often than not,
#but it turns out that it did not cover all cases. I ended up programming this so I could determine
#which cases I was getting wrong, but had no idea how to modify my previous method to work for this case

def get_min_costs_between_cells(c1, c2, cells):
    def calc_min_cost(a, b):
        cost = 0
        for cell in cells:
            if cell >= a and cell <= b:
                temp = b-a + calc_min_cost(a, cell-1) + calc_min_cost(cell+1, b)
                if not cost or temp<cost:
                    cost = temp
        return cost
    calc_min_cost = cache(calc_min_cost)

    return calc_min_cost(c1,c2)

def alt_get_lowest_cost(N, cells):
    return get_min_costs_between_cells(1, N, cells)

######################################