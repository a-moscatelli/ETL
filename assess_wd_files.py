wd='.'
fnpattern='.py'

import os
import hashlib
from functools import partial

def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()
                # https://stackoverflow.com/questions/7829499/using-hashlib-to-compute-md5-digest-of-a-file-in-python-3
[ print(fname,os.path.getsize(fname),md5sum(fname)) for fname in os.listdir(wd) if fnpattern in fname ]
# sqlserver_imp_exp.py 2168 6a0bf8773668b2e8a8731809b7f2daad