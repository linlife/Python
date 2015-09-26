#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015��3��27��
@author : Lin
'''
import MySQLdb
import conf

class MySqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict

    
    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)
        data =cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    
    def Get_One(self,sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql)
        data =cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    
    def Set_one(self,sql):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur=conn.cursor()
        
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
    def Insert_one(self,sql,params):
        conn = MySQLdb.connect(**self.__conn_dict)
        cur=conn.cursor()
        
        cur.execute(sql,params)
        conn.commit()
        
        cur.close()
        conn.close()
        
        
    