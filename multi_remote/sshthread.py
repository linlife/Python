#!/usr/bin/env python2.7
#coding:utf-8


import threading
import paramiko
import os
import sys

ip_list=['192.168.60.128','192.168.60.129']

def ssh(ip,command):#执行的命令方法
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,22,'root','centos')
    if ssh.connect:
        print 'remote machine %s successful'%ip
    stdin,stdout,stderr = ssh.exec_command(command)
    result=stdout.read()
    if not result:
        result=stderr.read()
    return result

def upfile(ip,addr):#上传文件方法
    t = paramiko.Transport((ip,22))
    t.connect(username='root',password='centos')
    sftp = paramiko.SFTPClient.from_transport(t)
    file_name=os.path.basename(addr)
    sftp.put(addr,'/tmp/'+file_name)

    t.close()
class MySSH(threading.Thread):#远程登录执行命令
    def __init__(self,ip,mycommand):
        self.__ip=ip
        self.__cmd=mycommand
        super(MySSH,self).__init__()

    def run(self):
        threading.Thread.run(self)
        result=ssh(self.__ip,self.__cmd)
        if result:
            print 'machine %s'%self.__ip
            print result
        else:
            print 'may be is an excute command or error'
            print result
class MyUpload(threading.Thread):#上传文件
    def __init__(self,ip,sour_addr):
        self.__ip=ip
        self.__sa=sour_addr
        super(MyUpload,self).__init__()
        print 'upload file to machine %s Successful!'%self.__ip


    def run(self):
        threading.Thread.run(self)
        upfile(self.__ip,self.__sa)

def menu():#总菜单
    prompt='''
    登录多台机器
    1)同时执行命令
    2）同时上传文件到tmp目录下
    3）退出
请选择：'''
    while True:
        try:
            choose=input(prompt)
        except Exception ,e:
            print 'please enter right number!'
        else:
            if choose==1:
                cmd=raw_input('your command>>>')
                for item in ip_list:
                    temp = MySSH(item,cmd)
                    temp.start()
                    temp.join()
            if choose ==2:
                while True:
                    addr=raw_input('please enter your full path file:')
                    if os.path.isfile(addr):
                        break
                    else:
                        print 'can\'t find this file'
                for item in ip_list:
                    temp=MyUpload(item,addr)
                    temp.start()
                    temp.join()
            if choose ==3:
                sys.exit()
                

if __name__=='__main__':
    menu() 

        
