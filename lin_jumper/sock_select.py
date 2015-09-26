#!/usr/bin/env python2.7
#_*_ coding:utf-8 _*_
'''
Created On 2015年4月8日
@author : Lin
'''

import select
import socket
import sys
import Queue
 
# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#创建一个server连接口
server.setblocking(0)#对接口设置flag标志位，0表示False:处于非堵塞block状态
 
# Bind the socket to the port
server_address = ('localhost', 10000)#设置端口号
print >>sys.stderr, 'starting up on %s port %s' % server_address#显示输出开始的主机名和端口号
server.bind(server_address)#绑定端口号
 
# Listen for incoming connections
server.listen(5)#同时监听的连接数

# Sockets from which we expect to read
inputs = [ server ]#存放接受进来的数据信息列表

# Sockets to which we expect to write
outputs = [ ]#存放返回数据的信息列表
# Outgoing message queues (socket:Queue)
message_queues = {}#建立存放输入和输出数据的字典，由select


while inputs:#主循环
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'#显示等待
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    #将他们分别赋值为readable,writable,exceptional, 所有在readable list中的socket连接代表有数据可接收(recv),
    #所有在writable list中的存放着你可以对其进行发送(send)操作的socket连接，当连接通信出现error时会把error写到exceptional列表中。
    # Handle inputs
    for s in readable:  #查找readable列表的每个值   
        if s is server:#如果值为server
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()#建立连接
            print >>sys.stderr, 'new connection from', client_address
            connection.setblocking(0)#处于非阻塞
            inputs.append(connection)     
            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()#建立相对应的队列值
            
        else:#已经建立的连接
            data = s.recv(1024)#接受数据
            if data:
                # A readable client socket has data
                print >>sys.stderr, 'received "%s" from %s' % (data, s.getpeername())
                message_queues[s].put(data)#放入对应的队列中
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)#把接受来的数据放到输出列表中
            else:
                    # Interpret empty result as closed connection
                print >>sys.stderr, 'closing', client_address, 'after reading no data'
                    # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)  #既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                inputs.remove(s)    #inputs中也删除掉
                s.close()           #把这个连接关闭掉
         
                # Remove message queue
                del message_queues[s] #从队列中删除  
                    
    print message_queues 
    print 'wriatable:',writable
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
            outputs.remove(s)
        else:
            print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername())
            s.send(next_msg.upper())#发送同样的信息给客户端
    
    # Handle "exceptional conditions"
    for s in exceptional:#报错队列中的数据
        print >>sys.stderr, 'handling exceptional condition for', s.getpeername()
        # Stop listening for input on the connection
        inputs.remove(s)#从输入数据中删除
        if s in outputs:#如果在输出数据里面，也删除
            outputs.remove(s)
        s.close()
     
        # Remove message queue
        del message_queues[s]
    
                
                    