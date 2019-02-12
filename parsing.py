import mathematic


def replace(p):
    p = p.replace(' ', '')
    p = p.replace('X', 'x')
    p = p.replace('--', '+').replace('+-', '-').replace('-+', '-').replace('++', '+')
    p = p.replace('^', '').replace('*', '')
    p = p.replace('x-', 'x1-').replace('x+', 'x1+')
    p = p.replace('-x', '-1x').replace('+x', '+1x')
    if p[-1] == 'x':
        p = p + '1'
    if p[0] == 'x':
        p = '1' + p
    p = p.replace('-', '|-').replace('+', '|+')
    p = p.replace('+', '')
    if p[0] == '|':
        p = p[1:]
    splited = p.split('|')
    for i in range(len(splited)):
        if splited[i].find('x') == -1:
            splited[i] = splited[i] + 'x0'
    return splited


def sort_in_list(p):
    arr = []
    for i in range(len(p)):
        parts = p[i].split('x')
        arr.append(int(parts[1]))
    max_n = max(arr)
    list = [0] * (max_n + 1)
    for n in p:
        parts = n.split('x')
        i = int(parts[1])
        if mathematic.is_int(parts[0]):
            list[int(parts[1])] += int(parts[0])
        else:
            list[int(parts[1])] += float(parts[0])
    return list


def parse_polynom(p):
    parts = p.split('=')
    left_part = replace(parts[0])
    right_part = replace(parts[1])
    left_list = sort_in_list(left_part)
    right_list = sort_in_list(right_part)
    len_left = len(left_list)
    len_right = len(right_list)
    ret_list = [0] * max(len_left, len_right)
    for i in range(len_left):
        ret_list[i] += left_list[i]
    for i in range(len_right):
        ret_list[i] -= right_list[i]
    while ret_list[-1] == 0:
        ret_list.pop(-1)
    return ret_list
