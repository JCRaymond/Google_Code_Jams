def contains_letters(string, chars):
    s1 = "".join([char for char in string])
    for char in chars:
        if char in s1:
            index = s1.rfind(char)
            s1 = s1[:index] + s1[index+1:]
        else:
            return False
    return True


def remove_letters(string, chars):
    if not contains_letters(string, chars):
        return False

    for char in chars:
        index = string.rfind(char)
        string = string[:index] + string[index+1:]

    return string


def get_containing_num(string):
    string = string.upper()
    outnum = ""
    nums = ("ZERO", "TWO", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ONE", "THREE")
    num_dict = {"ZERO":"0", "ONE":"1", "TWO":"2", "THREE":"3", "FOUR":"4", "FIVE":"5", "SIX":"6", "SEVEN":"7", "EIGHT":"8", "NINE":"9"}
    index = 0
    while index < len(nums) and len(string) > 0:
        num = nums[index]
        res = remove_letters(string, num)
        if res != False:
            outnum += num_dict[num]
            string = res
        else:
            index += 1
    outnum = "".join(sorted([a for a in outnum]))
    return outnum