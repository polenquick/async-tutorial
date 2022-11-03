# u need components to build a pc - minimum 4,2,3 to build one 1
# if u have 5,5,5 u can still build only one pc
# def get_full_pc_count(a, b, c) -> int:
#     if a >= 4 and b >= 2 and c >= 3:
#         return min(a // 4, b // 2, c // 3)
#     return 0
#
# print(get_full_pc_count(5, 5, 3))



def get_ratio():
    w = [2, 0, 0, 4, 5, 6, 7, 8, 9, 0]
    b = sorted(w)
    c = sum(b[:3])
    d = sum(b[-3:])
    try:
        (d / c)
    except ZeroDivisionError:
        print("błąd - dzielisz przez zero")
    # if c == 0:
    #     print('nie dziel przez 0')

    print(sum(w[:3]))
    print(b)
    print(c)
    print(d)


def get_good_average():
    w = [5, 4, 2, 6, 2, 6, 7, 8, 3, 2, 5, 86, 96, 43, 34, 53, 74, 36, 10, 10]
    d = sorted(w)
    e = d[4:-4]
    f = sum(d[4:-4]) / len(d[4:-4])
    h = d[int(len(d) * 0.25): -int(len(d) * 0.25)]
    i = sum(h)/len(h)
    print(e)
    print(f)
    print(h)
    print(i)

get_ratio()
# get_good_average()