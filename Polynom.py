import mathematic

_EPS = 0.00000000001


class Polynom:
    def __init__(self, polynom_list):
        self.__polynom_list = polynom_list
        self.__degree = self.__calculate_degree(polynom_list)
        self.__redused_form = self.__go_to_reduced(polynom_list)
        print('Polynom_list = ' + str(polynom_list))

    @property
    def degree(self):
        return str(self.__degree)

    @property
    def redused_form(self):
        return self.__redused_form

    def print_roots(self):
        if self.__degree > 2:
            print('The polynomial degree is stricly greater than 2, I can\'t solve.')
        elif self.__degree == 2:
            a = self.__polynom_list[2]
            b = self.__polynom_list[1]
            c = self.__polynom_list[0]
            d = b * b - 4 * a * c
            if d < 0:
                print('Discriminant is strictly negative, the two complex solutions are:')
                print(str(-b / (2 * a)) + ' + i * ' + str(mathematic.sqrt(mathematic.fabs(d), _EPS) / (2 * a)))
                print(str(-b / (2 * a)) + ' - i * ' + str(mathematic.sqrt(mathematic.fabs(d), _EPS) / (2 * a)))
            elif d == 0:
                print('Discriminant equals to zero, the one solution is:')
                print(-b / 2 * a)
            else:
                print('Discriminant is strictly positive, the two solutions are:')
                print((-b + mathematic.sqrt(d, _EPS)) / (2 * a))
                print((-b - mathematic.sqrt(d, _EPS)) / (2 * a))
        elif self.__degree == 1:
            a = self.__polynom_list[0]
            b = self.__polynom_list[1]
            x = -a/b
            if mathematic.is_int(x):
                x = int(x)
            print('The solution is:\n' + str(x))
        else:
            a = self.__polynom_list[0]
            if a == 0:
                print('The solution are: all the real numbers')
            else:
                print('The equation has no solution')

    @staticmethod
    def __calculate_degree(polynom_list):
        degree = len(polynom_list) - 1
        while polynom_list[degree] == 0 and degree != 0:
            degree -= 1
        return degree

    @staticmethod
    def __go_to_reduced(polynom_list):
        ret = ''

        # i = 0
        if polynom_list[0] < 0:
            ret += ' - ' + str(mathematic.fabs(polynom_list[0])) + ' * X^0 '
        else:
            ret += str(mathematic.fabs(polynom_list[0])) + ' * X^0 '

        # i = [1,len]
        for i in range(1, len(polynom_list)):
            if polynom_list[i] < 0:
                ret += '- '
            else:
                ret += '+ '
            ret += str(mathematic.fabs(polynom_list[i])) + ' * X^' + str(i) + ' '
        ret += '= 0'
        return ret



