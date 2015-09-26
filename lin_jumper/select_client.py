#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015��4��8��
@author : Lin
'''

import socket
import sys
 
messages = [ 'This is the message. ',
             'It will be sent ',
             'in parts.',
             ]
server_address = ('localhost', 10000)
 
# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ] 
# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
for s in socks:
    s.connect(server_address)#建立连接
 
for message in messages:
 
    # Send messages on both sockets
    for s in socks:
        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
        s.send(message)#发送数据
 
    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)#接受数据
        print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
        if not data:#如果没有数据则关闭
            print >>sys.stderr, 'closing socket', s.getsockname()
            s.close()    



