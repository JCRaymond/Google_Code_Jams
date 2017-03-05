lowest = 0

def get_num_symbols(string):
    symbols = []
    for car in string:
        if car not in symbols:
            symbols.append(car)
    return len(symbols)

def get_lowest_num(string):
    if len(string) < 1:
        return ""
    symbol_val = {string[0]:chr(lowest+1),}
    num = str(chr(lowest+1))
    string = string[1:]
    val = lowest
    for car in string:
        if car not in symbol_val.keys():
            symbol_val[car] = chr(val)
            val+=1
            if val == lowest+1:
                val+=1

        num += symbol_val[car]
    return num

def to_base_10(num, base):
    return sum([(ord(val)-lowest)*pow(base, exp) for exp, val in enumerate(num[::-1])])