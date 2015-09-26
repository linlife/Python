#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015��3��27��
@author : Lin
'''

import sql_helper

class SqlAdmin(object):
    def __init__(self):
        self.__helper=sql_helper.MySqlHelper()
    
    def check_tables(self):#检查所有建立的表
        sql='show tables'
        params=None
        return self.__helper.Get_Dict(sql, params)
    
    def create_table(self,name):#新建表
        sql='create table %s(client varchar(100),server varchar(100))'%name
        self.__helper.Set_one(sql)
    def insert_data_to_table(self,name,client_data,server_data):#给表加数据
        sql='insert into %s(client,server)'%name+'values(%s,%s)'
        params=(client_data,server_data)
        self.__helper.Insert_one(sql, params)
    def auto_reply(self):#自动回复
        sql='select * from autoreply'
        params=None
        return self.__helper.Get_Dict(sql, params)
    def check_record(self,name):#查询聊天记录
        sql='select * from %s'%name
        return self.__helper.Get_One(sql)
    
    
        

        
        
        
    