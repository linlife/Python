from sql_admin import Admin

def main():
    admin=Admin()
    admin.insert_record('lin','2015','192.168.1.1','hello word')
if __name__=='__main__':
    main()
