#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015��3��27��
@author : Lin
'''


import SocketServer
from ToMysql.sql_admin import SqlAdmin
class  MyServer(SocketServer.BaseRequestHandler):
    
    def setup(self):
        pass

    def server_reply(self,data):
        admin=SqlAdmin()
        result='Hi'
        reply_dicts=admin.auto_reply()
        for line_dict in reply_dicts:
            for i in line_dict:
                if i == 'rev' and data.lower() in line_dict[i].lower():
                    result=line_dict['reply']
        return result
        
        
    def handle(self):
        conn =self.request
        conn.send('This is robot Tom!')
        flag=True
        while flag:
            data=conn.recv(1024)
            print data
            result=MyServer.server_reply(self, data)
            if data=='q':
                flag=False
            conn.send(result)
        conn.close()

    def finish(self):
        pass
        
if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.serve_forever()