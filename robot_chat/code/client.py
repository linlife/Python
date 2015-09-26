#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015��3��27��
@author : Lin
'''

import socket
from ToMysql.sql_admin import SqlAdmin

def create_recordtable(name):#创建记录表
    admin=SqlAdmin()
    table_list=[]
    mysql_tables=admin.check_tables()
    for dic in mysql_tables:
        for i in dic:
            table_list.append(dic[i])
    if name not in table_list:
        admin.create_table(name)
    else:
        print 'exist table %s'%name
def write_recordtable(name,client_data,server_data):#记录聊天到对应表里面
    admin=SqlAdmin()
    admin.insert_data_to_table(name, client_data, server_data)
    
    

def MyName():
    name=raw_input('please login with your name:')
    return name

def Chat(name):
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_port=('127.0.0.1',9999)
    client.connect(ip_port)
    data=client.recv(1024)
    print data
    while True:    
        inp = raw_input('client:')
        client.send(inp)
        if inp == 'q':
            break
        data=client.recv(1024)
        print data
        write_recordtable(name,inp,data)
def check_record(name):
    admin=SqlAdmin()
    check_result=admin.check_record(name)
    for eachline in check_result:
        print eachline
    

def menu():
    name=MyName()
    create_recordtable(name)
    prompt='''
    1)go to chat
    2)check chat record
    3)quit
    please choose:'''
    while True:
        try:
            choice=input(prompt)
        except Exception, e:
            print 'please choose number'
        else:
            if choice==1:Chat(name)
            if choice==2:check_record(name)
            if choice==3:break
            
if __name__=='__main__':
    menu()