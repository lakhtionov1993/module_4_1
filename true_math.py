from math import inf
def divide(first, second):
    division = 0
    if second == 0:
        division = inf
    else:
        division = first / second
    return division


# 2 вариант
#
# def divide(first, second):
#     if second == 0:
#         return inf
#     return first / second
