# пример реализации программы, которая ожидает получить в параметрах список чисел в системе счисления с основанием,
# переданном в параметре base (если он не указан, то подразумевается двоичная система счисления) и переводит их в
# десятичную. Преобразованный список чисел выводится на экран.

import argparse
import sys

parser = argparse.ArgumentParser(
    description='convert integers to decimal system')
parser.add_argument('integers', metavar='integers', nargs='+', type=str,
                    help='integers to be converted')
parser.add_argument('--base', default=2, type=int,
                    help='default numeric system')
parser.add_argument('--log', default=sys.stdout,
                    type=argparse.FileType('w'),
                    help='the file where converted data should be written')

args = parser.parse_args()
s = ' '.join(map(lambda x: str(int(x, args.base)), args.integers))
args.log.write(s + '\n')
args.log.close()