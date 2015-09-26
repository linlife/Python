#!/usr/bin/env python

import urllib2
import urllib
import os
import re
import sys
import time

atime=time.time()-60*60*24*1
mydate=time.strftime('%Y-%m-%d',time.localtime(atime))
loglst=[]
logsdir=mydate+'logs'
downloadurl={
             'i8.tg.com.cn':'http://223.203.224.40/%s/76/027/i8.tg.com.cn.log.gz'%mydate,\
             'www.jia.com':'http://223.203.224.40/%s/06/140/www.jia.com.log.gz'%mydate,\
             'qingdao.jia.com':'http://223.203.224.40/%s/68/456/qingdao.jia.com.log.gz'%mydate,\
             'sdhz.jia.com':'http://223.203.224.40/%s/10/401/sdhz.jia.com.log.gz'%mydate,\
             'jinan.jia.com':'http://223.203.224.40/%s/93/369/jinan.jia.com.log.gz'%mydate,\
             'sdjz.jia.com':'http://223.203.224.40/%s/52/535/sdjz.jia.com.log.gz'%mydate,\
             'sdly.jia.com':'http://223.203.224.40/%s/53/925/sdly.jia.com.log.gz'%mydate,\
             'sdwf.jia.com':'http://223.203.224.40/%s/55/525/sdwf.jia.com.log.gz'%mydate,\
             'sdzz.jia.com':'http://223.203.224.40/%s/88/608/sdzz.jia.com.log.gz'%mydate,\
             'suzhou.jia.com':'http://223.203.224.40/%s/13/481/suzhou.jia.com.log.gz'%mydate,\
             'changzhou.jia.com':'http://223.203.224.40/%s/32/443/changzhou.jia.com.log.gz'%mydate,\
             'jsha.jia.com':'http://223.203.224.40/%s/21/652/jsha.jia.com.log.gz'%mydate,\
             'kunshan.jia.com':'http://223.203.224.40/%s/29/162/kunshan.jia.com.log.gz'%mydate,\
             'jslyg.jia.com':'http://223.203.224.40/%s/68/296/jslyg.jia.com.log.gz'%mydate,\
             'nanjing.jia.com':'http://223.203.224.40/%s/22/202/nanjing.jia.com.log.gz'%mydate,\
             'nantong.jia.com':'http://223.203.224.40/%s/06/890/nantong.jia.com.log.gz'%mydate,\
             'jstz.jia.com':'http://223.203.224.40/%s/98/059/jstz.jia.com.log.gz'%mydate,\
             'wuxi.jia.com':'http://223.203.224.40/%s/90/119/wuxi.jia.com.log.gz'%mydate,\
             'jsxz.jia.com':'http://223.203.224.40/%s/82/328/jsxz.jia.com.log.gz'%mydate,\
             'jsyz.jia.com':'http://223.203.224.40/%s/53/395/jsyz.jia.com.log.gz'%mydate,\
             'hangzhou.jia.com':'http://223.203.224.40/%s/73/377/hangzhou.jia.com.log.gz'%mydate,\
             'jiaxing.jia.com':'http://223.203.224.40/%s/73/297/jiaxing.jia.com.log.gz'%mydate,\
             'ningbo.jia.com':'http://223.203.224.40/%s/96/389/ningbo.jia.com.log.gz'%mydate,\
             'shaoxing.jia.com':'http://223.203.224.40/%s/72/717/shaoxing.jia.com.log.gz'%mydate,\
             'zjwz.jia.com':'http://223.203.224.40/%s/98/269/zjwz.jia.com.log.gz'%mydate,\
             'hefei.jia.com':'http://223.203.224.40/%s/68/346/hefei.jia.com.log.gz'%mydate,\
             'ahsz.jia.com':'http://223.203.224.40/%s/37/763/ahsz.jia.com.log.gz'%mydate,\
             'shenzhen.jia.com':'http://223.203.224.40/%s/04/460/shenzhen.jia.com.log.gz'%mydate,\
             'gddg.jia.com':'http://223.203.224.40/%s/75/197/gddg.jia.com.log.gz'%mydate,\
             'gdfs.jia.com':'http://223.203.224.40/%s/09/260/gdfs.jia.com.log.gz'%mydate,\
             'guangzhou.jia.com':'http://223.203.224.40/%s/33/583/guangzhou.jia.com.log.gz'%mydate,\
             'huizhou.jia.com':'http://223.203.224.40/%s/27/592/huizhou.jia.com.log.gz'%mydate,\
             'fuzhou.jia.com':'http://223.203.224.40/%s/02/860/fuzhou.jia.com.log.gz'%mydate,\
             'nanning.jia.com':'http://223.203.224.40/%s/98/269/nanning.jia.com.log.gz'%mydate,\
             'gxlz.jia.com':'http://223.203.224.40/%s/42/474/gxlz.jia.com.log.gz'%mydate,\
             'zhengzhou.jia.com':'http://223.203.224.40/%s/55/415/zhengzhou.jia.com.log.gz'%mydate,\
             'wuhan.jia.com':'http://223.203.224.40/%s/66/636/wuhan.jia.com.log.gz'%mydate,\
             'changsha.jia.com':'http://223.203.224.40/%s/54/585/changsha.jia.com.log.gz'%mydate,\
             'hnyy.jia.com':'http://223.203.224.40/%s/45/284/hnyy.jia.com.log.gz'%mydate,\
             'nanchang.jia.com':'http://223.203.224.40/%s/13/371/nanchang.jia.com.log.gz'%mydate,\
             'shenyang.jia.com':'http://223.203.224.40/%s/18/811/shenyang.jia.com.log.gz'%mydate,\
             'dalian.jia.com':'http://223.203.224.40/%s/66/526/dalian.jia.com.log.gz'%mydate,\
             'dandong.jia.com':'http://223.203.224.40/%s/52/685/dandong.jia.com.log.gz'%mydate,\
             'haerbin.jia.com':'http://223.203.224.40/%s/28/912/haerbin.jia.com.log.gz'%mydate,\
             'changchun.jia.com':'http://223.203.224.40/%s/58/525/changchun.jia.com.log.gz'%mydate,\
             'jljl.jia.com':'http://223.203.224.40/%s/07/410/jljl.jia.com.log.gz'%mydate,\
             'chengdu.jia.com':'http://223.203.224.40/%s/09/580/chengdu.jia.com.log.gz'%mydate,\
             'kunming.jia.com':'http://223.203.224.40/%s/80/008/kunming.jia.com.log.gz'%mydate,\
             'guiyang.jia.com':'http://223.203.224.40/%s/79/657/guiyang.jia.com.log.gz'%mydate,\
             'shijiazhuang.jia.com':'http://223.203.224.40/%s/40/324/shijiazhuang.jia.com.log.gz'%mydate,\
             'handan.jia.com':'http://223.203.224.40/%s/25/732/handan.jia.com.log.gz'%mydate,\
             'hbts.jia.com':'http://223.203.224.40/%s/32/523/hbts.jia.com.log.gz'%mydate,\
             'hbxt.jia.com':'http://223.203.224.40/%s/57/535/hbxt.jia.com.log.gz'%mydate,\
             'taiyuan.jia.com':'http://223.203.224.40/%s/96/099/taiyuan.jia.com.log.gz'%mydate,\
             'sxjc.jia.com':'http://223.203.224.40/%s/29/022/sxjc.jia.com.log.gz'%mydate,\
             'xian.jia.com':'http://223.203.224.40/%s/81/818/xian.jia.com.log.gz'%mydate,\
             'wulumuqi.jia.com':'http://223.203.224.40/%s/10/781/wulumuqi.jia.com.log.gz'%mydate,\
             'qhxn.jia.com':'http://223.203.224.40/%s/96/899/qhxn.jia.com.log.gz'%mydate,\
             'beijing.jia.com':'http://223.203.224.40/%s/23/732/beijing.jia.com.log.gz'%mydate,\
             'chongqing.jia.com':'http://223.203.224.40/%s/97/779/chongqing.jia.com.log.gz'%mydate,\
             'shanghai.jia.com':'http://223.203.224.40/%s/42/064/shanghai.jia.com.log.gz'%mydate,\
             'tianjin.jia.com':'http://223.203.224.40/%s/00/890/tianjin.jia.com.log.gz'%mydate,\
             'jiaju.jia.com':'http://223.203.224.40/%s/80/598/jiaju.jia.com.log.gz'%mydate,\
             'mall.jia.com':'http://223.203.224.40/%s/31/113/mall.jia.com.log.gz'%mydate,\
             'tg.jia.com':'http://223.203.224.40/%s/18/501/tg.jia.com.log.gz'%mydate,\
             'pinpai.jia.com':'http://223.203.224.40/%s/78/387/pinpai.jia.com.log.gz'%mydate,\
             'tuku.jia.com':'http://223.203.224.40/%s/66/726/tuku.jia.com.log.gz'%mydate,\
             'zixun.jia.com':'http://223.203.224.40/%s/13/391/zixun.jia.com.log.gz'%mydate,\
             'm.jia.com':'http://223.203.224.40/%s/28/182/m.jia.com.log.gz'%mydate,\
             'mtgi1.jia.com':'http://223.203.224.40/%s/09/540/mtgi1.jia.com.log.gz'%mydate,\
             'mtgi2.jia.com':'http://223.203.224.40/%s/68/796/mtgi2.jia.com.log.gz'%mydate,\
             'mtgi3.jia.com':'http://223.203.224.40/%s/27/052/mtgi3.jia.com.log.gz'%mydate,\
             'mi1.jia.com':'http://223.203.224.40/%s/32/313/mi1.jia.com.log.gz'%mydate,\
             'mi2.jia.com':'http://223.203.224.40/%s/73/057/mi2.jia.com.log.gz'%mydate,\
             'mi3.jia.com':'http://223.203.224.40/%s/14/801/mi3.jia.com.log.gz'%mydate,\
             'mued1.jia.com':'http://223.203.224.40/%s/35/553/mued1.jia.com.log.gz'%mydate,\
             'mued2.jia.com':'http://223.203.224.40/%s/94/809/mued2.jia.com.log.gz'%mydate,\
             'mued3.jia.com':'http://223.203.224.40/%s/53/065/mued3.jia.com.log.gz'%mydate,\
             #'tuku-wap.m.jia.com':''%mydate,\
             #'zhuangxiu.jia.com':''%mydate,\
             #'i1.tg.com.cn':''%mydate,\
             }



def logdir(mydate):
    os.chdir("/usr/local/logs")
    if os.path.isdir(logsdir):
        sys.exit(0)
    else:
        os.mkdir(logsdir)

        
def downloadlogs():
    os.chdir("/usr/local/logs/%s"%logsdir)
    for line in downloadurl.values():
        logname=line.split('/')[-1]
        urllib.urlretrieve(line,logname)
    os.popen("gzip -d *.gz")

def spiderlog():
    os.chdir("/usr/local/logs/%s"%logsdir)
    for root,dirs,files in os.walk("/usr/local/logs/%s"%logsdir):
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



def menu():
    logdir(mydate)
    downloadlogs()
    spiderlog()
                    

if __name__=='__main__':
    menu()
