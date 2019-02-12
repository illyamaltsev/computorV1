import sys
from Polynom import Polynom
from parsing import parse_polynom
from validate import validate


def main(argc, argv):
    if argc == 2 and validate(argv[1]):
        polynom = Polynom(parse_polynom(argv[1]))
        print('Reduced form: ' + polynom.redused_form)
        print('Polynomial degree: ' + polynom.degree)
        polynom.print_roots()
    else:
        print('argc error')


main(len(sys.argv), sys.argv)
