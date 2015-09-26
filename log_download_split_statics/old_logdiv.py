#!/usr/bin/env python

import urllib2
import urllib
import os
import re
import sys
import time

atime=time.time()-60*60*24*2
mydate=time.strftime('%Y%m%d',time.localtime(atime))
logurl='http://logcenter.chinacache.com/URLGetter?username=shqijia&password=]QK2mj}lvs&date=%s'%mydate
logsdir='/usr/local/logs/logsdownload'

def logdir(date):
    os.chdir("/usr/local/logs")
    logsdir=date+'logs'
    if os.path.isdir(logsdir):
        sys.exit(0)
    else:
        os.mkdir(logsdir)
    


def urlloglist(url):
    f=urllib2.urlopen(url)
    urllist=f.readlines()
    f.close()
    for i,j in enumerate(urllist):
        urllist[i]=urllist[i][:-2]
    return urllist
        
def downloadlogs():
    if os.path.isdir(logsdir):
        os.popen("rm -rf %s"%logsdir)
    else:
        os.mkdir(logsdir)
    loglst=urlloglist(logurl)
    for line in loglst:
        if re.match('.*\.gz$',line):
            logname=line.split('/')[-1]
            localsz=logsdir+'/'+logname
            urllib.urlretrieve(line,localsz)
    os.popen("gzip -d *.gz")

def writelogtofile(filename,logcontent):
    with open(filename,'a') as f:
        f.write(logcontent+'\n')

def logsfiles():
    lst=[]
    for root, dirs, files in os.walk(logsdir):
        for file in files:
            lst.append(root+'/'+file)
    return lst
    

def divlogs():
    lst=logsfiles()
    logsdir=mydate+'logs'
    os.chdir('/usr/local/logs/%s'%logsdir)
    for file in lst:
        with open(file) as f:
            loglst=f.readlines()
            for i,j in enumerate(loglst):
                loglst[i]=loglst[i].strip()
                if "ChinaCache" in loglst[i]:
                    try:
                        logname='error.log'
                        writelogtofile(logname,loglst[i])
                        #os.popen("echo %s >> /usr/local/logs/20150610_error.log"%loglst[i])
                    except Exception ,e:
                        print 'read ',loglst[i],'error'
                
                elif "http://" in loglst[i]:
                    try:
                        logname=loglst[i].split('http://')[1].split('/')[0].strip()
                        logname=logname+'.log'
                        writelogtofile(logname,loglst[i])
                    except Exception,e:
                        print logname ,'error',loglst[i]
                elif "https://" in loglst[i]:
                    try:
                        logname=loglst[i].split('https://')[1].split('/')[0].strip()
                        logname=logname+'.log'
                        writelogtofile(logname,loglst[i])
                    except Exception,e:
                        print logname ,'error',loglst[i]
    os.chdir("/usr/local/logs")
    os.popen("rm -rf %s"%logsdir)

def menu():
    downloadlogs()
    logdir(mydate)
    divlogs()
    
                    

if __name__=='__main__':
    menu()
