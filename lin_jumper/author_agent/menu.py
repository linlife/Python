import os
import sys
import pickle
from mysqlusing.sql_admin import Admin
msg="""
\033[42;1mWelcome using Lin's auditing system!\033[0m
"""

print msg

admin=Admin()
table_users=admin.get_table_users()
user_id=0

def login():#与数据库中验证用户登录名和密码
    while True:
        try:
            lst_user=[]
            dic_user={}
            uname=raw_input('please enter your administrator name:')
            upassword=raw_input('please enter your aministrator password:')
            for dic in table_users:
                for line in dic:
                    if line=='name' and uname==dic[line]:
                        lst_user.append(dic[line])
                        dic_user=dic
                        break
            if dic_user['password']==upassword:
                lst_user.append(dic_user['password'])
            if len(lst_user)==2:
                print 'Going to connect..... '
                global user_id
                user_id=admin.get_user_id(uname)['id']
                return uname
                break
            else:
                print '\033[31;1myour name or password is not right ,please re-enter.\033[0m'
        except Exception,e:
            print('\033[31;1mplease have right enter,thanks.\033[0m')

def servers(userid):#通过用户的ID找出对应能登录的服务器
    server_lst=[]
    serverips=admin.get_user_servers(userid)
    for dic in serverips:
        for line in dic:
            if line=='server_ip':
                server_lst.append(dic[line])
    return server_lst
    
def server_choice(userid):#显示输出用户可登录的
        print '\033[34;1mHere is your administrator server\033[0m'
        lst=servers(userid)
        for i,j in enumerate(lst):
            print i,j
        print 'Q/q for quit-->'
        return lst
def menu():#主运行程序
    uname=login()
    while True:
        lst=server_choice(user_id)
        try:
            num_ip=raw_input('please choice server number you need login(or q for quit):')
            if num_ip.lower()=='q':break
            if lst[int(num_ip)]:
                print '\033[32;1mGoing to connect \033[0m',lst[int(num_ip)]
                data=[]
                data.append(uname)
                data.append(lst[int(num_ip)])
                with open('tmp.pk','w') as f:#将用户名和登录的服务器IP记录到临时的文件中，方便interactive.py 后面读取并存入数据库
                    pickle.dump(data,f)
                os.system("python /home/author_agent/paramiko-1.10.1/demos/demo2.py %s@%s"%(uname,lst[int(num_ip)]))

        except Exception,e:
            print('\033[32;1mplease enter right number\033[0m')
                


if __name__=='__main__':
    menu()


