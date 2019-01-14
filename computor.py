import sys
import re
import mathematic
import Polynom


def parse_polynom(av):
    list = av.split(' = ')
    # print('list = ' + str(list))
    left_list = re.compile('\*X\^.').split(list[0].replace(' ', ''))
    del left_list[-1]
    # print('left_list = ' + str(left_list))
    right_list = re.compile('\*X\^.').split(list[1].replace(' ', ''))
    del right_list[-1]
    # print('right_list = ' + str(right_list))
    ret_list = []
    for n in left_list:
        if mathematic.is_int(n):
            ret_list.append(int(n))
        else:
            ret_list.append(float(n))
    for i in range(len(right_list)):
        if len(ret_list) > i:
            if mathematic.is_int(right_list[i]):
                ret_list[i] -= int(right_list[i])
            else:
                ret_list[i] -= float(right_list[i])
        else:
            if mathematic.is_int(right_list[i]):
                ret_list.append(-int(right_list[i]))
            else:
                ret_list.append(-float(right_list[i]))
    # print('ret_list = ' + str(ret_list))
    return ret_list


def main(argc, argv):
    if argc == 2:
        polynom = Polynom.Polynom(parse_polynom(argv[1]))
        print('Reduced form: ' + polynom.redused_form)
        print('Polynomial degree: ' + polynom.degree)
        polynom.print_roots()
    else:
        print('argc error')


main(len(sys.argv), sys.argv)
