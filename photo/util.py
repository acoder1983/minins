import re
import os
import sys
import time
import subprocess
from datetime import datetime
# python -m pip install -U hachoir


def get_file_min_date(f):
    p = subprocess.Popen(['hachoir-metadata.exe', f], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    s = str(out)
    dates = []
    r = re.compile('(\d{4}.\d{2}.\d{2})')
    dates += [int(d[:4] + d[5:7] + d[8:10]) for d in r.findall(s)
              if int(d[:4]) > 2000 and int(d[:4]) < 2030 and int(d[5:7]) < 13 and int(d[8:10]) < 32]
    ctime = os.path.getctime(f)
    dates.append(int(datetime.fromtimestamp(ctime).strftime('%Y%m%d')))
    mtime = os.path.getmtime(f)
    dates.append(int(datetime.fromtimestamp(mtime).strftime('%Y%m%d')))
    return str(min(dates))


def change_modify_time(f, date_str):
    d = datetime(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8]))
    os.utime(f, (d.timestamp(), d.timestamp()))


def main(f):
    # subfix=f[f.rfind('.')+1:].lower()
    # if subfix in ['jpg','jpeg','png','tiff']:
    #     print('pic')
    # elif subfix in ['mp4','mov']:
    #     print('vid')

    d = get_file_min_date(f)
    # print(d)
    change_modify_time(f, d)
    mtime = os.path.getmtime(f)
    print(datetime.fromtimestamp(mtime).strftime('%Y%m%d'))


if __name__ == '__main__':
    main(sys.argv[1])
