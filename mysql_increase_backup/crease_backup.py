#!/usr/bin/env python


'''
@uthor by lin 2015.05.07
'''
import os
import shelve
import paramiko

os.chdir('/root/mysqlcpy')
dirlst=os.listdir('/root/mysqlcpy')

def check_shelvedb():
    if os.path.isfile('/root/test/myshel.db'):
        f=shelve.open('/root/test/myshel.db')
        tmp_num=f['record']
        f.close()
    else:
        f=shelve.open('/root/test/myshel.db')
        f['record']=0
        tmp_num=f['record']
        f.close()
    return tmp_num

def change_num(mynum):
    f=shelve.open('/root/test/myshel.db')
    f['record']=mynum
    f.close()
def parasend(mylog):
    private_key_path='/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_path)
    t = paramiko.Transport(('192.168.99.56',22))
    t.connect(username='root',pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put('/root/mysqlcpy/%s'%mylog,'/root/myrecv/%s'%mylog)
    t.close()


def cp_list(dirlst):
    my_list=[]
    for i in dirlst:
        if os.path.isfile(i) and 'mysql-bin' in i:
            my_list.append(i)
    my_list.sort()
    my_list.remove(my_list[-1])
    return my_list

def menu():
    lst=cp_list(dirlst)
    num=check_shelvedb()
    for i in lst:
        if int(i.split('.')[1])>num:
            parasend(i)
    change_num(int(lst[-1].split('.')[1]))
    print 'ok'

if __name__=='__main__':
    menu()
