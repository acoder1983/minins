import os
import sys
import util
import time
from collections import defaultdict


def modify(folder):
    mod_c = 0
    for path, dir_list, file_list in os.walk(folder):
        for file_name in file_list:
            f = os.path.join(path, file_name)
            min_date = util.get_file_min_date(f)
            util.change_modify_time(f, min_date)
            print('change %s' % f)
            mod_c += 1
    return mod_c


if __name__ == '__main__':
    t = time.time()
    c = modify(sys.argv[1])
    print('modify %d files, time cost: %d' % (c, time.time() - t))
