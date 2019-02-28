import os
import sys
import util
import time
from collections import defaultdict


def clean(folder):
    del_c = 0
    for path, dir_list, file_list in os.walk(folder):
        for file_name in file_list:
            f = os.path.join(path, file_name)
            min_date = util.get_file_min_date(f)
            date_dir = path[-10:].replace('-', '')
            if min_date != date_dir:
                os.remove(f)
                del_c += 1
                print('\nremove %s' % f)
            sys.stdout.write('.')
    return del_c


if __name__ == '__main__':
    t = time.time()
    c = clean(sys.argv[1])
    print('clean %d files, time cost: %d' % (c, time.time() - t))
