n = int(input())
for i in range(n + 1):
    k = int(input())
    if k != 0:
        s = n - i
        if k > 1:
            if s == 0:
                print(' +', k)
            elif s == 1:
                print(' + ' + str(k) + 'x', end='')
            elif s == n:
                print(str(k) + 'x **', s, end='')
            else:
                print(' + ' + str(k) + 'x **', s, end='')
        else:
            if s == 0:
                print(' +', k)
            elif s == 1:
                print(' + ' + 'x', end='')
            elif s == n:
                print('x **', s, end='')
            else:
                print(' + ' + 'x **', s, end='')