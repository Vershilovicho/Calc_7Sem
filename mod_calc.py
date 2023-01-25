def sum_num(value1, value2):
    return value1 + value2


def sub_num(value1, value2):
    return value1 - value2


def mult_num(value1, value2):
    return value1 * value2


def div_num(value1, value2):
    return value1 / value2


def pow_num(value1, value2=None):
    if not value2:
        return value1 ** 0.5
    return value1 ** value2

# def pow2_num(value1):
#     return value1 ** 0.5

# def pow_num(value1, value2):
#     return value1 ** value2



def int_num(value1, value2):
    return value1 // value2


def percent_num(value1, value2):
    return round(value1 % value2, 2)
