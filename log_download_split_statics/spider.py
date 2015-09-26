#!/usr/bin/env python
import os

logpath="/usr/local/logs/2015-06-29logs"
os.chdir("%s"%logpath)
loglst=[]
for root,dirs,files in os.walk("%s"%logpath):
    for f in files:
        try:
            if f.split('.')[-1]=='log':
                loglst.append(f)
        except Exception ,e:
            pass

for flog in loglst:
    os.popen("egrep -i 'Baiduspider|Sogou web spider|360Spider' %s  >spider_%s "%(flog,flog))
    if os.path.getsize('spider_%s'%flog)== 0:
        os.remove('spider_%s'%flog)

