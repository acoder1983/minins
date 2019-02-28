import os
import sys
import time
import hashlib


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main(repo, tmp):
    repo_md5 = []
    for path, dir_list, file_list in os.walk(repo):
        for file_name in file_list:
            f = os.path.join(path, file_name)
            repo_md5.append(md5(f))
            print('add md5 %s' % f)
    repo_md5 = set(repo_md5)

    i = 0
    for path, dir_list, file_list in os.walk(tmp):
        for file_name in file_list:
            f = os.path.join(path, file_name)
            if md5(f) in repo_md5:
                os.remove(f)
                print('remove %s' % f)
                i += 1
    return i


if __name__ == '__main__':
    t = time.time()
    c = main(sys.argv[1], sys.argv[2])
    print('remove %d files, time cost: %d' % (c, time.time() - t))
