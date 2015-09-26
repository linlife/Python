from sql_helper import MySqlHelper

class Admin(object):
    def __init__(self):
        self.__helper = MySqlHelper()
    def get_table_servers(self):#查询servers表
        sql="select * from servers"
        params = None
        return self.__helper.Get_Dict(sql,params)
    def get_table_users(self):#查询users表
        sql="select * from users"
        params = None
        return self.__helper.Get_Dict(sql,params)
    def get_user_id(self,username):#查询user表里面的用户id
        sql="select users.id from users where users.name=%s"
        params = (username,)
        return self.__helper.Get_One(sql,params)
    def get_user_servers(self,userid):#多对多表查询，找出此用户能够登录哪几台服务器。
        sql="select users.name,servers.server_ip from action_list,servers,users where users.id=action_list.user_id and servers.id=action_list.server_id and users.id=%s"
        params=(userid,)
        return self.__helper.Get_Dict(sql,params)

    def insert_record(self,r_name,r_time,r_ip,r_log):#记录用户登录服务器里的操作命令
        sql='insert into record(name,time,ip,log) values(%s,%s,%s,%s)'
        params=(r_name,r_time,r_ip,r_log)
        self.__helper.Insert_one(sql,params)


