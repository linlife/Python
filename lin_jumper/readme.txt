堡垒机（192.168.60.130）登录用户名：author_agent	密码:aat
远程服务器和可登录用户：
192.168.60.128	tom,
129.168.60.129	tom,jack
192.168.60.131	tom,jack,mary


数据库表结构
users表：记录用户和密码，以及对应的ID号
servers表：记录服务器的IP地址，和对应的ID号
action_list表：主要记录users 表ID 和servers表ID做外键，提供多对多表查询
record:将用户登录服务器的操作记录下来分成四个内容：用户名，服务器IP,时间，命令记录（其中用户名和服务器IP是通过PICKLE方式记录读取的）




		