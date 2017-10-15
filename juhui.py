import sys

def repay(base, r1, r2, taken):
    d = 0
    while True:
        p = base * r1
        if p<100 or p < taken:
            break
        base = base - p + (p-taken)*r2
        d += 1

    return d,base

if __name__ == '__main__':
    d,base=repay(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
    print('take %d days %d, remain %d' % (d, d*float(sys.argv[4])*0.8, base))