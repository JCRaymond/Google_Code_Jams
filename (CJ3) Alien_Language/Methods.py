def parse_str(string):
    parsed = []

    str_index = 0
    while str_index < len(string):
        if string[str_index] == "(":
            possible = []
            str_index+=1
            while string[str_index] != ")":
                possible.append(string[str_index])
                str_index+=1
            str_index+= 1
            parsed.append(possible)
        else:
            parsed.append(string[str_index])
            str_index+=1

    return parsed


def word_fits_template(word, template):
    for i, car in enumerate(word):
        if car not in template[i]:
            return False
    return True


def count_dict_fits_to_template(dict, template):
    num = 0
    for word in dict:
        if word_fits_template(word, template):
            num+=1
    return num