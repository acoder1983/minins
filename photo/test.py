import re
import os
import sys
import time
import subprocess
from datetime import datetime
# python -m pip install -U hachoir

def main(f):
    # subfix=f[f.rfind('.')+1:].lower()
    # if subfix in ['jpg','jpeg','png','tiff']:
    #     print('pic')
    # elif subfix in ['mp4','mov']:
    #     print('vid')
    p=subprocess.Popen(['hachoir-metadata.exe',f], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    s=str(out)
    dates=[]
    r=re.compile('(\d{4}.\d{2}.\d{2})')
    dates+=list(filter(lambda x:x>19700000 and x<20300000 ,[int(d[:4]+d[5:7]+d[8:10]) for d in r.findall(s)]))
    ctime=os.path.getctime(f)
    dates.append(int(datetime.fromtimestamp(ctime).strftime('%Y%m%d')))
    mtime=os.path.getmtime(f)
    dates.append(int(datetime.fromtimestamp(mtime).strftime('%Y%m%d')))
    print(dates)
    print(min(dates))
#     r=p.wait()
    

if __name__ == '__main__':
    main(sys.argv[1])
    